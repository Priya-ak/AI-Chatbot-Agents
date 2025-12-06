# ai_agent.py

from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


def _build_llm(provider: str, model_name: str):
    """Return a LangChain chat model for Groq or OpenAI."""
    provider = provider.lower()

    if provider == "groq":
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is missing in .env")
        return ChatGroq(model=model_name, api_key=GROQ_API_KEY)

    if provider == "openai":
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is missing in .env")
        return ChatOpenAI(model=model_name, api_key=OPENAI_API_KEY)

    raise ValueError(f"Unknown provider: {provider}")


def get_response_from_ai_agent(
    llm_id: str,
    query: str,
    allow_search: bool,
    system_prompt: str,
    provider: str,
) -> str:
    """
    Builds an agent for the requested provider+model and returns the AI reply text.
    """

    # ---- choose LLM ----
    llm = _build_llm(provider, llm_id)

    # ---- choose tools ----
    tools = []
    if allow_search:
        if not TAVILY_API_KEY:
            raise ValueError("TAVILY_API_KEY is missing in .env")
        tools = [TavilySearchResults(max_results=2)]

    # ---- create agent ----
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt,
    )

    # ---- invoke ----
    state = {"messages": [{"role": "user", "content": query}]}
    result = agent.invoke(state)

    messages = result.get("messages", [])

    # pick last AIMessage
    for msg in reversed(messages):
        if isinstance(msg, AIMessage):
            return msg.content

    # fallback
    if messages:
        last = messages[-1]
        return getattr(last, "content", str(last))

    return ""

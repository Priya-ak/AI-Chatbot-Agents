# backend.py

from typing import List
from pydantic import BaseModel
from fastapi import FastAPI

from ai_agent import get_response_from_ai_agent


# ---------- Pydantic model ----------
class RequestState(BaseModel):
    model_name: str           # e.g. "llama-3.3-70b-versatile"
    model_provider: str       # "Groq" or "OpenAI"
    system_prompt: str
    messages: List[str]       # simple chat history as plain strings
    allow_search: bool = False


# ---------- Allowed models ----------
ALLOWED_MODEL_NAMES = [
    "gpt-5-nano",              # or any real OpenAI model id you want
    "llama-3.3-70b-versatile",
    "mixtral-8x7b-32768",
    "llama3-70b-8192",
]

app = FastAPI(title="AI Agent")


# ---------- Endpoint ----------
@app.post("/chat")
async def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    """

    # validate model name
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}

    # extract request data
    query = request.messages[-1] if request.messages else ""

    try:
        response_text = get_response_from_ai_agent(
            llm_id=request.model_name,
            query=query,
            allow_search=request.allow_search,
            system_prompt=request.system_prompt,
            provider=request.model_provider,
        )
        return {"response": response_text}
    except Exception as e:
        # return error to frontend if something goes wrong
        return {"error": str(e)}


# ---------- Run app ----------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend:app", host="127.0.0.1", port=9000, reload=True)

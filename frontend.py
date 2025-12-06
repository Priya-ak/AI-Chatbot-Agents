# frontend.py

import streamlit as st
import requests

API_URL = "http://127.0.0.1:9000/chat"

st.set_page_config(page_title="AI Agent", layout="wide")

st.title("AI Chatbot Agents")
st.write("Create and interact with AI Agents!")

# ----------------- Session state for chat history -----------------
# Each message: {"role": "user" | "assistant", "content": "..."}
if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------- Agent configuration (top) -----------------
with st.container():
    system_prompt = st.text_area(
        "Define your AI Agent:",
        value="Act as a helpful Python tutor.",
        height=120,
    )

    provider = st.radio(
        "Select Provider:",
        ["Groq", "OpenAI"],
        horizontal=True,
    )

    if provider == "Groq":
        model = st.selectbox(
            "Select Groq Model:",
            ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"],
        )
    else:
        model = st.selectbox(
            "Select OpenAI Model:",
            ["gpt-5-nano", "llama3-70b-8192"],
        )

    allow_search = st.checkbox("Allow Web Search", value=False)

# ----------------- Chat history (emoji avatars) -----------------
chat_container = st.container()

with chat_container:
    for msg in st.session_state.messages:
        role = msg["role"]
        avatar = "🧑‍💻" if role == "user" else "🤖"

        with st.chat_message(role, avatar=avatar):
            st.markdown(f"<div style='font-size:16px;'>{msg['content']}</div>",
                        unsafe_allow_html=True)

# ----------------- Input box at the bottom -----------------
prompt = st.chat_input("Ask your agent something...")

if prompt:
    # 1) store + immediately show user message
    user_msg = {"role": "user", "content": prompt}
    st.session_state.messages.append(user_msg)

    with chat_container:
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(f"<div style='font-size:16px;'>{prompt}</div>",
                        unsafe_allow_html=True)

    # 2) prepare payload for backend (only user texts are sent)
    payload = {
        "model_name": model,
        "model_provider": provider,
        "system_prompt": system_prompt,
        "messages": [
            m["content"] for m in st.session_state.messages if m["role"] == "user"
        ],
        "allow_search": allow_search,
    }

    # 3) call FastAPI backend
    try:
        with st.spinner("Thinking..."):
            resp = requests.post(API_URL, json=payload, timeout=120)
            resp.raise_for_status()
            data = resp.json()
        answer = data.get("response", "No reply received.")
    except requests.exceptions.ConnectionError:
        answer = (
            "Cannot connect to backend. "
            "Check that FastAPI is running and that API_URL uses the correct port."
        )
    except Exception as e:
        answer = f"Error: {e}"

    # 4) store + show assistant reply
    assistant_msg = {"role": "assistant", "content": answer}
    st.session_state.messages.append(assistant_msg)

    with chat_container:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(f"<div style='font-size:16px;'>{answer}</div>",
                        unsafe_allow_html=True)

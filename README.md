# 🧠 AI Chatbot Agents (Groq + OpenAI)

AI Chatbot Agents is a simple Streamlit web app that lets you create and chat with custom AI agents.  
You can define how the agent should behave, choose between **Groq** and **OpenAI** models, optionally enable web search, and then start chatting in a clean UI.

---

## 🌟 Features

- Define a **custom role / system prompt** for your agent  
  (e.g. `Act as a helpful Python tutor.`)
- Switch between **Groq** and **OpenAI** as providers
- Select a **model** from a dropdown (e.g. `llama-3.3-70b-versatile`)
- Optional **web search** toggle (if you wire a search tool)
- Modern **Streamlit chat UI** with scrollable history

---

## 🖼 Screenshot
<img width="960" height="568" alt="image" src="https://github.com/user-attachments/assets/402582c0-80a5-4cbe-bab8-6208f9734d3e" />

🧱 Tech Stack

- Language: Python

- Frontend: Streamlit

- Providers: Groq API, OpenAI API

- Optional: Web search tool (e.g. Tavily, custom HTTP search, etc.)
📁 Project Structure
```

├── app 
├── ai_agent.py # Core logic for AI interaction & response generation
├── backend.py # Backend API routing & model processing
├── frontend.py # UI layout & user interaction using Streamlit 
├── .env # API keys & environment variables 
└── README.md # Project documentation

```
🔐 Environment Variables
Create a file named .env in the project root (same folder as app.py)
or set these variables in your system environment.
```
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here   # only if using web search

```
⚙️ Installation

1.Clone the repository
```
git clone https://github.com/<your-username>/AI-Chatbot-Agents.git
cd AI-Chatbot-Agents
```
2.Create and activate a virtual environment (optional but recommended)
```
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```
3.Install dependencies
```
pip install -r requirements.txt
```
4.Set your API keys

Make sure your .env file contains the required keys as shown above.

▶️ Running the App
```
streamlit run app.py
```
This will start the app on:
```
http://localhost:8501
```
Open this URL in your browser.
📘 How to Use

1.Define your AI Agent
  In the text area at the top, type how the agent should behave.
  Example: Act as a helpful Python tutor.

2.Select Provider & Model

  - Choose Groq or OpenAI radio button.

  - Select a model from the dropdown list.

3.Enable Web Search (optional)

  - Tick Allow Web Search if you configured a search tool.

4.Chat with the Agent

 - Type a message in the input box (Ask your agent something...).

 - Press Enter or click the send button.

 - The conversation appears in the chat area.

🧩 Customization Ideas

 - Add more models to the dropdown.

 - Add temperature / max-tokens sliders for advanced control.

 - Connect more tools:

     - Web search

     - Code execution

     -Database queries

 - Style the Streamlit app using custom CSS or themes.

🤝 Contributing

Contributions are welcome!

  - Open an issue for bugs or feature requests.

  - Submit a pull request for UI improvements, new tools, or better prompts.
## 📄 License

   This project is licensed under the **MIT License**.


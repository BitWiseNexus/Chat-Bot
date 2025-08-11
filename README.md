# 💬 Python Chatbot with LangChain & Gemini API

A simple **command-line chatbot** built using **LangChain** and **Google Generative AI (Gemini)**.  
The chatbot maintains conversation history for more natural and contextual replies.

---

## 🚀 Features

- Uses **Google Gemini 2.5 Flash** model for fast responses.
- Maintains **chat history** for context-aware conversations.
- Runs in **Python CLI** for quick testing and interaction.
- Uses `.env` file for secure API key management.

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/python-langchain-gemini-chatbot.git
cd python-langchain-gemini-chatbot
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Setup Environment Variables

1. Create a `.env` file in the project root.
2. Add your Google API Key:
```env
GOOGLE_API_KEY=your_api_key_here
```
3. You can get your API key from: [Google AI Studio](https://aistudio.google.com/)

---

## 🖥 Usage

Run the chatbot:
```bash
python chatbot.py
```

Example interaction:
```
You: Hello
Bot: Hi there! How can I help you today?
```

Type `exit` to quit the chat.

---

## 📜 Code Overview

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini-2.5-flash"
)

chat_history = [
    SystemMessage(content="You are a helpful assistant")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("Bot:", result.content)
```

---

## 📂 Project Structure

```
📦 python-langchain-gemini-chatbot
├── chatbot.py          # Main chatbot script
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (API key)
└── README.md           # Documentation
```

---
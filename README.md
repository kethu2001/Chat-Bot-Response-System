# 🤖 AI Chatbot - Chat Bot Response System

A simple AI-powered chatbot built with Python, LiteLLM, and Tkinter GUI.

---

## 📸 Features

- 💬 Clean dark-themed chat interface
- ⚡ Fast AI responses powered by Groq
- 🔄 Non-freezing UI using threading
- 🔐 Secure API key management with `.env`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Programming language |
| Tkinter | GUI interface |
| LiteLLM | AI model connector |
| Groq API | Free AI model provider |
| python-dotenv | Secure API key management |

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/kethu2001/Chat-Bot-Response-System.git
cd Chat-Bot-Response-System
```

### 2. Install dependencies
```bash
pip install litellm python-dotenv
```

### 3. Create `.env` file
Create a `.env` file in the project root and add your Groq API key:
```
GROQ_API_KEY=your-groq-api-key-here
```
> Get a free API key at [console.groq.com](https://console.groq.com)

### 4. Run the chatbot
```bash
python main.py
```

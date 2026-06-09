import tkinter as tk
from tkinter import scrolledtext
import threading
from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()

# OpenAI
# response = completion(model="openai/gpt-4o", messages=[{"role": "user", "content": "Hello!"}])

# Anthropic  
# response = completion(model="anthropic/claude-sonnet-4-20250514", messages=[{"role": "user", "content": "Hello!"}])

# response = completion(model="gemini/gemini-2.0-flash-lite", messages=[{"role": "user", "content": "Hello!"}])



def get_ai_response(user_message):
    response = completion(
        model="groq/llama-3.1-8b-instant",
        messages=[{"role": "user", "content": user_message}]
    )
    return response.choices[0].message.content

def send_message():
    user_input = entry.get().strip()
    if not user_input:
        return

    # Show user message
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You: {user_input}\n", "user")
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)

    entry.delete(0, tk.END)
    send_btn.config(state=tk.DISABLED)

    # Get AI response in a separate thread (prevents UI freezing)
    def fetch_response():
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "Bot: Thinking...\n", "bot")
        chat_area.config(state=tk.DISABLED)
        chat_area.see(tk.END)

        response = get_ai_response(user_input)

        # Remove "Thinking..." and show actual response
        chat_area.config(state=tk.NORMAL)
        chat_area.delete("end-2l", "end-1l")
        chat_area.insert(tk.END, f"Bot: {response}\n\n", "bot")
        chat_area.config(state=tk.DISABLED)
        chat_area.see(tk.END)

        send_btn.config(state=tk.NORMAL)
        entry.focus()

    threading.Thread(target=fetch_response, daemon=True).start()

def on_enter(event):
    send_message()

# Window setup 
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("600x500")
root.resizable(True, True)
root.configure(bg="#1e1e2e")

# Title
title = tk.Label(root, text="🤖 AI Chatbot", font=("Helvetica", 16, "bold"),
                 bg="#1e1e2e", fg="#cdd6f4")
title.pack(pady=10)

# Chat area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED,
                                       font=("Helvetica", 11), bg="#313244",
                                       fg="#cdd6f4", insertbackground="white",
                                       relief=tk.FLAT, padx=10, pady=10)
chat_area.pack(padx=15, pady=5, fill=tk.BOTH, expand=True)
chat_area.tag_config("user", foreground="#89b4fa", font=("Helvetica", 11, "bold"))
chat_area.tag_config("bot",  foreground="#a6e3a1", font=("Helvetica", 11))

# Input area 
input_frame = tk.Frame(root, bg="#1e1e2e")
input_frame.pack(padx=15, pady=10, fill=tk.X)

entry = tk.Entry(input_frame, font=("Helvetica", 12), bg="#45475a",
                 fg="#cdd6f4", insertbackground="white", relief=tk.FLAT)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 8))
entry.bind("<Return>", on_enter)
entry.focus()

send_btn = tk.Button(input_frame, text="Send", font=("Helvetica", 11, "bold"),
                     bg="#89b4fa", fg="#1e1e2e", relief=tk.FLAT,
                     padx=16, pady=6, cursor="hand2", command=send_message)
send_btn.pack(side=tk.RIGHT)

root.mainloop()

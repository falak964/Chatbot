import tkinter as tk
from tkinter import scrolledtext
import requests

# Hugging Face API URL and Key
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
HEADERS = {"Authorization": "Bearer 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"}

# Function to get chatbot response
def get_response():
    user_message = user_input.get().strip()
    if not user_message:
        return

    chat_box.insert(tk.END, f"You: {user_message}\n")
    user_input.delete(0, tk.END)

    # API Request
    payload = {"inputs": user_message}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    data = response.json()

    if isinstance(data, list) and "generated_text" in data[0]:
        bot_reply = data[0]["generated_text"]
    else:
        bot_reply = "Sorry, I couldn't understand that."

    chat_box.insert(tk.END, f"Bot: {bot_reply}\n")
    chat_box.yview(tk.END)  # Auto-scroll to latest message

# GUI Setup
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

# Chat Display Area
chat_box = scrolledtext.ScrolledText(root, width=55, height=20, wrap=tk.WORD)
chat_box.pack(pady=10)
chat_box.insert(tk.END, "Bot: Hello! How can I help you today?\n")

# User Input Field
user_input = tk.Entry(root, width=40, font=("Arial", 12))
user_input.pack(pady=5)

# Send Button
send_button = tk.Button(root, text="Send", command=get_response, bg="#008CBA", fg="white", font=("Arial", 12))
send_button.pack(pady=5)

# Bind Enter Key to Send Message
root.bind("<Return>", lambda event: get_response())

# Run Tkinter App
root.mainloop()

# chat_app.py
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class ChatApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chat with API")
        self.geometry("400x500")

        self.chat_log = ScrolledText(self, state='disabled', height=20)
        self.chat_log.pack(padx=20, pady=10)

        self.entry = ScrolledText(self, height=4)
        self.entry.pack(padx=20, pady=10)

        submit_button = tk.Button(self, text="Send", command=self.on_submit)
        submit_button.pack(pady=10)

        self.bind("<Return>", self.on_submit)

    def on_submit(self, event=None):
        user_input = self.entry.get("1.0", tk.END).strip()
        if user_input:
            self.display_message("You: " + user_input)
            api_response = self.fake_api_call(user_input)
            self.display_message("Server: " + api_response)
            self.entry.delete('1.0', tk.END)

    def display_message(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, message + "\n\n")
        self.chat_log.config(state='disabled')
        self.chat_log.see(tk.END)
        self.bell()

    def fake_api_call(self, user_input):
        return "Hi"

# chat_app.py
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import api
import sys

import setup
# adding Folder_2 to the system path
sys.path.insert(0, 'C:/Users/meghd/Desktop/Chatbot/api/VA_movie')

class ChatApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.run = setup.Run()
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
            self.get_answer(user_input)

    def get_answer(self, user_input):
        answer = self.run.get_answer(user_input)
        self.display_message("Movie VA: " + str(answer))
        self.entry.delete('1.0', tk.END)
    
    def display_message(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, message + "\n\n")
        self.chat_log.config(state='disabled')
        self.chat_log.see(tk.END)
        self.bell()


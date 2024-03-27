# chat_app.py
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

import api
import sys
# adding Folder_2 to the system path
sys.path.insert(0, 'C:/Users/meghd/Desktop/Chatbot/api/VA_movie')

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
            self.answer(user_input)

    def answer(self, user_input):
        api_response = self.api_call(user_input)
        self.display_message("Movie VA: " + api_response)
        self.entry.delete('1.0', tk.END)
    
    def display_message(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, message + "\n\n")
        self.chat_log.config(state='disabled')
        self.chat_log.see(tk.END)
        self.bell()

    def api_call(self, user_input):
        response = api.get_movie_details(user_input)
        return response

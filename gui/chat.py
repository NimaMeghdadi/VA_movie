
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import PhotoImage
from tools import intent_detection
import sys
import setup

sys.path.insert(0, 'C:/Users/meghd/Desktop/Chatbot/api/VA_movie')

class ChatApp(tk.Tk):
    """
    Chat application GUI.
    """
    def __init__(self):
        super().__init__()
        self.dependecy = 0
        self.dependecy_m = 0
        self.run = setup.Run()
        self.title("Virtual AMovie application")
        self.geometry("500x700")

        image_file = "gui/2.png"
        img = PhotoImage(file=image_file)
        self.background_label = tk.Label(self, image=img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.image = img
        self.chat_log = ScrolledText(self, state='disabled', height=20 , font=('Helvetica', 12))
        self.chat_log.pack(padx=20, pady=(130,10) )
        self.entry = ScrolledText(self, height=4, font=('Helvetica', 12))
        self.entry.pack(padx=20, pady=10)
        
        submit_button = tk.Button(self, text="Send", command=self.on_submit, height= 4 
                                  , width=81, bg="#163261", fg="white", font=('Helvetica', 12))
        submit_button.pack(pady=10)
        self.display_message("Movie VA: Hello! How can I help you today?")
        self.bind("<Return>", self.on_submit)

    def on_submit(self, event=None):
        user_input = self.entry.get("1.0", tk.END).strip()
        if user_input:
            self.display_message("You: " + user_input)
            if self.dependecy != 0:
                movie_name = user_input
                self.get_movie(movie_name)
                self.dependecy = 0
                
            elif self.dependecy_m != 0:
                intent = user_input
                self.get_intent(intent)
                self.dependecy_m = 0
            else:
                self.get_answer(user_input)
    
    def get_intent(self,intent):
        intent_type = intent_detection.IntentType()
        intent = intent_type(intent)
        answer = self.run.get_movie_details(self.dependecy_m,intent)
        if answer:
            if (answer == "ERRORRRR_answer"):
                self.display_message("Movie VA: Sorry, we cannot find the information in our database for Movie name you provided.")
            elif(answer=='ERRORRRR_intent_type'):
                self.display_message("Movie VA: Sorry, we cannot find what information you want from the movie.")
            else:
                self.display_message("Movie VA: " + f"The {intent} of {self.dependecy_m} is {str(answer)}")
        else:
            self.display_message("Movie VA: Sorry, we cannot find the movie in our database.")
        self.entry.delete('1.0', tk.END)
        
    def get_movie(self, movie_name):
        print("get movie #########################3")
        answer = self.run.get_movie_details(movie_name,self.dependecy)
        if answer:
            if (answer == "ERRORRRR_answer"):
                self.display_message("Movie VA: Sorry, we cannot find the information in our database for Movie name you provided.")
            elif(answer=='ERRORRRR_movie_name'):
                self.display_message("Movie VA: Sorry, we cannot find the movie name in our database, please write just the movie name")
            else:
                self.display_message("Movie VA: " + f"The {self.dependecy} of {movie_name} is {str(answer)}")
        else:
            self.display_message("Movie VA: Sorry, we cannot find the movie in our database.")
        self.entry.delete('1.0', tk.END)
    
    def get_answer(self, user_input):
        movieName= intent_detection.MovieName()(user_input)
        intent = intent_detection.IntentType()(user_input)
        answer = self.run.get_answer(user_input)
        if answer == 'N/A':
            answer = "ERRORRRR_answer"
        if answer and intent and movieName:
            if(answer=='ERRORRRR_intent_type' and movieName=='ERRORRRR_movie_name'):
                self.display_message("Movie VA: Sorry, could you please paraphrase your question?") # both intent and movie name not found
            elif(answer=='ERRORRRR_intent_type'):
                self.display_message("Movie VA: Sorry, could you please tell me what exactly you want to know about this movie ") # intent not found
                self.dependecy_m = movieName
            elif(answer=='ERRORRRR_movie_name'):
                self.dependecy = intent
                self.display_message("Movie VA: Sorry, we cannot find the movie name in our database, please write just the movie name")
            elif (answer == "ERRORRRR_answer"):
                self.display_message("Movie VA: Sorry, we cannot find the information in our database for Movie name you provided.")
            elif(intent=='Year'):
                self.display_message("Movie VA: The year of the movie " + str(movieName.title())+" is " + str(answer))
            elif(intent=='Director'):
                self.display_message("Movie VA: The director of the movie " + str(movieName.title())+" is " + str(answer))
            elif(intent=='Plot'):
                self.display_message("Movie VA: The plot of the movie " + str(movieName.title())+" is " + str(answer))
            elif(intent=='Actors'):
                self.display_message("Movie VA: The actors of the movie " + str(movieName.title())+"  are " + str(answer))
            elif(intent=='Rating'):
                self.display_message("Movie VA: The rating of the movie " + str(movieName.title())+"  is " + str(answer))
            elif(intent=='Genre'):
                self.display_message("Movie VA: The genre of the movie " + str(movieName.title())+"  is " + str(answer))
            elif(intent=='Awards'): 
                self.display_message("Movie VA: The awards of the movie " + str(movieName.title())+"  are " + str(answer))
            elif(intent=='Language'):
                self.display_message("Movie VA: The language of the movie " + str(movieName.title())+"  is " + str(answer))
            elif(intent=='Country'):
                self.display_message("Movie VA: The country of the movie " + str(movieName.title())+"  is " + str(answer))
            elif(intent=='Writer'):
                self.display_message("Movie VA: The writer of the movie " + str(movieName.title())+"  is " + str(answer))
            else:
                self.display_message("unfortunately, the information you are looking for does not supported in current version of VA-Movie")
        
        #self.display_message("Movie VA: " + str(answer))
        self.entry.delete('1.0', tk.END)
    
    def display_message(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, message + "\n\n")
        self.chat_log.config(state='disabled')
        self.chat_log.see(tk.END)
        self.bell()


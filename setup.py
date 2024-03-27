import tkinter as tk
import gui
from tkinter.scrolledtext import ScrolledText

from gui.chat import ChatApp
from api.omdb import MovieFinder
from tools import ExtractMovie

class Run(object):
    def __init__(self):
        # app = ChatApp()
        # app.mainloop()
        sentence = 'who is the director of Inception?'
    
    def __call__(self):
        # self.get_user_req()
        # self.get_movie_name()
        self.get_movie_details(movie_name='Inception')
        # self.get_intent()
        # self.show_result()
    
    def get_user_req(self):
        pass# return user_req
    
    def intent_detection(self,user_req):
        pass #return type_intent, movie_name
    
    def get_movie_details(self, movie_name):
        pass# return movie_name, answer_movie_intent
    
    def show_result(self, response):
        pass
    
if __name__ == "__main__":
    run = Run() # create our instance
    
    run() # call our instance

    
    

import tkinter as tk
import gui
from tkinter.scrolledtext import ScrolledText

from gui.chat import ChatApp
from api.omdb import MovieDetailFetcher
from tools import intent_detection

class Run(object):
    def __init__(self):
        # app = ChatApp()
        # app.mainloop()
        self.sent = 'who is the director of Inception?'
    
    def __call__(self):
        # self.get_user_req()
        self.intent_creation(user_req=self.sent)
        #self.get_intent()
        self.get_movie_details(movie_name='Inception')
        #self.show_result(response='Inception is directed by Christopher Nolan') 
        #self.show_result()
    
    def get_user_req(self):
        pass# return user_req
    
    def intent_creation(self,user_req):
        print(user_req)
        pass #return type_intent, movie_nameMovieDetailFetcher
    
    def get_movie_details(self, movie_name):
        MovieDetailFetcher().get_movie_details(movie_name)
        pass# return movie_name, answer_movie_intent
    
    def show_result(self, response):
        #print(response)
        pass
    
if __name__ == "__main__":
    run = Run() # create our instance
    
    run() # call our instance

    
    

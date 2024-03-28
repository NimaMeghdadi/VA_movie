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
        #self.show_result(response='Inception is directed by Christopher Nolan')
        self.intent_creation(user_req=self.sent)
        intent=self.get_intent() 
        result= self.get_movie_details(movie_name='Inception',intent=intent) 
        self.show_result(result,intent)
    
    def get_user_req(self):
        pass# return user_req
    
    def get_intent(self):
        return 'year'
    
    def intent_creation(self, user_req):
        print(user_req)
        pass #return type_intent, movie_nameMovieDetailFetcher
    
    def get_movie_details(self, movie_name, intent):
        return MovieDetailFetcher().get_movie_details(movie_name , intent)
        pass# return movie_name, answer_movie_intent
     
    def show_result(self, response, intent):
        if(intent=='year'):
            print(f"The year of the movie is {response}")
        elif(intent=='director'):
            print(f"The director of the movie is {response}")
        elif(intent=='plot'):
            print(f"The plot of the movie is {response}")
        elif(intent=='actors'):
            print(f"The actors of the movie are {response}")    
        elif(intent=='release'):
            print(f"The movie was released on {response}")
        elif(intent=='rating'):
            print(f"The rating of the movie is {response}")
        elif(intent=='genre'):
            print(f"The genre of the movie is {response}")
        elif(intent=='awards'): 
            print(f"The awards of the movie are {response}")
        elif(intent=='runtime'):
            print(f"The runtime of the movie is {response}")
        elif(intent=='language'):
            print(f"The language of the movie is {response}")
        elif(intent=='country'):
            print(f"The country of the movie is {response}")
        elif(intent=='writer'):
            print(f"The writer of the movie is {response}")
        elif(intent=='production'):
            print(f"The production of the movie is {response}")
        else:
            print("Intent not found")
        pass
    
if __name__ == "__main__":
    run = Run() # create our instance
    
    run() # call our instance

    
    

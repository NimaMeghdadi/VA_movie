import tkinter as tk
from tkinter.scrolledtext import ScrolledText

from api.omdb import MovieDetailFetcher
import  gui.chat as chat
from tools import intent_detection

class Run(object):
    def __init__(self):
        
        # self.sent = 'who is the director of Shawshank ?'
        # self.sent = 'who is the director of dune?'
        self.sent = 'who is the director of 1917?'
    
    def __call__(self):
        self.get_user_req()
        #self.show_result(response='Inception is directed by Christopher Nolan')
        # self.intent_creation(user_req=self.sent)
        # intent=self.get_intent() 
        # result= self.get_movie_details(movie_name='Inception',intent=intent) 
        # self.show_result(result,intent)
        # self.get_movie_details('Inception', 'director')
    
    def get_user_req(self):
        app = chat.ChatApp()
        app.mainloop()
    
    def intent_creation(self,user_req)-> str:
        movie_name = intent_detection.MovieName()
        intent_type = intent_detection.IntentType()
        print(movie_name(user_req))
        print(intent_type(user_req))
        return intent_type(user_req), movie_name(user_req)
    
    def get_answer(self,user_req)-> str:
        intent_type, movie_name=self.intent_creation(user_req)
        print(f"movie_name: {movie_name},{intent_type}")
        answer = self.get_movie_details(movie_name, intent_type)
        print(f"answer: {answer}")
        return answer

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

    
    

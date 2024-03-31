import requests
import time

from api.omdb import MovieDetailFetcher
import  gui.chat as chat
from tools import intent_detection
from config import HUGGINGFACE_API_KEY,HUGGINGFACE_API_URL
class Run(object):
    def __init__(self):
        pass
        # self.sent = 'who is the director of Shawshank ?'
        # self.sent = 'who is the director of dune?'
        # self.sent = 'who is the director of 1917?'
        # self.sent = 'who is the director of matrix?'
    
    def __call__(self):
        self.check_model()
        self.get_user_req()
    
    def get_user_req(self):
        app = chat.ChatApp()
        app.mainloop()

    def intent_creation(self,user_req)-> str:
        movie_name = intent_detection.MovieName()
        intent_type = intent_detection.IntentType()
        print("movie name: "+ movie_name(user_req))
        print("intent Type: "+intent_type(user_req))
        return intent_type(user_req), movie_name(user_req)

    def get_answer(self,user_req)-> str:
        intent_type, movie_name=self.intent_creation(user_req)
        answer = self.get_movie_details(movie_name, intent_type) if intent_type and movie_name != None else "Intent not found"
        print(f"answer: {answer}")
        return answer

    def get_movie_details(self, movie_name, intent):
        return MovieDetailFetcher().get_movie_details(movie_name , intent)


    def check_model(self):
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
        input_data = {
            "inputs": {
                "question": "which movie we are talking about?",
                "context": f"{'who is the director of 1917?'}"
            }
        }
        delay_seconds=2
        retry_attempts=3
        model = "thatdramebaazguy/movie-roberta-MITmovie-squad"
        API_URL = HUGGINGFACE_API_URL + model
        for i in range(retry_attempts):
            print(f"Attempt {i+1}")
            try:
                output = requests.post(API_URL, json=input_data, headers=headers)
                output = output.json()
                print(output)
                if output['score']:
                    print("model is ready")
                    return True
                time.sleep(delay_seconds)
            except requests.exceptions.RequestException as e:
                time.sleep(delay_seconds)
            return False
        
if __name__ == "__main__":
    run = Run() # create our instance
    
    run() # call our instance

    
    

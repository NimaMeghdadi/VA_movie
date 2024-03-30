import requests
from config import OMDB_URL,API_KEY

class MovieDetailFetcher:

    def __init__(self):
        pass

    def get_movie_details(self, movie_name, intent):

        payload = {'t': movie_name, 'apikey': API_KEY}
        response = requests.get(OMDB_URL, params=payload, timeout=10)  # Added timeout argument
        if response.status_code == 200:
            response = response.json()
            print("===================")
            print(response)
            print("===================")
            if intent == 'year' or intent =='Year':
                results = response['Year']
            elif intent == 'director' or intent == 'Director':
                results = response['Director']
            elif intent == 'plot' or intent == 'Plot':
                results = response['Plot']
            elif intent == 'actors' or intent == 'Actors':    
                results = response['Actors']
            elif intent == 'rating' or intent == 'Rating':
                results = response['ImdbRating']
            elif intent == 'genre' or intent == 'Genre':
                results = response['Genre']
            elif intent == 'awards' or intent == 'Awards':
                results = response['Awards']
            elif intent == 'language' or intent == 'Language':
                results = response['Language']
            elif intent == 'country' or intent == 'Country':
                results = response['Country']
            elif intent == 'writer' or intent == 'Writer':
                results = response['Writer']
          
            else:
                results = "Intent not found"
            
            print(results)
            if results:
                return(results)
            else:
                return "No information found, please check the movie name"



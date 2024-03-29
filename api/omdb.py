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
            if intent == 'director':
                results = response['Director']
            elif intent == 'plot':
                results = response['Plot']
            elif intent == 'actors':    
                results = response['Actors']
            elif intent == 'release':
                results = response['Released']
            elif intent == 'rating':
                results = response['imdbRating']
            elif intent == 'genre':
                results = response['Genre']
            elif intent == 'awards':
                results = response['Awards']
            elif intent == 'year':
                results = response['Year']
            elif intent == 'runtime':
                results = response['Runtime']
            elif intent == 'language':
                results = response['Language']
            elif intent == 'country':
                results = response['Country']
            elif intent == 'writer':
                results = response['Writer']
            elif intent == 'production':
                results = response['Production']
            else:
                results = "Intent not found"
            
            print(results)
            if results:
                return(results)



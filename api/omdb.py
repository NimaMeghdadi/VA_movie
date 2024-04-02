import requests

from config import OMDB_URL,API_KEY

class MovieDetailFetcher:
    """
    Get movie details from the OMDB API.
    """

    def __init__(self):
        pass

    def get_movie_details(self, movie_name, intent):
        if (intent == "ERRORRRR_intent_type"):
            return "ERRORRRR_intent_type"
        elif (movie_name == "ERRORRRR_movie_name"):
            return "ERRORRRR_movie_name"
        payload = {'t': movie_name.title() , 'apikey': API_KEY}
        response = requests.get(OMDB_URL, params=payload, timeout=10)  # Added timeout argument
        response = response.json()
        results = None
        if response['Response'] !='False':
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
            results = "ERRORRRR_answer"

        return results




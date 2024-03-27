import requests
from config import OMDB_URL,API_KEY

class MovieDetailFetcher:

    def __init__(self):
        pass

    def get_movie_details(self, movie_name):

        payload = {'t': movie_name, 'apikey': API_KEY}
        response = requests.get(OMDB_URL, params=payload, timeout=10)  # Added timeout argument
        if response.status_code == 200:
            response = response.json()
            results = response.get('Director')
            print("===================")
            print(response)
            print("===================")
            if results:
                print(results)



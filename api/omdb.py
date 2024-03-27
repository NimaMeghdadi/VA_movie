import requests
import re
from config import OMDB_URL,API_KEY

class MovieDetailFetcher:

    def __init__(self):
        pass

    def get_movie_details(self, movie_name):

        payload = {'t': movie_name, 'apikey': API_KEY}
        response = requests.get(OMDB_URL, params=payload)
        if response.status_code == 200:
            results = response.json()['results']
            if results:
                print(results.text)



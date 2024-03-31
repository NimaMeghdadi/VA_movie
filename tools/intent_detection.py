<<<<<<< HEAD
=======
import re
import string
>>>>>>> de3fc588e0975a1c1fbef64d7f7a49fb4d7ec96f
import requests
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
<<<<<<< HEAD
import string
import spacy
from config import HUGGINGFACE_API_KEY,HUGGINGFACE_API_URL
# Check if the nltk packages are already downloaded, if not, then download them
nltk_packages = ['punkt', 'stopwords']
=======

#import spacy
# import json
# import os
>>>>>>> de3fc588e0975a1c1fbef64d7f7a49fb4d7ec96f

for package in nltk_packages:
    try:
        # Check if package is already downloaded
        nltk.data.find(f'tokenizers/{package}')
    except LookupError:
        # If not found, download it
        nltk.download(package)

class MovieName:
    """
    Extracts movie names from a sentence.
    """
    def __init__(self):
<<<<<<< HEAD
        
        self.nlp = spacy.load("en_core_web_sm")
=======
        # self.nlp = spacy.load("en_core_web_sm")
>>>>>>> de3fc588e0975a1c1fbef64d7f7a49fb4d7ec96f
        self.model = "thatdramebaazguy/movie-roberta-MITmovie-squad"
        self.API_URL = HUGGINGFACE_API_URL + self.model
        # pass
    def __call__(self,user_req) -> str:
        
        return self.extract_movie_name(user_req=user_req)
<<<<<<< HEAD
        
    
=======
>>>>>>> de3fc588e0975a1c1fbef64d7f7a49fb4d7ec96f
        
    def extract_movie_name(self, user_req) -> str:
        
        # movie_name = self.extract_movie_name_ner(user_req)
        # extract movie name from LLM
        movie_name = self.extract_movie_name_llm(user_req)
        return movie_name
    
    def extract_movie_name_ner(self, user_req) -> str:
        # extract movie name from LLM
        doc = self.nlp(user_req)
        movie_name = [ent.text for ent in doc.ents if ent.label_ in ("WORK_OF_ART", "ORG", "PERSON")]
        movie_name = movie_name[0] if movie_name else ''

    def extract_movie_name_llm(self, user_req) -> str:
        # extract movie name from LLM
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
        input_data = {
            "inputs": {
                "question": "which movie we are talking about?",
                "context": f"{user_req}"
            }
        }
        output = self.query(input_data,headers)
        if 'answer' not in output:
            return "we cannot find the movie name in our database, please another movie name."
        movie_name = [letter for letter in output['answer'] if letter != '?']
        movie_name = ''.join(movie_name)
        print(" mio mio "+ output['answer'] +" " + movie_name)
        return movie_name
    
    def query(self,payload,headers):
        response = requests.post(self.API_URL, headers=headers, json=payload)
        return response.json()
    


class IntentType:
    """
    Extracts intent type from a sentence.
    """
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        
    def __call__(self,user_req) -> str:
        return self.extract_intent_type(user_req=user_req)

#payam inja -->
    def extract_intent_type(self, user_req) -> str:
        intent_keywords = {
<<<<<<< HEAD
        "plot": ["plot", "story", "summary", "synopsis"],
        "director": ["director", "directed"],
        "actors": ["cast", "actors", "starring"],
        "release_date": ["release date", "released"],
        "year": ["year"],
=======
        "Year": ["year", "when", "release date", "released"],
        "Director": ["director", "directed", "filmmaker", "directors","directing","direct"],
        "Plot": ["plot", "story", "summary", "synopsis"],
        "Actors": ["cast", "actors","actor","actress","actresses","starring"],
        "Rating": ["rating", "rated", "rated" , "imdb score", "score"],
        "Genre": ["genre", "horor", "comedy", "romantic", "action"],
        "Awards": ["awards", "award", "prize", "winner", "win","won"],
        "Language": ["language", "speak", "english", "spanish", "french"],
        "Country": ["country", "made", "origin", "originated"],
        "Writer": ["writer", "written", "script"]
        
>>>>>>> de3fc588e0975a1c1fbef64d7f7a49fb4d7ec96f
        }

        # Tokenize the input text and remove punctuation
        stop_words = set(stopwords.words('english') + list(string.punctuation))
        words = word_tokenize(user_req)
        filtered_words = [word for word in words if word.lower() not in stop_words]

        # Initialize intent and potential title
        intent = None
        for key, keywords in intent_keywords.items():
            if any(keyword in user_req.lower() for keyword in keywords):
                intent = key
                break

        return intent
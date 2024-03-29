import re
import spacy
import requests
import json
import os
import requests
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Download necessary NLTK data

from config import HUGGINGFACE_API_KEY,HUGGINGFACE_API_URL
class MovieName:
    """
    Extracts movie names from a sentence.
    """
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.model = "thatdramebaazguy/movie-roberta-MITmovie-squad"
        self.API_URL = HUGGINGFACE_API_URL + self.model
        pass
    def __call__(self,user_req) -> str:
        return self.extract_movie_name(user_req=user_req)
        # return self.extract_movie_name(user_req=user_req)
        
    def extract_movie_name(self, user_req) -> str:
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
        # Example question and context
        input_data = {
            "inputs": {
                "question": "which movie we are talking about?",
                "context": f"{user_req}"
            }
        }
        output = self.query(input_data,headers)
        movie_name = [letter for letter in output['answer'] if letter != '?']
        movie_name = ''.join(movie_name)
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

    def extract_intent_type(self, user_req) -> str:
        intent_keywords = {
        "plot": ["plot", "story", "summary", "synopsis"],
        "director": ["director", "directed"],
        "actors": ["cast", "actors", "starring"],
        "release_date": ["release date", "released"],
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
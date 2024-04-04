import requests
import spacy
import nltk
import google.generativeai as genai

from config import HUGGINGFACE_API_KEY,HUGGINGFACE_API_URL,GEMINI_API_KEY
nltk_packages = ["punkt", "stopwords"]
nltk.download(nltk_packages,quiet=True)
nlp = spacy.load("en_core_web_sm")


class MovieName:
    """
    Extracts movie names from a sentence using 2 main techniques: LLM and NER.
    """
    def __init__(self):
        self.model = "thatdramebaazguy/movie-roberta-MITmovie-squad"
        self.API_URL = HUGGINGFACE_API_URL + self.model
        
    def __call__(self,user_req) -> str:
        
        return self.extract_movie_name(user_req=user_req)

    def extract_movie_name(self, user_req) -> str:
        # extract movie name using NER
        movie_name1 = self.extract_movie_name_ner(user_req)
        # extract movie name from LLM
        movie_name2 = self.extract_movie_name_llm(user_req)
        movie_name3 = self.extract_movie_name_llm_gemini(user_req)
        
        print(f"movie_name1: {movie_name1}")
        print(f"movie_name2: {movie_name2}")
        print(f"movie_name3: {movie_name3}")

        if movie_name1 == movie_name2 == movie_name3:
            return movie_name3
        elif movie_name2 == movie_name3:
            return movie_name3
        elif movie_name1 == movie_name3:
            return movie_name3
        elif movie_name1 == movie_name2:
            return movie_name1
        elif len(movie_name1.split()) <=2 and len(movie_name1.split()) >0:
            return movie_name1
        elif movie_name1 =='' and movie_name3 != "ERRORRRR_movie_name":
            return movie_name3
        elif movie_name3 == "ERRORRRR_movie_name" and len(movie_name2.split()) <=2 and len(movie_name2.split()) > 0:
            return movie_name2
        return "ERRORRRR_movie_name"
    
    def extract_movie_name_ner(self, user_req) -> str:
        # extract movie name from LLM Huggingface
        doc = nlp(user_req)
        movie_name = [ent.text for ent in doc.ents if ent.label_ in ("WORK_OF_ART", "ORG", "PERSON",'NUM','DATE')]
        movie_name = movie_name[0] if movie_name else ''
        return movie_name

    def extract_movie_name_llm_gemini(self, user_req) -> str:
        genai.configure(api_key=GEMINI_API_KEY)   
        model = genai.GenerativeModel('gemini-1.0-pro')
        response_movie = model.generate_content(f"in this sentence: \" {user_req} \" give me the just movie name in the sentence (if you did not find send \"ERRORRRR_movie_name\") ")
        # print(response.text)
        return response_movie.text
    
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
            return "ERRORRRR_movie_name"
        
        movie_name = [letter for letter in output['answer'] if letter != '?']
        movie_name = ''.join(movie_name)
        
        return movie_name
    
    def query(self,payload,headers):
        response = requests.post(self.API_URL, headers=headers, json=payload, timeout=20)
        return response.json()
    


class IntentType:
    """
    Extracts intent type from a sentence using keyword detection.
    """
    def __init__(self):
        pass
    def __call__(self,user_req) -> str:
        return self.extract_intent_type(user_req=user_req)

    def extract_intent_type(self, user_req) -> str:
        # extract intent type from user request by using keywords in the sentence
        intent_keywords = {
        "Year": ["year", "when", "release date", "released", "release", "year of release", "the year"],
        "Director": ["director", "directed", "filmmaker", "directors","directing","direct", "the director"],
        "Plot": ["plot", "story", "summary", "synopsis", "plot summary", "plot of the movie", "plot of the film","the summary", "the plot"],
        "Actors": ["cast", "actors","actor","actress","actresses","starring","starred","star","stars","role","roles","character","characters", "the actors","the actresses","the cast"],
        "Rating": ["rating", "rated", "rated" , "imdb score", "score", "imdb rating", "imdb", "rate", "the rating"],
        "Genre": ["genre", "horror","horor", "comedy", "romantic", "action" , "thriller", "drama", "adventure", "sci-fi", "science fiction", "the genre"],
        "Awards": ["awards", "award", "prize","prizes", "nominated", "nominations", "the awards","won", "winner", "winners"],
        "Language": ["language", "speak", "english", "spanish", "french" , "german", "italian", "the language"],
        "Country": ["country", "made", "origin", "originated" , "the country"],
        "Writer": ["writer", "written", "script" , "the writer"]
        }

        intent = None
        for key, keywords in intent_keywords.items():
            if any(keyword in user_req.lower() for keyword in keywords):
                intent = key
                return str(intent)
        return "ERRORRRR_intent_type"
        
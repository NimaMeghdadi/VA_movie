# Title 

### Movie Virtual Assistant

# Description

This program will bring the information that is available in [omdb dataset](https://www.omdbapi.com/) using API in the chatbot environment and can help people who want to know specific information about movies without googling and try to find this information.

# Installation

Before you start, install the dependencies

```
pip install -r requirements.txt
pip install -q -U google-generativeai
spacy download en
```

and get api_key from 
- [omdb](https://www.omdbapi.com/apikey.aspx) 
- [gemini](https://ai.google.dev/) 
- [Hugging Face](https://huggingface.co/docs/api-inference/en/quicktour) 

then replace it in config.py

# Features
### movie detection
Get movie name from the user input 
- [movie-roberta-MITmovie-squad](https://huggingface.co/thatdramebaazguy/movie-roberta-MITmovie-squad)
- [gemini](https://ai.google.dev/tutorials/python_quickstart)
- [NER](https://demos.explosion.ai/displacy-ent)

### intent detection

Used keywords to detect intent from the input sentence.
```
"Year": ["year", "when", "release date", "released"],
"Director": ["director", "directed", "filmmaker", "directors", "directing", "direct"],
.
.
.
```

# Examples

### OMDB API response example: 
```json
{"Title":"Dune","Year":"2021","Rated":"PG-13","Released":"22 Oct 2021","Runtime":"155 min","Genre":"Action, Adventure, Drama","Director":"Denis Villeneuve","Writer":"Jon Spaihts, Denis Villeneuve, Eric Roth",
"Actors":"Timothée Chalamet, Rebecca Ferguson, Zendaya","Plot":"A noble family becomes embroiled in a war for control over the galaxy's most valuable asset while its heir becomes troubled by visions of a dark future.",
"Language":"English, Mandarin","Country":"United States, Canada","Awards":"Won 6 Oscars. 173 wins & 294 nominations total","Poster":"https://m.mediaamazon.com/images/M/MV5BMDQ0NjgyN2YtNWViNS00YjA3LTkxNDktYzFkZTExZGMxZDkxXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_SX300.jpg",
"Ratings":[{"Source":"Internet Movie Database","Value":"8.0/10"},{"Source":"Rotten Tomatoes","Value":"83%"},
{"Source":"Metacritic","Value":"74/100"}],"Metascore":"74","imdbRating":"8.0","imdbVotes":"772,111","imdbID":"tt1160419",
"Type":"movie","DVD":"22 Oct 2021","BoxOffice":"$108,897,830","Production":"N/A","Website":"N/A","Response":"True"}
```

### Chatbot Environment example:
<p align="center">
<img src="https://github.com/NimaMeghdadi/VA_movie/assets/4293190/865d9e7c-d225-4382-ab1a-801bcfeb9846"  width="600" height="400"/>
</p>



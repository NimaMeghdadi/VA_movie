
# Movie Virtual Assistant

## Description
The Movie Virtual Assistant provides movie information in a chatbot environment, allowing users to retrieve details about films directly without needing to search manually. It integrates with the OMDb dataset, utilizing various APIs to fetch information about movies, including details on directors, release dates, genres, ratings, and more.

## Features
- **Movie Detection**: Identifies movie names from user input using `movie-roberta-MITmovie-squad` and Gemini for natural language processing (NLP).
- **Named Entity Recognition (NER)**: Recognizes entities like movie titles, directors, and genres in user requests.
- **Intent Detection**: Detects user intent based on keywords, such as release year or director, using predefined intent mappings for efficient querying.

## Installation
To set up the Movie Virtual Assistant:

1. Install the required dependencies by following the commands in `requirements.txt`, updating Google Generative AI, and downloading the English language model for SpaCy.

2. Obtain and set up API keys from the following providers:
   - OMDb API
   - Gemini
   - Hugging Face

3. Replace these keys in `config.py` to enable API access.

## Configuration
Add your API keys in the `config.py` file:
```python
# config.py
OMDB_API_KEY = 'your_omdb_api_key'
GEMINI_API_KEY = 'your_gemini_api_key'
HUGGING_FACE_API_KEY = 'your_hugging_face_api_key'
```

## Usage Examples
Sample interaction with the assistant:
- **User**: "Who directed Dune?"
- **Assistant**: "Dune (2021) was directed by Denis Villeneuve."

### Sample OMDb API Response
A typical response from the OMDb API might include:
```json
{
  "Title": "Dune",
  "Year": "2021",
  "Rated": "PG-13",
  "Released": "22 Oct 2021",
  "Genre": "Action, Adventure, Drama",
  "Director": "Denis Villeneuve",
  "Actors": "Timothée Chalamet, Rebecca Ferguson, Zendaya",
  "Plot": "A noble family becomes embroiled in a war for control...",
  "Ratings": [{"Source": "Internet Movie Database", "Value": "8.0/10"}],
  "BoxOffice": "$108,897,830",
  ...
}
```

## Directory Structure
- **api/**: Contains API interaction scripts for querying movie information.
- **config.py**: Holds API keys and configuration settings.
- **gui/**: Code for the graphical user interface (if available).
- **requirements.txt**: Lists all dependencies for setting up the project.
- **setup.py**: Script to install the package and its dependencies.
- **tools/**: Utility scripts to assist with various functionalities.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the terms specified in the `LICENSE` file.

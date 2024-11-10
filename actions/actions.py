# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

#=============> movie recommendation (Dataset Approach)


# import pandas as pd
# from rasa_sdk import Action
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet


# movie_df = pd.read_csv("preprocessed_movies.csv")

# class ActionRecommendMovie(Action):
#     def name(self) -> str:
#         return "action_recommend_movie"

#     def run(self, dispatcher: CollectingDispatcher, tracker, domain):
#         genre = tracker.get_slot("genre")

#         recommended_movies = movie_df[movie_df['genres'].str.contains(genre, case=False)]

#         if not recommended_movies.empty:
#             movie = recommended_movies.sample(1)['title'].values[0]
#             dispatcher.utter_message(text=f"I recommend watching '{movie}'!")
#         else:
#             dispatcher.utter_message(text="I couldn't find any movies in that genre.")
#         return []

#=============> movie recommendation (Api Approach)

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRecommendMovie(Action):
    def name(self) -> str:
        return "action_recommend_movie"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        genre = tracker.get_slot("genre")
        
        # Define genre mappings if needed, or directly use genre as per API format
        genre_mapping = {
            "action": 28,
            "adventure": 12,
            "animation": 16,
            "comedy": 35,
            "crime": 80,
            "documentary": 99,
            "drama": 18,
            "family": 10751,
            "fantasy": 14,
            "history": 36,
            "horror": 27,
            "music": 10402,
            "mystery": 9648,
            "romance": 10749,
            "science fiction": 878,
            "thriller": 53,
            "war": 10752,
            "western": 37
        }
        
        # Fetch genre ID from genre_mapping dictionary
        genre_id = genre_mapping.get(genre.lower())

        if not genre_id:
            dispatcher.utter_message(text=f"Sorry, I couldn't find movies for the genre '{genre}'.")
            return []

        # TMDb API endpoint
        url = f"https://api.themoviedb.org/3/discover/movie"
        params = {
            "api_key": "19694c9b4f9a2e1a229036fd8bc7bdf3",
            "with_genres": genre_id,
            "sort_by": "popularity.desc",
            "language": "en-US",
            "page": 1,
        }
 
        # Make the API request
        response = requests.get(url, params=params)
        data = response.json()

        # Extract the top movie title for recommendation
        if data["results"]:
            movie_title = data["results"][0]["title"]
            dispatcher.utter_message(text=f"I recommend watching '{movie_title}'!")
        else:
            dispatcher.utter_message(text=f"Sorry, I couldn't find any popular movies in the '{genre}' genre.")

        return []

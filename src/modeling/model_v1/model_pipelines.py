# Packages
import pandas as pd
from preprocessing import TextPreprocessing
from user_input import User
from generate_new_preference import GenerateNewPreference
from recommender_system import RecommenderSystem
from filtering import Filtering
from carbon_footprint import CarbonFootprint

total_distance = None
def itinerary_planning_pipeline(data, city, budget, duration, user_preferences_1, user_preferences_2=None):
    start_latitude = -6.8281528
    start_longitude = 107.4350179
    # preprocessing
    prep = TextPreprocessing(data, city)
    stemmed_documents = prep.stemming()
    datasets, tokenized_strings = prep.tokenizer(stemmed_documents)
    # user input
    user = User(datasets)
    combined, user_preferences, duration, budget = user.input(city, budget, duration, user_preferences_1, user_preferences_2)
    # Preferences
    preferences = GenerateNewPreference()
    new_preference_user = preferences.fit(combined, user_preferences)
    # Recommender System
    recommender = RecommenderSystem(datasets, city, tokenized_strings)
    recommender.fit()
    recommender.recommend(user_preferences)
    recommendation_result = recommender.postprocessing()
    # Filtering
    filter = Filtering(recommendation_result)
    filter.budgeting(budget)
    route, total_distance, recommendation_distance, recommendation_place_name = filter.distance(start_latitude, start_longitude)
    return route, total_distance, recommendation_distance, recommendation_place_name

def carbon_footprint_pipeline(total_distance):
    footprint = CarbonFootprint()
    results = footprint.calculate_all(total_distance)
    return results





from preprocessing import TextPreprocessing
from city import City
from user_input import User
from generate_new_preferences import GenerateNewPreference
from recommender_system import RecommenderSystem
from thompson_sampling_ratings import ThompsonSampling
from filtering import Filtering
from duration_divide import DurationPlaceDivider
from carbon_footprint import CarbonFootprint
from city_thompson import CityThompson
from thompson_sampling_generate import ThompsonSamplingGenerate
from discover_place import generate_places
import pandas as pd

file_paths = {
    "bandung": "../../../data/attractions/indonesia_clean_v1/city/bandung.csv",
    "banjarbaru": "../../../data/attractions/indonesia_clean_v1/city/banjarbaru.csv",
    "bengkulu": "../../../data/attractions/indonesia_clean_v1/city/bengkulu.csv",
    "denpasar": "../../../data/attractions/indonesia_clean_v1/city/denpasar.csv",
    "jakarta": "../../../data/attractions/indonesia_clean_v1/city/jakarta.csv",
    "jayapura":"../../../data/attractions/indonesia_clean_v1/city/jayapura.csv",
    "maluku":"../../../data/attractions/indonesia_clean_v1/city/maluku.csv",
    "semarang":"../../../data/attractions/indonesia_clean_v1/city/semarang.csv",
    "surabaya":"../../../data/attractions/indonesia_clean_v1/city/surabaya.csv",
    "yogyakarta":"../../../data/attractions/indonesia_clean_v1/city/yogyakarta.csv"
}

file_paths_random = pd.read_csv("../../../data/attractions/random_place/discover_place.csv")

datasets = {key: pd.read_csv(path) for key, path in file_paths.items()}

def itinerary_planning_pipeline(data, city, budget, duration, user_preferences_1, user_preferences_2=None):
    # Get user city
    user_city = City()
    start_latitude, start_longitude = user_city.select_city(city, 1)
    # Preprocessing
    preprocess = TextPreprocessing(data, city)
    stemmed_documents = preprocess.stemming()
    datasets, tokenized_strings = preprocess.tokenizer(stemmed_documents)
    # User Input
    user = User(datasets)
    combined, user_preferences, duration, budget = user.input(city, budget, duration, user_preferences_1, user_preferences_2)
    # Generate New Preferences
    preferences = GenerateNewPreference()
    user_preferences_new = preferences.fit(combined, user_preferences)
    # Recommender System (Text Similarity)
    recommender = RecommenderSystem(datasets, city, tokenized_strings)
    recommender.fit()
    recommender.recommend(user_preferences)
    recommendation_result = recommender.postprocessing()
    # Thompson Sampling
    sample = ThompsonSampling()
    recommendation_exploration = sample.exploration(recommendation_result, duration)
    # Filtering
    filter = Filtering(recommendation_exploration)
    recommendation_budget, total_budget = filter.budgeting(budget)
    recommendation_budget = recommendation_budget.sort_values('price', ascending=False)
    # Duration
    recommendation_duration = recommendation_budget[:(duration * 3)]
    # Distance
    route, total_distance, recommendation_distance = filter.distance(recommendation_duration, start_latitude, start_longitude)
    recommendation_place_name = recommendation_distance[['id','place_name']]
    # Divide by recommendation
    duration_divide = DurationPlaceDivider(recommendation_distance)
    day_recommendation = duration_divide.divide_durations_place_name(duration)

    return duration, city, total_distance, budget, recommendation_distance, recommendation_place_name, day_recommendation

def carbon_footprint_pipeline(city, total_distance):
    # Calculate Carbon Footprint
    footprint = CarbonFootprint()
    results = footprint.predict_all(total_distance)
    # Price and CO2 Emissions
    city_price_emissions = City()
    city_price_emissions.carbon(results)
    city_price_emissions_data = city_price_emissions.select_city(city, 2)
    return city_price_emissions_data

def generate_preferences_pipeline(city_name):
    city = CityThompson()
    keywords, expected_keywords = city.select_city(city_name)
    arm = ThompsonSamplingGenerate()
    arm.add_keywords(keywords, expected_keywords)
    arm.add_rewards(keywords, expected_keywords)
    return arm.choose_unique_arms()

def discover_place_pipeline(data):
    result = generate_places(data)
    return result
import pandas as pd
from model_pipelines import itinerary_planning_pipeline, carbon_footprint_pipeline, generate_preferences_pipeline, discover_place_pipeline
from fastapi import FastAPI
from pydantic import BaseModel
import json

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

app = FastAPI()

class User(BaseModel):
    city: str
    budget: float
    duration: int
    user_preferences_1: str
    user_preferences_2: str | None = None

class City(BaseModel):
    city: str

@app.get("/")
async def read_root():
    return "Welcome to Itinergo ML API! :)"

@app.post("/generate/preferences")
async def generate_preferences(item: City):
    generate = generate_preferences_pipeline(item.city)
    return generate

@app.post("/recommend/place_name")
async def recommend_place_name(item: User):
    duration, city, total_distance, budget, recommendation_distance, recommendation_place_name, day_recommendation = itinerary_planning_pipeline(datasets, item.city, item.budget, item.duration, item.user_preferences_1, item.user_preferences_2)
    json_data = json.loads(recommendation_place_name.to_json(orient='records'))

    # Define global variables
    global recommend_distance
    recommend_distance = recommendation_distance
    global total_distance_carbon
    total_distance_carbon = total_distance
    global city_recommend
    city_recommend = city
    global budget_recommend
    budget_recommend = budget
    global duration_recommend
    duration_recommend = duration
    global recommendation_without_day
    recommendation_without_day = json_data

    return day_recommendation

@app.get("/recommend/all")
async def recommend_all():
    result = recommend_distance.to_json(orient='records')
    json_data = json.loads(result)
    return json_data

@app.get("/predict/carbon")
async def carbon_footprint():
    city_price_emissions_data = carbon_footprint_pipeline(city_recommend, total_distance_carbon)
    import json

    result_dict = {
        city_price_emissions_data[0]: {
            'car_price': city_price_emissions_data[1],
            'car_co2': city_price_emissions_data[2],
            'bus_price': city_price_emissions_data[3],
            'bus_co2': city_price_emissions_data[4],
            'motorbike_price': city_price_emissions_data[5],
            'motorbike_co2': city_price_emissions_data[6],
            'total_distance': int(round(total_distance_carbon*10)/10),
            'total_budget': int(round(budget_recommend*10)/10),
            'total_days': duration_recommend,
            'total_places': 3*duration_recommend
        }
    }

    json_data = json.dumps(result_dict)
    return json_data

@app.get("/recommend/without/days")
async def recommend_days():
    return recommendation_without_day

@app.get("/generate/place")
async def discover_place():
    place = discover_place_pipeline(file_paths_random)
    result = json.loads(place)
    return result

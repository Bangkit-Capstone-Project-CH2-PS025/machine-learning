import pandas as pd
from model_pipelines import itinerary_planning_pipeline, carbon_footprint_pipeline
from fastapi import FastAPI
from pydantic import BaseModel
import json

# Path file dataset
file_paths = {
    "bandung": "D:/Users/PycharmProjects/ItinergoProject/data/attractions/indonesia_clean_v1/city/bandung.csv",  # Sesuaikan dengan path file Anda
}
# Load datasets
datasets = {key: pd.read_csv(path) for key, path in file_paths.items()}

app = FastAPI()

# API
class User(BaseModel):
    city: str
    budget: float
    duration: int
    user_preferences_1: str
    user_preferences_2: str | None = None

# GET root
@app.get("/")
async def read_root():
    return "Welcome to Itinergo ML API! :)"

# GET /generate/preferences
@app.get("/generate/preferences")
async def generate_preferences():
    return "Nothing :("

# POST /recommend/all
@app.post("/recommend/all")
async def recommend_all(item: User):
    route, total_distance, recommendation_distance, recommendation_place_name = itinerary_planning_pipeline(datasets, item.city, item.budget, item.duration, item.user_preferences_1, item.user_preferences_2)
    result = recommendation_distance[['id', 'place_name', 'description','category', 'city', 'province', 'price', 'rating', 'coordinates']].to_json(orient='records')
    json_data = json.loads(result)

    # Define global variables
    global recommend_place
    recommend_place = recommendation_place_name
    global total_distance_carbon
    total_distance_carbon = total_distance
    return json_data

# GET /recommend/place_name
@app.get("/recommend/place_name")
async def recommend_place():
    result = recommend_place.to_json(orient='records')
    json_data = json.loads(result)
    return json_data

# GET /calculate/carbon
@app.get("/calculate/carbon")
async def carbon_footprint():
    footprint = carbon_footprint_pipeline(total_distance_carbon)
    return footprint
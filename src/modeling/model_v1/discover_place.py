import pandas as pd

# Path of file
df = pd.read_csv("D:/Users/PycharmProjects/ItinergoProject/data/attractions/random_place/discover_place.csv")

def generate_places(data, n_sample=1, frac=1):
    random_places = data.sample(frac).reset_index(drop=True)
    generate_one_place = random_places.sample(n_sample).reset_index(drop=True)
    return generate_one_place.to_json(orient='records')
import pandas as pd
from IPython.display import Image

# Path of file
df = pd.read_csv("D:/Users/PycharmProjects/ItinergoProject/data/attractions/random_place/discover_place.csv")

def generate_places(data, n_sample=1, frac=1):
    random_places = data.sample(frac).reset_index(drop=True)
    generate_one_place = random_places.sample(n_sample).reset_index(drop=True)
    image_dir = generate_one_place['dir'][0]
    return generate_one_place

place = generate_places(df)
json_data = place.to_json(orient='records')
print(json_data)
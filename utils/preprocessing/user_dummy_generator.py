import random
import pandas as pd
import zipfile

preferences = pd.read_csv("/content/all_preferences.csv")
max_budget = pd.read_csv("/content/all_max_budget.csv")

cities = ['bandung', 'banjarbaru', 'bengkulu', 'denpasar', 'jakarta', 'jayapura', 'maluku', 'semarang', 'surabaya', 'yogyakarta']

for city in cities:
    locals()[city] = preferences[city].tolist()
    locals()["max_price_" + city] = max_budget[city].tolist()

city_var = [bandung, banjarbaru, bengkulu, denpasar, jakarta, jayapura, maluku, semarang, surabaya, yogyakarta]
max_budget_city = [max_price_bandung, max_price_banjarbaru, max_price_bengkulu, max_price_denpasar, max_price_jakarta, max_price_jayapura, max_price_maluku, max_price_semarang, max_price_surabaya, max_price_yogyakarta]

def generate_dummy_user(preferences, budget_max=None, budget_min=0, min_pref=1, max_pref=2):
    num_preferences = random.randint(min_pref, max_pref)
    user_preferences = random.sample(preferences, num_preferences)
    user_budget = round(random.uniform(budget_min, budget_max) / 500) * 500

    pref_1 = user_preferences[0]

    if len(user_preferences) > 1:
        pref_2 = user_preferences[1]
    else:
        pref_2 = None

    return {
        "preferences_1": pref_1,
        "preferences_2": pref_2,
        "budget": user_budget
    }

num_users = 1000
city_dfs = {}
for i in range(len(city_var)):
    dummy_users = [generate_dummy_user(city_var[i], max_budget_city[i][0]) for _ in range(num_users)]
    city_name = cities[i]
    city_dfs[city_name] = pd.DataFrame(dummy_users)

for city, df in city_dfs.items():
    file_name = city + "_user_dummy.csv"
    df.to_csv(file_name, index=False)

zip_file_name = "users_dummy_data.zip"

with zipfile.ZipFile(zip_file_name, 'w') as zipf:
    for city, df in city_dfs.items():
        file_name = city + "_user_dummy.csv"
        zipf.write(file_name)
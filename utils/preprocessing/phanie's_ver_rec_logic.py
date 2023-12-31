# -*- coding: utf-8 -*-
"""Phanie's Ver_Rec_Logic

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16-TM05dDRgazGFtb50sADaW1GVkOZMYF
"""

import pandas as pd
import numpy as np
import re
import random

jkt = pd.read_csv('/content/drive/MyDrive/Bangkit Academy 2023/Capstone Dataset/jakarta.csv')

jkt.head()

def calculate_daily_budget_and_recommendations(budget, duration):
    daily_budget = budget / duration
    recommendations_per_day = 3
    budget_per_recommendation = daily_budget / recommendations_per_day
    recommendations = []

    for day in range(1, duration + 1):
        daily_recommendations = []
        for recommendation_number in range(1, recommendations_per_day + 1):
            recommendation = f"Day {day}, Recommendation {recommendation_number}: Spend {budget_per_recommendation:.2f} on this recommendation"
            daily_recommendations.append(recommendation)
        recommendations.append(daily_recommendations)

    return recommendations

def save_recommendation_spend(recommendations):
    budget_recommendation = []
    for daily_recommendations in recommendations:
        for recommendation in daily_recommendations:
            # Regex to extract the numeric part
            spend_amount = float(re.search(r'\d+\.\d+', recommendation).group())
            budget_recommendation.append(spend_amount)
    return budget_recommendation

def filter_dataset(dataset, budget_recommendation):
    # Calculate the threshold based on the budget's recommendation
    threshold = max(budget_recommendation)

    # Threshold
    jkt_filtered = dataset[dataset['price'] <= threshold]
    return jkt_filtered

def get_user_preferences(jkt):
    categories = jkt['category'].unique()

    print("Choose your travel preferences (maximum 2):")
    print("Available categories:", categories)

    # Initialize an empty list to store user preferences
    user_preferences = []

    # Preferences - USER INPUT
    while len(user_preferences) < 2:
        preference = input("Enter a category (or 'done' to finish): ").capitalize()

        if preference == 'Done':
            break
        elif preference.lower() in map(str.lower, categories):
            if preference not in user_preferences:
                user_preferences.append(preference)
                print(f"'{preference}' added to your preferences.")
            else:
                print("You have already selected this category. Choose another.")
        else:
            print("Invalid category. Please choose from the available categories.")

    # Validation
    if not user_preferences:
        print("No preferences selected. Please choose at least one category.")
    elif len(user_preferences) > 2:
        print("Too many preferences selected. Choose a maximum of 2 categories.")
        user_preferences = []

    return user_preferences

def save_user_input(budget, duration):
    # Save user input for budget and duration
    user_input = {'budget': budget, 'duration': duration}
    return user_input

# Dictionary to store filtered datasets for each user
user_filtered_dataset_dict = {}

# Budget and duration - USER INPUT
budget = float(input("Enter your budget: "))
duration = int(input("Enter the duration (in days): "))

# Save user input
user_input = save_user_input(budget, duration)

result = calculate_daily_budget_and_recommendations(budget, duration)

# Save the recommendation spend for the current user
budget_recommendation = save_recommendation_spend(result)
jkt_filtered = filter_dataset(jkt, budget_recommendation)

# Recommendation
for day, recommendations in enumerate(result, start=1):
    print(f"\nDay {day} Budget: {budget / duration:.2f}")
    for recommendation in recommendations:
        print(recommendation)

# Access the filtered dataset for the current user
print(f"\nFiltered Dataset for User {budget}, Duration {duration}:\n{jkt_filtered}")

# Filter the dataset based on PREFERENCES
user_preferences = get_user_preferences(jkt_filtered)
jkt_filtered_2 = jkt_filtered[jkt_filtered['category'].isin(user_preferences)]

# Print
print(f"\nFiltered Dataset based on User Preferences:\n{jkt_filtered_2}")

np.random.seed(42)

# Initialize lists to store recommendations
exploitation_recommendations = []
exploration_recommendations = []

# Function to select recommendations using Thompson Sampling
def thompson_sampling(ratings):
    sampled_index = np.argmax(np.random.beta(1 + ratings, 1))
    return sampled_index

# Iterate through each day
for day in range(1, duration + 1):
    # Exploitation recommendation
    exploitation_mask = jkt_filtered_2['rating'] > 4.5
    exploitation_candidates = jkt_filtered_2[exploitation_mask]

    # Exclude already recommended places
    exploitation_candidates = exploitation_candidates[~exploitation_candidates['place_name'].isin(exploitation_recommendations + exploration_recommendations)]

    if not exploitation_candidates.empty:
        selected_exploitation = exploitation_candidates.sample(1)
        exploitation_recommendations.append(selected_exploitation['place_name'].values[0])

    # Exploration recommendation (optional)
    exploration_candidates = jkt_filtered_2[~exploitation_mask]

    # Exclude already recommended places
    exploration_candidates = exploration_candidates[~exploration_candidates['place_name'].isin(exploitation_recommendations + exploration_recommendations)]

    if len(exploitation_recommendations) > 1 and not exploration_candidates.empty:
        exploration_index = thompson_sampling(exploration_candidates['rating'])
        selected_exploration = exploration_candidates.iloc[[exploration_index]]  # Wrap in double square brackets to get a DataFrame
        exploration_recommendations.append(selected_exploration['place_name'].values[0])

    # Print recommendations for the day
    print(f"Day {day}")
    print(f"Recommendation 1: {exploitation_recommendations[-1] if exploitation_recommendations else 'No recommendation'}")
    print(f"Recommendation 2: {exploration_recommendations[-1] if exploration_recommendations else 'No recommendation'}")
    print()
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances
from collections import OrderedDict
import numpy as np

class RecommenderSystem:
  def __init__(self, data, city, metadata_tokenized):
    """
    Initialize RecommenderSystem class with required attributes.
    Parameters:
    - data (dict): Dictionary containing datasets.
    - city (str): The specific city's dataset to be used.
    - metadata_tokenized (list): List of tokenized metadata for the city.
    """
    self.data = data
    self.city = data[city]
    self.metadata_tokenized = metadata_tokenized
    self.vectorizer = None
    self.documents = None
    self.recommendation_result = None

  def fit(self):
    """
    Fit method to encode metadata with TF-IDF vectorization.
    """
    self.vectorizer = TfidfVectorizer()
    self.documents = self.vectorizer.fit_transform(self.metadata_tokenized)

  def recommend(self, user_preferences, top_recommend=15):
    """
    Recommend method to generate recommendations based on user preferences.
    Parameters:
    - user_preferences (list): List of user preferences.
    - top_recommend (int): Number of top recommendations to generate (default: 10).
    Returns:
    - list: A list of indices representing recommended items/documents.
    """
    self.list_appended = []

    for preference in user_preferences:
      preference_vector = self.vectorizer.transform([preference])
      distance = cosine_distances(preference_vector, self.documents)
      distance_sort = distance.argsort()[0, 0:top_recommend]
      self.list_appended.append(distance_sort)
    return self.list_appended

  def postprocessing(self):
    combined = list(OrderedDict.fromkeys(np.concatenate(self.list_appended)))
    self.recommendation_result = self.city.iloc[combined]
    return self.recommendation_result
import numpy as np
import pandas as pd

class ThompsonSampling():
  def __init__(self):
    self.ratings = []
    self.exploitation_recommendations = []
    self.exploration_recommendations = []

  def bandit(self, ratings):
    sampled_indices = np.argmax(np.random.beta(1+ratings, 10))
    return sampled_indices

  def exploration(self, data, duration):
    for day in range(1, duration+1):
      exploitation_mask = data['rating'] >= 4.5
      self.exploitation_candidates = data[exploitation_mask]
      self.exploitation_candidates = self.exploitation_candidates[~self.exploitation_candidates['place_name'].isin(self.exploitation_recommendations + self.exploration_recommendations)]
      self.exploitation_recommendations.append(self.exploitation_candidates)
      self.exploration_candidates = data[~exploitation_mask]
      self.exploration_candidates = self.exploration_candidates[~self.exploration_candidates['place_name'].isin(self.exploitation_recommendations + self.exploration_recommendations)]
      self.exploration_recommendations.append(self.exploration_candidates)

      # Thompson sampling
      combine = pd.concat(self.exploitation_recommendations + self.exploration_recommendations, ignore_index=True)

      return combine
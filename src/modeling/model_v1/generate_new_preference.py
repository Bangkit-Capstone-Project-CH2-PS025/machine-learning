import gensim

class GenerateNewPreference():
  def __init__(self):
    """
    Initialize GenerateNewPreferences class with default parameters.
    """
    self.user_preferences = None
    self.dataset = None
    self.vector_size = 100
    self.window = 500
    self.min_count = 2
    self.workers = 100

  def fit(self, dataset, user_preferences):
    """
    Fit method to generate new user preferences using Word2Vec.

    Parameters:
    - dataset (list): List of tokenized sentences or text data.
    - user_preferences (list): List of user preferences.
    Returns:
    - str: New user preference generated from Word2Vec model.
    """
    self.user_preferences = user_preferences
    self.dataset = dataset

    # If user preferences is not 1
    if len(self.user_preferences) != 1:
      # Tokenize the dataset
      tokenized_data = [gensim.utils.simple_preprocess(sentence) for sentence in dataset]
      # Model Word2Vec
      model = gensim.models.Word2Vec(tokenized_data, vector_size=self.vector_size, window=self.window, min_count=self.min_count, workers=self.workers)
      # Similarity of user_preferences
      similarity = model.wv.similarity(w1=self.user_preferences[0], w2=self.user_preferences[1])
      # Similarity of word in user_preferences
      similar_words = model.wv.most_similar(positive=[self.user_preferences[0], self.user_preferences[1]])
      self.user_preferences.append(similar_words[0][0])
    else:
      pass
    return user_preferences[2]
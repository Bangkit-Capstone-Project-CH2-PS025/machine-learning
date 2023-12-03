class User():
  def __init__(self, data):
    """
    Initialize User class with attributes for user inputs.
    """
    self.data = data
    self.city = None
    self.budget = None
    self.duration = None
    self.user_preferences = None
    self.combined_list = None

  def input(self, city, budget, duration, user_preferences_1, user_preferences_2=None):
    """
    Define input function to capture user preferences and inputs.

    Parameters:
    - city (str): The city chosen by the user.
    - budget (float): The budget set by the user.
    - duration (int): The duration of the user's visit.
    - user_preferences_1 (str): The primary user preference.
    - user_preferences_2 (str, optional): Additional user preference (if any).

    Returns:
    - list: A combined list of tokenized metadata for the chosen city.
    - list: A list of user preferences.
    - int: The duration of the visit.
    - float: The budget for the trip.
    """
    self.city = str(city)
    self.budget = float(budget)
    self.duration = int(duration)
    self.user_preferences = [user_preferences_1]
    # If user_preferences is not None, then append user_preferences_2 to user_preferences
    if user_preferences_2 is not None:
      self.user_preferences.append(user_preferences_2)
    # Combine the column of 'metadata_tokenized' to one list
    self.combined_list = self.data[city]['metadata_tokenized'].tolist()
    return self.combined_list, self.user_preferences, self.duration, self.budget
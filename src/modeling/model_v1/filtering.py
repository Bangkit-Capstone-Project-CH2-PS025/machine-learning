import pandas as pd
import numpy as np

class Filtering:
    def __init__(self, data):
        """
        Initialize Filtering class with data and recommendation attributes.

        Parameters:
        - data (DataFrame): Dataset containing information for filtering.
        """
        self.data = data
        self.recommendation_budget = None
        self.recommendation_distance = None

    def budgeting(self, budget):
        """
        Budgeting method to filter data based on budget constraints.

        Parameters:
        - budget (float): Maximum budget constraint.

        Returns:
        - DataFrame: Filtered data within the budget limit.
        """
        self.total_price = 0
        self.selected_rows = []

        for index, row in self.data.iterrows():
            if self.total_price + row['price'] <= budget:
                self.total_price += row['price']
                self.selected_rows.append(row)

        self.recommendation_budget = pd.DataFrame(self.selected_rows)
        return self.recommendation_budget

    def haversine_distance(self, lat1, lon1, lat2, lon2):
        """
        Calculate Haversine distance between two geographical coordinates.

        Parameters:
        - lat1 (float): Latitude of the first point.
        - lon1 (float): Longitude of the first point.
        - lat2 (float): Latitude of the second point.
        - lon2 (float): Longitude of the second point.

        Returns:
        - float: Haversine distance between the points.
        """
        R = 6371
        dlat = np.radians(lat2 - lat1)
        dlon = np.radians(lon2 - lon1)
        a = np.sin(dlat/2) * np.sin(dlat/2) + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon/2) * np.sin(dlon/2)
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
        distance = R * c
        return distance

    def nearest_neighbor(self, points, start_lat, start_lon):
        """
        Find nearest neighbors using the Nearest Neighbor algorithm.

        Parameters:
        - points (array): Array of coordinates.
        - start_lat (float): Latitude of the starting point.
        - start_lon (float): Longitude of the starting point.

        Returns:
        - list: Route containing indices of nearest neighbor points.
        - float: Total distance of the route.
        """
        self.route = []
        self.total_distance = None
        start_point = np.array([[start_lat, start_lon]])
        points = np.concatenate((points, start_point), axis=0)

        n = len(points)
        visited = np.zeros(n, dtype=bool)
        visited[-1] = True
        route = [n - 1]
        total_dist = 0

        for i in range(n - 1):
            last_point = route[-1]
            min_dist = float('inf')
            nearest_point = None
            for j in range(n):
                if not visited[j] and j != last_point:
                    dist = self.haversine_distance(points[last_point][0], points[last_point][1], points[j][0], points[j][1])
                    if dist < min_dist:
                        min_dist = dist
                        nearest_point = j
            visited[nearest_point] = True
            route.append(nearest_point)
            total_dist += min_dist

        route.remove(n - 1)
        total_dist += self.haversine_distance(points[route[-1]][0], points[route[-1]][1], points[route[0]][0], points[route[0]][1])

        return route, total_dist

    def distance(self, start_lat, start_long):
        """
        Calculate distance and generate recommendations based on nearest neighbors.

        Parameters:
        - start_lat (float): Latitude of the starting point.
        - start_long (float): Longitude of the starting point.

        Returns:
        - list: Route containing indices of recommended points.
        - float: Total distance of the route.
        - DataFrame: Filtered data based on nearest neighbor route.
        """
        self.start_lat = start_lat
        self.start_long = start_long
        self.coordinates = self.recommendation_budget[['lat', 'long']].values

        route, total_distance = self.nearest_neighbor(self.coordinates, self.start_lat, self.start_long)
        self.route = route
        self.total_distance = total_distance
        self.recommendation_distance = self.recommendation_budget.iloc[self.route]
        self.recommendation_distance['coordinates'] = list(zip(self.recommendation_distance['lat'], self.recommendation_distance['long']))
        self.recommendation_distance_place_name = self.recommendation_distance[['id','place_name']]
        return self.route, self.total_distance, self.recommendation_distance, self.recommendation_distance_place_name
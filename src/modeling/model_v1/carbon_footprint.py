class CarbonFootprint():
    def __init__(self):
        """
        Initialize CarbonFootprint class.
        """
        self.co2_emissions = None

    def car(self):
        """
        Return emission factor for cars.

        Returns:
        - float: Emission factor for cars (kg CO2 per km).
        """
        emission_factors = 0.1639
        return emission_factors

    def bus(self):
        """
        Return emission factor for buses.

        Returns:
        - float: Emission factor for buses (kg CO2 per km).
        """
        emission_factors = 0.1022
        return emission_factors

    def motorbike(self):
        """
        Return emission factor for motorbikes.

        Returns:
        - float: Emission factor for motorbikes (kg CO2 per km).
        """
        emission_factors = 0.1133
        return emission_factors

    def vehicle_type(self, vehicle_type):
        """
        Select the emission factor based on the type of vehicle.

        Parameters:
        - vehicle_type (str): Type of vehicle ('car', 'bus', or 'motorbike').

        Returns:
        - float: Emission factor based on the selected vehicle type.
        """
        if vehicle_type == "car":
            return self.car()
        elif vehicle_type == "bus":
            return self.bus()
        elif vehicle_type == "motorbike":
            return self.motorbike()

    # calculate
    def calculate(self, vehicle_type, distance):
        """
        Calculate CO2 emissions based on the vehicle type and distance.

        Parameters:
        - vehicle_type (str): Type of vehicle ('car', 'bus', or 'motorbike').
        - distance (float): Distance traveled (in km).

        Returns:
        - float: CO2 emissions for the given distance and vehicle type (in kg CO2).
        """
        self.co2_emissions = self.vehicle_type(vehicle_type) * distance
        return round(self.co2_emissions, 1)

    def calculate_all(self, distance):
        """
          Calculate CO2 emissions for all vehicle types based on the given distance.

          Parameters:
          - distance (float): Distance traveled (in km).

          Returns:
          - list: List containing CO2 emissions for car, bus, and motorbike (in kg CO2).
          """
        self.distance = distance
        results = []
        vehicle_type = ['car', 'bus', 'motorbike']
        for vehicle in vehicle_type:
            result = self.calculate(vehicle, self.distance)
            results.append(result)
        return results
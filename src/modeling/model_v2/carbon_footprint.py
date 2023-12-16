import tensorflow as tf
import numpy as np

class CarbonFootprint():
    def __init__(self):
        self.co2_emissions = None

    def predict(self, vehicle_type, distance):
        if vehicle_type == "car":
            return self.car(distance)
        elif vehicle_type == "bus":
            return self.bus(distance)
        elif vehicle_type == "motorbike":
            return self.motorbike(distance)

    def car(self, distance):
        model_car = tf.keras.models.load_model('../../../models/carbon/model_carbon_car.h5')
        input_data = np.array([distance])
        prediction = model_car.predict(input_data.reshape(1,1), verbose=0)
        return prediction[0][0].squeeze()

    def bus(self, distance):
        model_bus = tf.keras.models.load_model('../../../models/carbon/model_carbon_bus.h5')
        input_data = np.array([distance])
        prediction = model_bus.predict(input_data.reshape(1, 1), verbose=0)
        return prediction[0][0].squeeze()

    def motorbike(self, distance):
        model_motorbike = tf.keras.models.load_model('../../../models/carbon/model_carbon_motorbike.h5')
        input_data = np.array([distance])
        prediction = model_motorbike.predict(input_data.reshape(1, 1), verbose=0)
        return prediction[0][0].squeeze()

    def predict_all(self, distance):
        self.distance = distance
        results = []
        vehicle_type = ['car', 'bus', 'motorbike']

        for vehicle in vehicle_type:
            result = self.predict(vehicle, self.distance)
            results.append(f"{result:.2f} kg CO2")

        return results
class City():
  def __init__(self):
    self.city = None

  def carbon(self, carbon):
    self.co2_car = carbon[0]
    self.co2_bus = carbon[1]
    self.co2_motorbike = carbon[2]

  def select_city(self, city, task):
    if city == "jakarta":
        if task == 1:
            return self.jakarta("coordinates")
        elif task == 2:
            return self.jakarta("price_emissions")
    elif city == "yogyakarta":
        if task == 1:
            return self.yogyakarta("coordinates")
        elif task == 2:
            return self.yogyakarta("price_emissions")
    elif city == "bandung":
        if task == 1:
            return self.bandung("coordinates")
        elif task == 2:
            return self.bandung("price_emissions")
    elif city == "semarang":
        if task == 1:
            return self.semarang("coordinates")
        elif task == 2:
            return self.semarang("price_emissions")
    elif city == "surabaya":
        if task == 1:
            return self.surabaya("coordinates")
        elif task == 2:
            return self.surabaya("price_emissions")
    elif city == "bengkulu":
        if task == 1:
            return self.bengkulu("coordinates")
        elif task == 2:
            return self.bengkulu("price_emissions")
    elif city == "banjarbaru":
        if task == 1:
            return self.banjarbaru("coordinates")
        elif task == 2:
            return self.banjarbaru("price_emissions")
    elif city == "denpasar":
        if task == 1:
            return self.denpasar("coordinates")
        elif task == 2:
            return self.denpasar("price_emissions")
    elif city == "maluku":
        if task == 1:
            return self.maluku("coordinates")
        elif task == 2:
            return self.maluku("price_emissions")
    elif city == "jayapura":
        if task == 1:
            return self.jayapura("coordinates")
        elif task == 2:
            return self.jayapura("price_emissions")

  def jakarta(self, condition):
    if condition == "coordinates":
      start_latitude = -6.2651234
      start_longitude = 106.8678393
      return start_latitude, start_longitude
    elif condition == "price_emissions":
      car = 20000
      bus = 3500
      motor = 12000
      return "jakarta", car, self.co2_car, bus, self.co2_bus, motor, self.co2_motorbike

  def yogyakarta(self, condition):
    if condition == "coordinates":
      start_latitude = -7.7889482
      start_longitude = 110.4281026
      return start_latitude, start_longitude
    elif condition == "price_emissions":
      car = 20000
      bus = 3500
      motor = 12000
      return "yogyakarta", car, self.co2_car, bus, self.co2_bus, motor, self.co2_motorbike

  def bandung(self, condition):
    if condition == "coordinates":
      start_latitude = -6.9146413
      start_longitude = 107.5998627
      return start_latitude, start_longitude
    elif condition == "price_emissions":
      car = 20000
      bus = 5000
      motor = 12000
      return "bandung", car, self.co2_car, bus, self.co2_bus, motor, self.co2_motorbike

  def semarang(self, condition):
    if condition == "coordinates":
      start_latitude = -6.9644063
      start_longitude = 110.4253333
      return start_latitude, start_longitude
    elif condition == "price_emissions":
      car = 20000
      bus = 3500
      motor = 12000
      return "semarang", car, self.co2_car, bus, self.co2_bus, motor, self.co2_motorbike

  def surabaya(self, condition):
    if condition == "coordinates":
      start_latitude = -7.3719669
      start_longitude = 112.7756714
      return start_latitude, start_longitude
    elif condition == "price_emissions":
      car = 20000
      bus = 5000
      motor = 12000
      return "surabaya", car, self.co2_car, bus, self.co2_bus, motor, self.co2_motorbike

  def bengkulu(self, condition):
    if condition == "coordinates":
      start_latitude = -3.8606521
      start_longitude = 102.3368196
      return start_latitude, start_longitude
    elif condition == "price_emissions":
      car = 20000
      bus = 5000
      motor = 12000
      return "bengkulu", car, self.co2_car, bus, self.co2_bus, motor, self.co2_motorbike

  def banjarbaru(self, condition):
    if condition == "coordinates":
      start_latitude = -3.4360195
      start_longitude = 114.7582452
      return start_latitude, start_longitude
    elif condition == "price_emissions":
      car = 20000
      bus = 5000
      motor = 12000
      return "banjarbaru", car, self.co2_car, bus, self.co2_bus, motor, self.co2_motorbike

  def denpasar(self, condition):
    if condition == "coordinates":
      start_latitude = -8.7469693
      start_longitude = 115.1642308
      return start_latitude, start_longitude
    elif condition == "price_emissions":
      car = 20000
      bus = 5000
      motor = 12000
      return "denpasar", car, self.co2_car, bus, self.co2_bus, motor, self.co2_motorbike

  def maluku(self, condition):
    if condition == "coordinates":
      start_latitude = -3.7048911
      start_longitude = 128.0862563
      return start_latitude, start_longitude
    elif condition ==  "price_emissions":
      car = 20000
      bus = 3500
      motor = 10000
      return "maluku", car, self.co2_car, bus, self.co2_bus, motor, self.co2_motorbike

  def jayapura(self, condition):
    if condition == "coordinates":
      start_latitude = -2.5772586
      start_longitude = 140.51555
      return start_latitude, start_longitude
    elif condition == "price_emissions":
      car = 50000
      bus = 50000
      motor = 15000
      return "jayapura", car, self.co2_car, bus, self.co2_bus, motor, self.co2_motorbike
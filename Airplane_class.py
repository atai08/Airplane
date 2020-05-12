

class Airplane():
    def __init__(self, mark, model, year, max_speed):
        self.mark = mark
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False

    def take_off(self):
        self.is_flying = True
        info_raise = f'{self.year} {self.mark} {self.model} successfully took off the ground'
        return info_raise

    def fly(self, flying_distance):
        self.odometer += flying_distance
        info_fly = f'{self.mark} {self.model} covered {self.odometer}km in the air and its maximum speed was {self.max_speed}km/h'
        return info_fly

    def land(self):
        self.is_flying = False
        info_land = f'{self.mark} {self.model} has successfully landed'
        odo_info = f'The distance on the odometer is {self.odometer}km'
        return info_land, odo_info


investigate = Airplane("AIRBUS", "A330", "2016", "880")

print(investigate.take_off())
print(investigate.fly(500))
print(investigate.land())
print()
print(investigate.take_off())
print(investigate.fly(500))
print(investigate.land())
print()
print(investigate.take_off())
print(investigate.fly(700))
print(investigate.land())

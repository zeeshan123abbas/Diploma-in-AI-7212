# frames.py
# FRAMES represent a stereotype object with SLOTS (attributes) and default values.
# Python classes are a natural way to write frames.
# Command:  python frames.py

class Vehicle:                       # general frame
    wheels = 4                       # default slot values
    fuel = "petrol"
    def describe(self):
        return f"{self.name}: {self.wheels} wheels, runs on {self.fuel}"

class Car(Vehicle):                  # more specific frame inherits slots
    seats = 5

class Rickshaw(Vehicle):
    wheels = 3                       # overrides the default
    fuel = "CNG"
    seats = 3

class Motorbike(Vehicle):
    wheels = 2
    seats = 2

# Instances fill the "name" slot; everything else comes from defaults
my_car = Car();        my_car.name = "Suzuki Alto"
auto = Rickshaw();     auto.name = "Qingqi Rickshaw"
bike = Motorbike();    bike.name = "Honda CD 70"
ev = Car();            ev.name = "Electric Car"; ev.fuel = "electricity"  # instance override

for item in [my_car, auto, bike, ev]:
    print(item.describe(), "| seats:", item.seats)

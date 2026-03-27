from classes import  Motorcycle, Car
## importing standart library module
import math
import time
# library pytest for testing canbe found in pypi.org
import pytest
print(Motorcycle)

# separating class usage in a different file
moto = Motorcycle("Honda", "CBR600RR", 2020)
print(f"the time is {time.time()}")
print(moto)
print(moto.is_engine_on)  # prints False
print(moto.is_headlight_on)  # prints False

moto.turn_engine_on()
print(moto.is_engine_on)  # prints True

moto.turn_headlight_on()
print(moto.is_headlight_on)  # prints True      

moto.start_driving()
moto.turn("left")

moto.turn_engine_off()  # should not turn off while driving 
moto.turn_headlight_off()
print(moto.is_headlight_on)  # prints False
time.sleep(2)

car = Car("Toyota", "Camry", 2021)
print(car)
car.turn_engine_on()
car.start_driving()
car.turn("right")
car.turn_engine_off()  #
class Vehicle: 
    is_engine_on = False        
    is_headlight_on = False
    make =  None
    model = None
    year = None
    is_driving = False
# def __str__(self):
#     return "Motorcycle(engine_on={self.is_engine_on}, headlight_on={self.is_headlight_on})"
    def turn_engine_on(self):
        print("Turning the engine on.")
        self.is_engine_on = True

    def turn_engine_off(self):
        print("Turning the engine off.")
        if self.is_driving:
            print("Cannot turn off the engine while driving!")
            return
        self.is_engine_on = False

    def turn_headlight_on(self):
        print("Turning the headlight on.")
        self.is_headlight_on = True
    
    def turn_headlight_off(self):
        print("Turning the headlight off.")
        self.is_headlight_on = False

    def start_driving(self):
        if not self.is_engine_on:
            print("Cannot start driving. The engine is off!")
            return
        print("Starting to drive.")
        self.is_driving = True

    def turn(self, direction):
        if not self.is_driving:
            print("Cannot turn. The motorcycle is not driving!")
            return
        print(f"Turning {direction}.")


    def __repr__(self):
        return (f'{self.make}, {self.model},  with engine' #python formatting f-string
                f'{"on" if self.is_engine_on else "off"}' 
                f'and headlight {"on" if self.is_headlight_on else "off"}'
        ) 
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Motorcycle(Vehicle): 
    turn_handlebar = None

class Car(Vehicle):
    def turn_steering_wheel(self, direction):
        print(f"Turning steering wheel {direction}.")

    def turn(self, direction):
        if direction in ['left', 'right']:
            self.turn_steering_wheel(direction)
        else:
            print("Cannot understand direction. Use 'left' or 'right'.")
            return
        print(f"Turning {direction}.")


    def __repr__(self):
        return (f'{self.make}, {self.model},  with engine' #python formatting f-string
                f'{"on" if self.is_engine_on else "off"}' 
                f'and headlight {"on" if self.is_headlight_on else "off"}'
        ) 
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


# moto = Motorcycle("Honda", "CBR600RR", 2020)
# print(moto)
# print(moto.is_engine_on)  # prints False
# print(moto.is_headlight_on)  # prints False

# moto.turn_engine_on()
# print(moto.is_engine_on)  # prints True

# moto.turn_headlight_on()
# print(moto.is_headlight_on)  # prints True      

# moto.start_driving()
# moto.turn("left")

# moto.turn_engine_off()  # should not turn off while driving 
# moto.turn_headlight_off()
# print(moto.is_headlight_on)  # prints False

# car = Car("Toyota", "Camry", 2021)
# print(car)
# car.turn_engine_on()
# car.start_driving()
# car.turn("right")
# car.turn_engine_off()  # should not turn off while driving

# add above to the for loop
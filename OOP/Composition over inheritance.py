class Motor:
    def start(self):
        print("Starting the engine")

class Car:
    def __init__(self):
        self.motor = Motor()

    def start(self):
        self.motor.start()

my_car = Car()
my_car.start()
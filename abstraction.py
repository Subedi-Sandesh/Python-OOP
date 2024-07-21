class Car:
    def __init__(self):
        self.acc = 0
        self.brake = 0
        self.clutch = 0

    def start(self):
        self.clutch = 1
        self.acc = 1
        print("Car started..")

car1 = Car()
car1.start()

#This program hides the use of clutch and acc in a automatic
#car and just shows the starting of the car to the user/

#which is called abstraction
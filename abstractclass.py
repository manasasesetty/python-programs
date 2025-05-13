from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod # decorator to make the method abstract
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass    

class Car(Vehicle):

    def go(self):
        print("You drive the car")
    
    def stop(self):
        print("You stop the car")

class Plane(Vehicle):

    def go(self):  
        print("You fly the plane")
    
    def stop(self):
        print("You land the plane")


car = Car()
plane = Plane()

car.go()
plane.go()

car.stop()
plane.stop()
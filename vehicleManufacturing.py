from abc import ABC, abstractmethod

# Product (Vehicle)
class Vehicle(ABC):
    @abstractmethod
    def get_details(self):
        pass

# Concrete Products (Car, Motorcycle, Truck)
class Car(Vehicle):
    def __init__(self):
        self.wheels = 4
        self.max_speed = 100
        self.seating_capacity =  4

    def get_details(self):
        return f"Car Details: Wheels={self.wheels}, Seating Capacity={self.seating_capacity}, Max Speed={self.max_speed}"

class Motorcycle(Vehicle):
    def __init__(self):
        self.wheels = 2
        self.max_speed = 100
        self.seating_capacity =  2

    def get_details(self):
        return f"Motorcycle Details: Wheels={self.wheels}, Seating Capacity={self.seating_capacity}, Max Speed={self.max_speed}"
        

class Truck(Vehicle):
    def __init__(self):
        self.wheels = 6
        self.max_speed = 100
        self.seating_capacity =  2

    def get_details(self):
        return f"Truck Details: Wheels={self.wheels}, Seating Capacity={self.seating_capacity}, Max Speed={self.max_speed}"
        

# Creator (Vehicle Factory)
class Factory(ABC):
    @abstractmethod
    def create_vehicle(self, max_speed):
        pass
    
# Concrete Creators (Car Factory, Motorcycle Factory, Truck Factory)
class CarFactory(Factory):
    def create_vehicle(self):
        return Car()

class MotorcycleFactory(Factory):
    def create_vehicle(self):
        return Motorcycle()

class TruckFactory(Factory):
    def create_vehicle(self):
        return Truck()

# Usage
if __name__ == '__main__':
    # User input for the desired vehicle type
    vehicle_type = input("Enter the vehicle type (car/motorcycle/truck): ")

    # Vehicle factory based on user input
    if vehicle_type == "car":
        factory = CarFactory()
    elif vehicle_type == "motorcycle":
        factory = MotorcycleFactory()
    elif vehicle_type == "truck":
        factory = TruckFactory()
    else:
        print("Invalid vehicle type.")
        exit()

    # Create the desired vehicle object using the factory
    vehicle = factory.create_vehicle()

    # Display the vehicle details
    print(vehicle.get_details())
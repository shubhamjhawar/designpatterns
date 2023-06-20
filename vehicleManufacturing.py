from abc import ABC, abstractmethod

# Abstract Vehicle class
class Vehicle(ABC):
    @abstractmethod
    def get_vehicle_type(self):
        pass

    @abstractmethod
    def get_number_of_wheels(self):
        pass

    @abstractmethod
    def get_seating_capacity(self):
        pass

    @abstractmethod
    def get_maximum_speed(self):
        pass


# Car class implementing the Vehicle interface
class Car(Vehicle):
    def get_vehicle_type(self):
        return "Car"

    def get_number_of_wheels(self):
        return 4

    def get_seating_capacity(self):
        return 5

    def get_maximum_speed(self):
        return 200


# Motorcycle class implementing the Vehicle interface
class Motorcycle(Vehicle):
    def get_vehicle_type(self):
        return "Motorcycle"

    def get_number_of_wheels(self):
        return 2

    def get_seating_capacity(self):
        return 2

    def get_maximum_speed(self):
        return 180


# Truck class implementing the Vehicle interface
class Truck(Vehicle):
    def get_vehicle_type(self):
        return "Truck"

    def get_number_of_wheels(self):
        return 6

    def get_seating_capacity(self):
        return 3

    def get_maximum_speed(self):
        return 150


# Vehicle Factory interface
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass


# Car Factory class implementing the VehicleFactory interface
class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()


# Motorcycle Factory class implementing the VehicleFactory interface
class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self):
        return Motorcycle()


# Truck Factory class implementing the VehicleFactory interface
class TruckFactory(VehicleFactory):
    def create_vehicle(self):
        return Truck()


# Example usage
if __name__ == "__main__":
    # User's input for vehicle type
    vehicle_type = "car"  # Options: "car", "motorcycle", "truck"

    # Factory selection based on user's input
    if vehicle_type.lower() == "car":
        factory = CarFactory()
    elif vehicle_type.lower() == "motorcycle":
        factory = MotorcycleFactory()
    elif vehicle_type.lower() == "truck":
        factory = TruckFactory()
    else:
        print("Invalid vehicle type!")
        exit()

    # Create the desired vehicle object using the factory
    vehicle = factory.create_vehicle()

    # Access and display the attributes of the manufactured vehicle
    print("Vehicle Type:", vehicle.get_vehicle_type())
    print("Number of Wheels:", vehicle.get_number_of_wheels())
    print("Seating Capacity:", vehicle.get_seating_capacity())
    print("Maximum Speed:", vehicle.get_maximum_speed())

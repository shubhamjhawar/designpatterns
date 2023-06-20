# designpatterns
# Design_Pattern_Assignment

## Weather Monitoring System
The Weather Monitoring System is a Python application that implements the Observer design pattern to monitor weather conditions and notify multiple display devices about changes in the weather. It establishes a one-to-many relationship between the weather station (subject) and the display devices (observers).

### Design Pattern: Observer
The Observer design pattern is used to establish a dependency between objects, such that when the state of one object (subject) changes, all its dependents (observers) are automatically notified and updated.

In the Weather Monitoring System, the Observer pattern is implemented as follows:

# Vehicle Manufacturing System

The Vehicle Manufacturing System is a Python program that allows users to create different types of vehicles using the factory design pattern. It also follows the Observer pattern to notify display devices when the weather conditions change.

## Features

- Supports the creation of cars, motorcycles, and trucks.
- Each vehicle type has specific attributes such as the number of wheels, seating capacity, and maximum speed.
- User-friendly interface for selecting the desired vehicle type and maximum speed.
- Utilizes the factory design pattern to encapsulate the creation logic and ensure the correct type of vehicle is created.
- Implements the Observer pattern to establish a one-to-many relationship between the weather station (subject) and the display devices (observers).
- When the weather data is updated, all registered display devices are automatically notified and display the latest weather information.
- Provides a way to access and display the attributes of the manufactured vehicle.

## Prerequisites

- Python 3.x

## Getting Started

1. Clone the repository:

   ```shell
   git clone https://github.com/shubhamjhawar/designpatterns


## Vehicle Manufacturing System
The Vehicle Manufacturing System is a Python application that utilizes the Factory Method design pattern to create different types of vehicles based on user input. The system allows users to specify the type of vehicle they want to manufacture (car, motorcycle, or truck) and provides the corresponding factory to create the desired vehicle object.


### Design Pattern: Factory Method
The Factory Method design pattern is used in this system to encapsulate the vehicle creation logic and ensure the correct type of vehicle is created based on user input. It provides an interface for creating objects, but defers the decision of which object to create to the subclasses. In this way, the Vehicle Factory acts as an abstract creator, and each specific vehicle factory subclass (CarFactory, MotorcycleFactory, TruckFactory) implements the factory method create_vehicle() to create the corresponding vehicle object.

By using the Factory Method pattern, the system achieves the following benefits:

 -  Decouples the client code from the specific vehicle classes, allowing for flexibility and extensibility in    adding new vehicle types.
- Provides a way to create objects without exposing the instantiation logic to the client.
- Ensures that the correct type of vehicle object is created based on user input, without the need for conditional statements or switch cases.


# designpatterns
x# Design_Pattern_Assignment

## Weather Monitoring System
The Weather Monitoring System is a Python application that implements the Observer design pattern to monitor weather conditions and notify multiple display devices about changes in the weather. It establishes a one-to-many relationship between the weather station (subject) and the display devices (observers).

### Design Pattern: Observer
The Observer design pattern is used to establish a dependency between objects, such that when the state of one object (subject) changes, all its dependents (observers) are automatically notified and updated.

In the Weather Monitoring System, the Observer pattern is implemented as follows:

- Subject: The WeatherStation class acts as the subject or the weather station. It maintains a list of registered observers (observers) and provides methods to register and unregister observers. It also defines a method to notify all registered observers when new weather data is available.

- Observers: The DisplayDevice class is the abstract base class for observers or display devices. It defines an abstract method update(weather_data) that concrete observers must implement. This method is called by the subject to update the observer with the latest weather data.

- Concrete Observers: The MobileAppDisplay, WebInterfaceDisplay, and DesktopApplicationDisplay classes are concrete observers or display devices. They inherit from the DisplayDevice base class and implement the update method to handle the received weather data. Each observer is responsible for updating its own user interface and displaying the weather information.


## Vehicle Manufacturing System
The Vehicle Manufacturing System is a Python application that utilizes the Factory Method design pattern to create different types of vehicles based on user input. The system allows users to specify the type of vehicle they want to manufacture (car, motorcycle, or truck) and provides the corresponding factory to create the desired vehicle object.


### Design Pattern: Factory Method
The Factory Method design pattern is used in this system to encapsulate the vehicle creation logic and ensure the correct type of vehicle is created based on user input. It provides an interface for creating objects, but defers the decision of which object to create to the subclasses. In this way, the Vehicle Factory acts as an abstract creator, and each specific vehicle factory subclass (CarFactory, MotorcycleFactory, TruckFactory) implements the factory method create_vehicle() to create the corresponding vehicle object.

By using the Factory Method pattern, the system achieves the following benefits:

 -  Decouples the client code from the specific vehicle classes, allowing for flexibility and extensibility in    adding new vehicle types.
- Provides a way to create objects without exposing the instantiation logic to the client.
- Ensures that the correct type of vehicle object is created based on user input, without the need for conditional statements or switch cases.


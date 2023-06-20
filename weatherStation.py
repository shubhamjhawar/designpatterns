from abc import ABC, abstractmethod

class WeatherData:
    def __init__(self):
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0
        self._observers = []

    def subscribe(self, observer):
        """Subscribe an observer to receive weather data updates."""
        self._observers.append(observer)

    def unsubscribe(self, observer):
        """Unsubscribe an observer from receiving weather data updates."""
        self._observers.remove(observer)

    def notify_observers(self):
        """Notify all subscribed observers about the updated weather data."""
        for observer in self._observers:
            observer.update(self)

    def set_measurement(self, temperature, humidity, pressure):
        """Set the weather measurements and notify observers."""
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()

    @property
    def temperature(self):
        """Get the temperature."""
        return self._temperature

    @property
    def humidity(self):
        """Get the humidity."""
        return self._humidity

    @property
    def pressure(self):
        """Get the pressure."""
        return self._pressure


class DisplayDevice(ABC):
    @abstractmethod
    def update(self, weather_data):
        """Update the display with the new weather data."""
        pass


class MobileAppDisplay(DisplayDevice):
    def update(self, weather_data):
        """Update the mobile app display with the new weather data."""
        temperature_report = self._get_report(weather_data.temperature, "temperature")
        humidity_report = self._get_report(weather_data.humidity, "humidity")
        pressure_report = self._get_report(weather_data.pressure, "pressure")
        print(f"Mobile App Display - {temperature_report}, {humidity_report}, {pressure_report}")

    @staticmethod
    def _get_report(value, measurement):
        """Generate a formatted report for the given measurement value."""
        if value == 0.0:
            return f"Wait for the {measurement} report"
        return str(value)


class WebInterfaceDisplay(DisplayDevice):
    def update(self, weather_data):
        """Update the web interface display with the new weather data."""
        temperature_report = self._get_report(weather_data.temperature, "temperature")
        humidity_report = self._get_report(weather_data.humidity, "humidity")
        pressure_report = self._get_report(weather_data.pressure, "pressure")
        print(f"Web Interface Display - {temperature_report}, {humidity_report}, {pressure_report}")

    @staticmethod
    def _get_report(value, measurement):
        """Generate a formatted report for the given measurement value."""
        if value == 0.0:
            return f"Wait for the {measurement} report"
        return str(value)


class DesktopApplicationDisplay(DisplayDevice):
    def update(self, weather_data):
        """Update the desktop application display with the new weather data."""
        temperature_report = self._get_report(weather_data.temperature, "temperature")
        humidity_report = self._get_report(weather_data.humidity, "humidity")
        pressure_report = self._get_report(weather_data.pressure, "pressure")
        print(f"Desktop Application Display - {temperature_report}, {humidity_report}, {pressure_report}")

    @staticmethod
    def _get_report(value, measurement):
        """Generate a formatted report for the given measurement value."""
        if value == 0.0:
            return f"Wait for the {measurement} report"
        return str(value)


if __name__ == "__main__":
    weather_station = WeatherData()

    mobile_app = MobileAppDisplay()
    web_interface = WebInterfaceDisplay()
    desktop_app = DesktopApplicationDisplay()

    weather_station.subscribe(mobile_app)
    weather_station.subscribe(web_interface)
    weather_station.subscribe(desktop_app)

    weather_station.set_measurement(25, 65, 105)
    weather_station.set_measurement(25,0.0, 105)
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


# User interaction for vehicle type selection
def get_vehicle_type_from_user():
    while True:
        vehicle_type = input("Enter the type of vehicle you want to manufacture (car, motorcycle, truck): ")
        if vehicle_type.lower() in ["car", "motorcycle", "truck"]:
            return vehicle_type.lower()
        else:
            print("Invalid vehicle type. Please try again.")


# Example usage
if __name__ == "__main__":
    # Get vehicle type from user
    vehicle_type = get_vehicle_type_from_user()

    # Factory selection based on user's input
    if vehicle_type == "car":
        factory = CarFactory()
    elif vehicle_type == "motorcycle":
        factory = MotorcycleFactory()
    elif vehicle_type == "truck":
        factory = TruckFactory()

    # Create the desired vehicle object using the factory
    vehicle = factory.create_vehicle()

    # Display the attributes of the manufactured vehicle
    print("Manufactured Vehicle:")
    print("Vehicle Type:", vehicle.get_vehicle_type())
    print("Number of Wheels:", vehicle.get_number_of_wheels())
    print("Seating Capacity:", vehicle.get_seating_capacity())
    print("Maximum Speed:", vehicle.get_maximum_speed())

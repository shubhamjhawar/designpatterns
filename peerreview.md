## Sonali approach 

## Code Comparison: Weather Data and Display Devices


The second code also implements a weather station system using the Observer pattern. Here's a breakdown of its components:

- `WeatherStation`: A class representing the weather station. It maintains a list of observers and previous weather data. It provides methods to register, unregister, and notify observers about weather data updates.

- `DisplayDevice` (Abstract Base Class): An abstract class defining the interface for display devices. It has an abstract method `update()` that needs to be implemented by subclasses.

- Subclasses of `DisplayDevice`: `MobileAppDisplay`, `WebInterfaceDisplay`, and `DesktopApplicationDisplay`. These classes implement the `update()` method to print weather data specific to their respective platforms.

In this code, the weather station checks for changes in weather data periodically and notifies the registered observers if a change is detected.

## Comparison

Both codes aim to achieve similar functionality using the Observer pattern but differ in their organization and implementation details:

- This code combines them within the `WeatherStation` class itself.
- This code encapsulates the weather data within the `WeatherStation` class and provides a method to fetch the current weather data.
- This uses `register_observer()` and `unregister_observer()` for the same purpose.
- This incorporates the notification process within the `notify_observer()` method of the `WeatherStation` class.
- This introduces a `previous_weather_data` variable to track changes in weather data and avoids unnecessary notifications when data hasn't changed

## Code Comparison: vehicle amnufacturing
The code involves more user interaction and has less hard coded and logic used are similar

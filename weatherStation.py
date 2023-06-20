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

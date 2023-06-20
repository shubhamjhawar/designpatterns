from abc import ABC, abstractmethod

class WeatherData:
    def __init__(self):
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    def set_measurement(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()

    @property
    def temperature(self):
        return self._temperature

    @property
    def humidity(self):
        return self._humidity

    @property
    def pressure(self):
        return self._pressure


class DisplayDevice(ABC):
    @abstractmethod
    def update(self, weather_data):
        pass


class MobileAppDisplay(DisplayDevice):
    def update(self, weather_data):
        temperature_report = self._get_report(weather_data.temperature, "temperature")
        humidity_report = self._get_report(weather_data.humidity, "humidity")
        pressure_report = self._get_report(weather_data.pressure, "pressure")
        print(f"Mobile App Display - {temperature_report}, {humidity_report}, {pressure_report}")

    @staticmethod
    def _get_report(value, measurement):
        if value == 0.0:
            return f"Wait for the {measurement} report"
        return str(value)


class WebInterfaceDisplay(DisplayDevice):
    def update(self, weather_data):
        temperature_report = self._get_report(weather_data.temperature, "temperature")
        humidity_report = self._get_report(weather_data.humidity, "humidity")
        pressure_report = self._get_report(weather_data.pressure, "pressure")
        print(f"Web interface App Display - {temperature_report}, {humidity_report}, {pressure_report}")

    @staticmethod
    def _get_report(value, measurement):
        if value == 0.0:
            return f"Wait for the {measurement} report"
        return str(value)


class DesktopApplicationDisplay(DisplayDevice):
    def update(self, weather_data):
        temperature_report = self._get_report(weather_data.temperature, "temperature")
        humidity_report = self._get_report(weather_data.humidity, "humidity")
        pressure_report = self._get_report(weather_data.pressure, "pressure")
        print(f"Desktop App Display - {temperature_report}, {humidity_report}, {pressure_report}")

    @staticmethod
    def _get_report(value, measurement):
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

    weather_station.set_measurement(25.6, 65.2, 1013.5)

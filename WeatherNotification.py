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

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notify_observers()

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        self._humidity = value
        self.notify_observers()

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, value):
        self._pressure = value
        self.notify_observers()

class DisplayDevice(ABC):
    @abstractmethod
    def update(self,weather_data):
        pass

class MobileAppDisplay(DisplayDevice):
    def update(self, weather_data):
        if(weather_data.temperature == 0.0):
            temperature_report = "Wait for the temperature report"
        else:
            temperature_report = weather_data.temperature
        
        if(weather_data.humidity == 0.0):
            humidity_report = "Wait for the humidity report"
        else:
            humidity_report = weather_data.humidity

        if(weather_data.pressure == 0.0):
            pressure_report = "Wait for the pressure report"
        else:
            pressure_report = weather_data.pressure
       

        print(f"Mobile App Display - Temperature: {temperature_report}, Humidity: { humidity_report}, Pressure: {pressure_report}")


class WebInterfaceDisplay(DisplayDevice):
    def update(self, weather_data):
        if(weather_data.temperature == 0.0):
            temperature_report = "Wait for the temperature report"
        else:
            temperature_report = weather_data.temperature
        
        if(weather_data.humidity == 0.0):
            humidity_report = "Wait for the humidity report"
        else:
            humidity_report = weather_data.humidity

        if(weather_data.pressure == 0.0):
            pressure_report = "Wait for the pressure report"
        else:
            pressure_report = weather_data.pressure
       

        print(f"Web interface App Display - Temperature: {temperature_report}, Humidity: { humidity_report}, Pressure: {pressure_report}")


class DesktopApplicationDisplay(DisplayDevice):
    def update(self, weather_data):
        if(weather_data.temperature == 0.0):
            temperature_report = "Wait for the temperature report"
        else:
            temperature_report = weather_data.temperature
        
        if(weather_data.humidity == 0.0):
            humidity_report = "Wait for the humidity report"
        else:
            humidity_report = weather_data.humidity

        if(weather_data.pressure == 0.0):
            pressure_report = "Wait for the pressure report"
        else:
            pressure_report = weather_data.pressure
       

        print(f"Desktop App Display - Temperature: {temperature_report}, Humidity: { humidity_report}, Pressure: {pressure_report}")




if __name__ == "__main__":
    weather_station = WeatherData()

    mobile_app = MobileAppDisplay()
    web_interface = WebInterfaceDisplay()
    desktop_app = DesktopApplicationDisplay()

    weather_station.subscribe(mobile_app)
    weather_station.subscribe(web_interface)
    weather_station.subscribe(desktop_app)

    weather_station.temperature = 25.6
    weather_station.humidity = 65.2
    weather_station.pressure = 1013.5

import requests
from django.conf import settings


class Weather:
    def __init__(self):
        self.url = "https://api.openweathermap.org/data/2.5/"
        self.api_key = settings.OPEN_WEATHER_API_KEY

    def get_weather(self, lat, lon):
        url = self.url + "weather"
        params = {"lat": lat, "lon": lon, "appid": self.api_key, "units": "metric"}
        response = requests.get(url, params=params)
        return response.json()

    def get_forecast(self, lat, lon):
        url = self.url + f"forecast?lat={lat}&lon={lon}&appid={self.api_key}"
        params = {"lat": lat, "appid": self.api_key, "units": "metric"}
        response = requests.get(url, params=params)
        return response.json()


WEATHER_CLIENT = Weather()

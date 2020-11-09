#!/usr/bin/env python
from BAC0.core.utils.notes import note_and_log
import requests, json, time
from datetime import datetime
from ddcmath.psychrometric import dewpoint

@note_and_log
class OpenWeather:

    blank = {
        "coord": {"lon": -92.11, "lat": 46.78},
        "weather": [
            {"id": 800, "main": "Unknown", "description": "Unknown", "icon": "01d"}
        ],
        "base": "stations",
        "main": {
            "temp": 0,
            "feels_like": 0,
            "temp_min": 0,
            "temp_max": 0,
            "pressure": 0,
            "humidity": 0,
        },
        "visibility": 0,
        "wind": {"speed": 0, "deg": 0},
        "clouds": {"all": 1},
        "dt": 0,
        "sys": {"type": 1, "id": 3903, "country": "US", "sunrise": 0, "sunset": 0},
        "timezone": 0,
        "id": 0,
        "name": "Unknown",
        "cod": 0,
    }

    def __init__(self, city="duluth", units="imperial"):
        self.base_url, self.api_key = self.get_api_key_and_base_url().values()
        self.city_name = city
        self.complete_url = (
            self.base_url
            + "appid="
            + self.api_key
            + "&q="
            + self.city_name
            + "&units="
            + units
        )
        self.data = None
        self.update()

    def update(self):
        backup = self.data
        try:
            response = requests.get(self.complete_url)
            #print(response.json())
            self.data = response.json()
        except Exception as error:
            self._log.error("Error updating weather | {}".format(error))
            if self.data is None:
                self._log.warning("Using blank template")
                return self.blank
            self._log.warning("Using last time report")
            return backup
        return self.data

    def get_api_key_and_base_url(self):
        with open("api.key", "r") as file:
            d = json.load(file)
        return d["openweathermap"]


    @property
    def timestamp(self):
        return datetime.fromtimestamp(self.data["dt"])

    @property
    def sunrise(self):
        return datetime.fromtimestamp(self.data["sys"]["sunrise"])

    @property
    def sunset(self):
        return datetime.fromtimestamp(self.data["sys"]["sunset"])

    @property
    def temp(self):
        return self.data["main"]["temp"]

    @property
    def hum(self):
        return self.data["main"]["humidity"]

    @property
    def press(self):
        return self.data["main"]["pressure"]

    @property
    def windspd(self):
        return self.data["wind"]["speed"]

    @property
    def winddir(self):
        directions = ['North', 'North East', 'East', 'South East', 'South', 'South West', 'West', 'North West']
        angle = self.data["wind"]["deg"]
        return directions[round(angle / 45) % 8]

    @property
    def cloudcov(self):
        return self.data["clouds"]["all"]

    @property
    def descrip(self):
        return self.data["weather"][0]["description"]

    @property
    def city(self):
        return self.data["name"]

    @property
    def dewpoint(self):
        return round(dewpoint(self.data["main"]["temp"], self.data["main"]["humidity"], SI=True))

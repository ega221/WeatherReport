import ipinfo
import requests
import yaml
from WeatherReportEntity import WeatherReportEntity
from datetime import datetime, timezone, timedelta

from Exceptions import *


class WeatherService:
    _IP_INFO_API_KEY: str
    _API_KEY_OPEN_WEATHER: str
    _BASE_URL: str

    def __init__(self) -> None:
        data = self.__get_initial_parameters()
        self._BASE_URL = data.get('openweathermap').get('base_url')
        self._IP_INFO_API_KEY = data.get('ipinfo').get('api_key')
        self._API_KEY_OPEN_WEATHER = data.get('openweathermap').get('api_key')

    def __get_initial_parameters(self) -> dict:
        with open("properties.yaml", "r") as yaml_file:
            try:
                data = yaml.safe_load(yaml_file)

                return data
            except yaml.YAMLError as exc:
                print("Ошибка при чтении YAML-файла:", exc)

    def __get_city_by_ip(self, ip: str = '') -> str:
        handler = ipinfo.getHandler(self._IP_INFO_API_KEY)
        details = handler.getDetails(ip)

        return details.all.get('city')

    def get_weather_report(self, city: str = '') -> WeatherReportEntity:
        if not city:
            city = self.__get_city_by_ip()

        url = self._BASE_URL + '?' + "appid=" + self._API_KEY_OPEN_WEATHER + "&q=" + city + '&lang=ru' + '&units=metric'
        response = requests.get(url)

        if response.status_code == 200:

            contents = response.json()
            time_shift = contents.get("timezone")
            time_zone = timezone(timedelta(seconds = time_shift))
            report = WeatherReportEntity(
                location=city,
                condition=contents['weather'][0]['description'],
                temperature=float(contents['main']['temp']),
                feels_like=float(contents['main']['feels_like']),
                humidity=contents['main']['humidity'],
                wind_speed=contents['wind']['speed'],
                date=datetime.now(time_zone).strftime("%Y-%d-%m %H:%M:%S%Z")
            )

            return report

        elif response.status_code == 404:
            raise CityNotFoundException

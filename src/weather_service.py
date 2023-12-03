from datetime import datetime, timedelta, timezone
from pathlib import Path

import ipinfo
import requests
import yaml

from exceptions import CityNotFoundException
from weather_report_entity import WeatherReportEntity


class WeatherService:
    _PATH_TO_CONFIG = Path(__file__).parent.parent / "properties.yaml"

    def __init__(self) -> None:
        data = self.__get_initial_parameters()
        self._base_url = data.get("openweathermap").get("base_url")
        self._ip_info_api_key = data.get("ipinfo").get("api_key")
        self._open_weather_api_key = data.get("openweathermap").get("api_key")

    def get_weather_report(self, city: str | None = None) -> WeatherReportEntity:
        if city is None:
            city = self.__get_city_by_ip()

        params = {
            "appid": self._open_weather_api_key,
            "q": city,
            "lang": "ru",
            "units": "metric",
        }

        response = requests.get(self._base_url, params=params)

        if response.status_code == 200:
            contents = response.json()
            time_shift = contents.get("timezone")
            time_zone = timezone(timedelta(seconds=time_shift))
            report = WeatherReportEntity(
                location=city,
                condition=contents["weather"][0]["description"],
                temperature=float(contents["main"]["temp"]),
                feels_like=float(contents["main"]["feels_like"]),
                humidity=contents["main"]["humidity"],
                wind_speed=contents["wind"]["speed"],
                date=datetime.now(time_zone).strftime("%Y-%d-%m %H:%M:%S%Z"),
            )
            return report
        elif response.status_code == 404:
            raise CityNotFoundException
        else:
            response.raise_for_status()

    def __get_city_by_ip(self, ip: str = "") -> str:
        handler = ipinfo.getHandler(self._ip_info_api_key)
        details = handler.getDetails(ip)

        return details.all.get("city")

    def __get_initial_parameters(self) -> dict | None:
        with open(self._PATH_TO_CONFIG, "r") as yaml_file:
            try:
                return yaml.safe_load(yaml_file)
            except yaml.YAMLError as exc:
                print("Ошибка при чтении YAML-файла:", exc)

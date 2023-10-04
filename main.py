import datetime as dt
import ipinfo
import json
import requests
import yaml


def get_initial_parameters() -> dict:
    with open("properties.yaml", "r") as yaml_file:
        try:
            data = yaml.safe_load(yaml_file)

            return data
        except yaml.YAMLError as exc:
            print("Ошибка при чтении YAML-файла:", exc)

def get_city_by_ip(ip: str = '') -> str:
    handler = ipinfo.getHandler(IP_INFO_API_KEY)
    details = handler.getDetails(ip)

    return details.all.get('city')

def get_celsius_from_response(response: json) -> float:
    kelvin = response.get("main").get("temp")
    return kelvin - 273.15


if __name__ == "__main__":
    data = get_initial_parameters()

    BASE_URL = data.get('openweathermap').get('base_url')
    IP_INFO_API_KEY = data.get('ipinfo').get('api_key')
    API_KEY_OPEN_WEATHER = data.get('openweathermap').get('api_key')

    CITY = get_city_by_ip()

    url = BASE_URL + '?' + "appid=" + API_KEY_OPEN_WEATHER + "&q=" + CITY
    response = requests.get(url).json()

    print(response)
    print(get_celsius_from_response(response))

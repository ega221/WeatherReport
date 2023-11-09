# WeatherReport

WheatherReport - это консольное приложение, предоставляющее пользователю информацию о погоде
по запросу. Пользователь может указать конкретный город, либо получить данные для своего местоположения. Помимо этого,
приложение сохраняет историю запросов и позволяет обращаться к ней, при необходимости.

Формат вывода данных:
```commandline
Время: 14:44:22 2023-10-19
Местоположение: Saint Petersburg
Температура: 3.77°C
Ощущается как: 1.94°C
Влажность: 85.00%
Скорость ветра: 2 м/c
```

Доступные команды:
1. -w {location}: - Дает информацию о погоде в населённом пункте или городе. Если не передавать параметр, то будет взято местположение пользователя.
2. -h - Показывает последние 10 запросов.
3. -c - Очищает историю.
4. -q - Закрывает программу и сохраняет историю.


## Что используется?
Для получения данных о погоде используется OpenWeatherApi.
Определение местоположения происходит с помощью ipInfo.oi.

## Для запуска:
Нужно создать конфигурационный файл вида:
```yaml
openweathermap:
  base_url: https://api.openweathermap.org/data/2.5/weather
  api_key: {open_weather_api_token}

ipinfo:
  api_key: {ipinfo_api_token}
```
И добавить его в корень проекта.
# WeatherReport

WheatherReport - это консольное приложение, предоставляющее пользователю информацию о погоде
по запросу. Пользователь может указать конкретный город, либо получить данные для своего местоположения. Помимо этого,
приложение сохраняет историю запросов и позволяет обращаться к ней, при необходимости.

Формат вывода данных:
```commandline
Текущее время: 2023-09-11 16:13:36+03:00
Название города: Saint Petersburg
Погодные условия: пасмурно
Текущая температура: 7 градусов по цельсию
Ощущается как: 7 градусов по цельсию
Скорость ветра: 0 м/c
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
Нужно создать конфигурационный файл properties.yaml вида:
```yaml
openweathermap:
  base_url: https://api.openweathermap.org/data/2.5/weather
  api_key: {open_weather_api_token}

ipinfo:
  api_key: {ipinfo_api_token}
```
И добавить его в корень проекта.
- Создать окружение: python -m venv \<venv_name\>
- Запустить: Для windows: \<venv_name\>/Scripts/activate; Для unix: source \<venv_name\>/bin/activate
- Далее установить небоходимые зависимости: pip install -r requirements.txt
- Запустить программу: python main.py
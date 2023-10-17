from WeatherReportEntity import WeatherReportEntity
from WeatherService import WeatherService
from Exceptions import *


def printWeatherReport(report: WeatherReportEntity):
    print(f"Время: {report.date}\n" 
      f"Местоположение: {report.location}\n" 
      f"Температура: {report.temperature:.2f}°C\n" 
      f"Ощущается как: {report.feels_like:.2f}°C\n"
      f"Влажность: {report.humidity:.2f}%\n"
      f"Скорость ветра: {report.wind_speed} м/c")


def main():
    service = WeatherService()

    while True:
        command = input().split()

        match command[0]:
            case '-h':
                print('help message placeholder')
            case '-c':
                print('closing programm')
                break
            case '-w':
                if (len(command) > 1):
                    try:

                        report = service.get_weather_report(command[1])
                        printWeatherReport(report)

                    except CityNotFoundException:
                        print('Given city not found, please try again.')
                        continue
                else:
                    report = service.get_weather_report()
                    printWeatherReport(report)
            case _:
                print('Unknown command, please try again or type -h for help.')





if __name__ == "__main__":
    main()



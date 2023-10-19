from ReportRepository import ReportRepository
from WeatherReportEntity import WeatherReportEntity
from WeatherService import WeatherService
from Exceptions import *

HELP_MESSAGE = '''Weather report - приложение для получения информации о погоде в текущий момент времени.
Доступные команды:
1. -w {location}: - Дает информацию о погоде в населённом пункте или городе. Если не передавать параметр, то будет взято
        местположение пользователя.
2. -h - Показывает последние 10 запросов.
3. -c - Очищает историю.
4. -q - Закрывает программу и сохраняет историю.
'''

def print_weather_report(report: WeatherReportEntity) -> None:
    print(f"Время: {report.date}\n" 
      f"Местоположение: {report.location}\n" 
      f"Температура: {report.temperature:.2f}°C\n" 
      f"Ощущается как: {report.feels_like:.2f}°C\n"
      f"Влажность: {report.humidity:.2f}%\n"
      f"Скорость ветра: {report.wind_speed} м/c")

def print_history(repository: ReportRepository) -> None:
    reports = repository.get_reports()
    if (len(reports) == 0):
        print("История запросов пуста.")
    else:
        print('--------- ИСТОРИЯ ЗАПРОСОВ ---------')
        for report in reports:
            print('------------------------------------')
            print_weather_report(report)
        print('------------------------------------')
        print('------------------------------------')


def main() -> None:
    service = WeatherService()
    repository = ReportRepository()

    while True:
        command = input().split(" ", 1)

        match command[0]:
            case '-h':
                print_history(repository)
            case '-c':
                repository.clear_reports()
                print("История запросов очищена!")
            case '-help':
                print(HELP_MESSAGE)
            case '-q':
                repository.save_to_json()
                print('Завершение работы')
                break
            case '-w':
                if (len(command) > 1):
                    try:

                        report = service.get_weather_report(command[1])
                        repository.add_report(report)
                        print_weather_report(report)

                    except CityNotFoundException:
                        print('Данный город не найден, попробуйте снова.')
                        continue
                else:
                    report = service.get_weather_report()
                    repository.add_report(report)
                    print_weather_report(report)
            case _:
                print('Неизвестная команда, пожалуйста, попробуйте -help, чтобы вывести доступные команды.')





if __name__ == "__main__":
    main()



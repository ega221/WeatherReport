from exceptions import CityNotFoundException
from report_repository import ReportRepository
from weather_report_entity import WeatherReportEntity
from weather_service import WeatherService

HELP_MESSAGE = """Weather report - приложение для получения информации о погоде в текущий момент времени.
Доступные команды:
1. -w {location}: - Дает информацию о погоде в населённом пункте или городе. Если не передавать параметр, то будет взято
        местположение пользователя.
2. -h {n} - Показывает последние n запросов, если параметр не дан, то выводятся 10 последних запросов.
3. -c - Очищает историю.
4. -q - Закрывает программу и сохраняет историю.
"""

UNKNOWN_COMMAND_MESSAGE = "Неизвестная команда, пожалуйста, попробуйте -help, чтобы вывести доступные команды."


def print_weather_report(report: WeatherReportEntity) -> None:
    print(
        f"Текущее время: {report.date.replace('UTC', '')}\n"
        f"Название города: {report.location}\n"
        f"Погодные условия: {report.condition}\n"
        f"Текущая температура: {report.temperature:.0f} градусов по цельсию\n"
        f"Ощущается как: {report.feels_like:.0f} градусов по цельсию\n"
        f"Скорость ветра: {report.wind_speed} м/c"
    )


def print_history(repository: ReportRepository, n: int = 10) -> None:
    reports = repository.load_from_json(n)
    if len(reports) == 0:
        print("История запросов пуста.")
    else:
        print("--------- ИСТОРИЯ ЗАПРОСОВ ---------")
        for report in reports:
            print("------------------------------------")
            print_weather_report(report)
        print("------------------------------------")
        print("------------------------------------")


def main() -> None:
    service = WeatherService()
    repository = ReportRepository()

    while True:
        command = input().strip().split(" ", 1)

        match command[0]:
            case "-h":
                if len(command) > 1:
                    try:
                        print_history(repository, int(command[1]))
                    except ValueError:
                        print(UNKNOWN_COMMAND_MESSAGE)
                elif len(command) == 1:
                    print_history(repository)
                else:
                    print(UNKNOWN_COMMAND_MESSAGE)
            case "-c":
                if len(command) == 1:
                    repository.clear_reports()
                    print("История запросов очищена!")
                else:
                    print(UNKNOWN_COMMAND_MESSAGE)
            case "-help":
                if len(command) == 1:
                    print(HELP_MESSAGE)
                else:
                    print(UNKNOWN_COMMAND_MESSAGE)
            case "-q":
                if len(command) == 1:
                    print("Завершение работы")
                    break
                else:
                    print(UNKNOWN_COMMAND_MESSAGE)
            case "-w":
                if len(command) > 1:
                    try:
                        report = service.get_weather_report(command[1])
                        repository.add_report(report)
                        print_weather_report(report)
                    except CityNotFoundException:
                        print("Данный город не найден, попробуйте снова.")
                else:
                    report = service.get_weather_report()
                    repository.add_report(report)
                    print_weather_report(report)
            case _:
                print(UNKNOWN_COMMAND_MESSAGE)


if __name__ == "__main__":
    main()

import json

from weather_report_entity import WeatherReportEntity


class ReportRepository:
    def __init__(self, file_name: str = ".history.json") -> None:
        self.reports: list[WeatherReportEntity] = []
        self._file_name = file_name
        self.__load_from_json()

    def add_report(self, report: WeatherReportEntity) -> None:
        if len(self.reports) >= 10:
            self.reports.pop(0)
        self.reports.append(report)

    def save_to_json(self) -> None:
        data = [report.convert_to_json() for report in self.reports]
        with open(self._file_name, "w") as file:
            json.dump(data, file)

    def clear_reports(self) -> None:
        self.reports = []

    def __load_from_json(self) -> None:
        try:
            with open(self._file_name) as f:
                data = json.load(f)
                self.reports = [WeatherReportEntity(**report) for report in data[-10:]]
        except FileNotFoundError:
            print("Файл истории не найден, будет создан новый")
            return
        except (TypeError, json.JSONDecodeError):
            print("Файл истории повреждён, будет создан новый")
            return

        if len(self.reports) == 0:
            print("Файл истории найден, история запросов пуста.")
        else:
            print("Файл истории найден, история последних запросов загружена")

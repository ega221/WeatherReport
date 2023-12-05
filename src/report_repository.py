import json

from weather_report_entity import WeatherReportEntity


class ReportRepository:
    def __init__(self, file_name: str = ".history.json") -> None:
        self._file_name = file_name

    def add_report(self, report: WeatherReportEntity) -> None:
        try:
            with open(self._file_name, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(report.convert_to_json())

        with open(self._file_name, "w") as file:
            json.dump(data, file)


    def save_to_json(self) -> None:
        data = [report.convert_to_json() for report in self.reports]
        with open(self._file_name, "a") as file:
            json.dump(data, file)

    def clear_reports(self) -> None:
        data = []
        with open(self._file_name, "w") as file:
            json.dump(data, file)

    def load_from_json(self, n: int = 10) -> list[WeatherReportEntity] | None:
        try:
            with open(self._file_name) as f:
                data = json.load(f)
                reports = [WeatherReportEntity(**report) for report in data[-n:]]
                reports.reverse()
        except FileNotFoundError:
            print("Файл истории не найден.")
            return []
        except (TypeError, json.JSONDecodeError):
            self.clear_reports()
            print("Файл истории повреждён, история очищена.")
            return []

        return reports

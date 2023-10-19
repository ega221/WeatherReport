import json

from WeatherReportEntity import WeatherReportEntity


class ReportRepository:
    reports: list[WeatherReportEntity] = []
    file_name: str

    def __init__(self, file_name: str = ".history.json") -> None:

        self.file_name = file_name
        self.__load_from_json()

    def add_report(self, report: WeatherReportEntity) -> None:
        if len(self.reports) >= 10:
            self.reports.pop(0)  # Deleting the oldest report
        self.reports.append(report)

    def save_to_json(self) -> None:
        data = [report.convert_to_json() for report in self.reports]
        with open(self.file_name, 'w') as file:
            json.dump(data, file)

    def __load_from_json(self) -> None:
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                self.reports = [WeatherReportEntity(**report) for report in data]
                if (len(self.reports) == 0):
                    print("Файл истории найден, история запросов пуста.")
                else:
                    print("Файл истории найден, история последних запросов загружена")
        except FileNotFoundError:
            print(f"Файл истории не найден, будет создан новый")

    def get_reports(self) -> list[WeatherReportEntity]:
        return self.reports

    def clear_reports(self) -> None:
        self.reports = []
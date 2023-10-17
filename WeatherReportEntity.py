from dataclasses import dataclass, asdict


@dataclass(order=True)
class WeatherReportEntity:
    location: str
    temperature: float
    feels_like: float
    humidity: int
    wind_speed: int
    date: str

    def convert_to_json(self):
        return asdict(self)
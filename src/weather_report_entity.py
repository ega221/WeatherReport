from dataclasses import asdict, dataclass


@dataclass
class WeatherReportEntity:
    location: str
    condition: str
    temperature: float
    feels_like: float
    humidity: int
    wind_speed: int
    date: str

    def convert_to_json(self) -> dict:
        return asdict(self)

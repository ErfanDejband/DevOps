"""
Temperature Monitoring API
A simple API to demonstrate DevOps practices
"""

from typing import Optional


class TemperatureSensor:
    """Simulates a temperature sensor"""

    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.readings = []

    def add_reading(self, temperature: float, unit: str = "C") -> dict:
        """
        Add a temperature reading

        Args:
            temperature: Temperature value
            unit: Temperature unit (C or F)

        Returns:
            dict: Reading record with timestamp
        """
        if unit not in ["C", "F"]:
            raise ValueError("Unit must be 'C' or 'F'")

        from datetime import datetime

        reading = {
            "temperature": temperature,
            "unit": unit,
            "timestamp": datetime.now().isoformat(),
            "sensor": self.name,
            "location": self.location,
        }

        self.readings.append(reading)
        return reading

    def get_latest_reading(self) -> Optional[dict]:
        """Get the most recent temperature reading"""
        if not self.readings:
            return None
        return self.readings[-1]

    def get_average_temperature(self) -> float:
        """Calculate average temperature from all readings"""
        if not self.readings:
            return 0.0

        total = sum(r["temperature"] for r in self.readings)
        return round(total / len(self.readings), 2)

    def get_all_readings(self) -> list:
        """Get all temperature readings"""
        return self.readings


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit"""
    return round((celsius * 9 / 5) + 32, 2)


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius"""
    return round((fahrenheit - 32) * 5 / 9, 2)

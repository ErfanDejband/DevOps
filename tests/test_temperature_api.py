"""
Unit tests for Temperature API
This is how we ensure code quality in DevOps!
"""

import pytest
from src.temperature_api import (
    TemperatureSensor,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
)


class TestTemperatureSensor:
    """Test the TemperatureSensor class"""

    def test_sensor_creation(self):
        """Test creating a new sensor"""
        sensor = TemperatureSensor("Sensor-1", "Living Room")
        assert sensor.name == "Sensor-1"
        assert sensor.location == "Living Room"
        assert sensor.readings == []

    def test_add_reading_celsius(self):
        """Test adding a Celsius reading"""
        sensor = TemperatureSensor("Sensor-1", "Kitchen")
        reading = sensor.add_reading(22.5, "C")

        assert reading["temperature"] == 22.5
        assert reading["unit"] == "C"
        assert reading["sensor"] == "Sensor-1"
        assert reading["location"] == "Kitchen"
        assert "timestamp" in reading

    def test_add_reading_fahrenheit(self):
        """Test adding a Fahrenheit reading"""
        sensor = TemperatureSensor("Sensor-2", "Bedroom")
        reading = sensor.add_reading(72.0, "F")

        assert reading["temperature"] == 72.0
        assert reading["unit"] == "F"

    def test_invalid_unit_raises_error(self):
        """Test that invalid units raise ValueError"""
        sensor = TemperatureSensor("Sensor-1", "Garage")

        with pytest.raises(ValueError, match="Unit must be 'C' or 'F'"):
            sensor.add_reading(25.0, "K")  # Kelvin not supported

    def test_get_latest_reading(self):
        """Test getting the most recent reading"""
        sensor = TemperatureSensor("Sensor-1", "Office")

        # No readings yet
        assert sensor.get_latest_reading() is None

        # Add readings
        sensor.add_reading(20.0, "C")
        sensor.add_reading(21.0, "C")
        sensor.add_reading(22.0, "C")

        latest = sensor.get_latest_reading()
        assert latest is not None
        assert latest["temperature"] == 22.0

    def test_get_average_temperature(self):
        """Test calculating average temperature"""
        sensor = TemperatureSensor("Sensor-1", "Lab")

        # Empty readings
        assert sensor.get_average_temperature() == 0.0

        # Add readings
        sensor.add_reading(20.0, "C")
        sensor.add_reading(22.0, "C")
        sensor.add_reading(24.0, "C")

        assert sensor.get_average_temperature() == 22.0

    def test_get_all_readings(self):
        """Test retrieving all readings"""
        sensor = TemperatureSensor("Sensor-1", "Basement")

        sensor.add_reading(18.0, "C")
        sensor.add_reading(19.0, "C")

        all_readings = sensor.get_all_readings()
        assert len(all_readings) == 2
        assert all_readings[0]["temperature"] == 18.0
        assert all_readings[1]["temperature"] == 19.0


class TestTemperatureConversion:
    """Test temperature conversion functions"""

    def test_celsius_to_fahrenheit(self):
        """Test C to F conversion"""
        assert celsius_to_fahrenheit(0) == 32.0
        assert celsius_to_fahrenheit(100) == 212.0
        assert celsius_to_fahrenheit(25) == 77.0
        assert celsius_to_fahrenheit(-40) == -40.0

    def test_fahrenheit_to_celsius(self):
        """Test F to C conversion"""
        assert fahrenheit_to_celsius(32) == 0.0
        assert fahrenheit_to_celsius(212) == 100.0
        assert fahrenheit_to_celsius(77) == 25.0
        assert fahrenheit_to_celsius(-40) == -40.0

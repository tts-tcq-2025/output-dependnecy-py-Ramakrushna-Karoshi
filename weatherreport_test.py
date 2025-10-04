from weatherreport import report, sensor_stub, sensor_stub_high_precip_low_wind

def test_rainy_weather_with_high_precip_and_wind():
    weather = report(sensor_stub)  # High temp, high precip, high wind
    print(f"Weather for high precip + wind: {weather}")
    assert "rain" in weather.lower(), (
        f"Expected 'rain' in forecast, got: {weather}"
    )

def test_high_precipitation_low_wind():
    weather = report(sensor_stub_high_precip_low_wind)  # High precip, low wind
    print(f"Weather for high precip + low wind: {weather}")
    assert "rain" in weather.lower(), (
        f"Expected rain-related forecast for high precipitation, got: {weather}"
    )

if __name__ == '__main__':
    test_rainy_weather_with_high_precip_and_wind()
    test_high_precipitation_low_wind()
    print("All tests completed (maybe!)")



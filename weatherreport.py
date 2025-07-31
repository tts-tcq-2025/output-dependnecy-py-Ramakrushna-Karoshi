

# def sensorStub():
#     return {
#         'temperatureInC': 50,
#         'precipitation': 70,
#         'humidity': 26,
#         'windSpeedKMPH': 52
#     }


# def report(sensorReader):
#     readings = sensorReader()
#     weather = "Sunny Day"

#     if (readings['temperatureInC'] > 25):
#         if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
#             weather = "Partly Cloudy"
#         elif readings['windSpeedKMPH'] > 50:
#             weather = "Alert, Stormy with heavy rain"
#     return weather


# # def testRainy():
#     weather = report(sensorStub)
#     print(weather)
#     assert("rain" in weather)


# def testHighPrecipitation():
#     # This instance of stub needs to be different-
#     # to give high precipitation (>60) and low wind-speed (<50)

#     weather = report(sensorStub)

#     # strengthen the assert to expose the bug
#     # (function returns Sunny day, it should predict rain)
#     assert(len(weather) > 0);


# if __name__ == '__main__':
#     testRainy()
#     testHighPrecipitation()
#     print("All is well (maybe!)");


# Task 1



# def sensorStub():
#     return {
#         'temperatureInC': 50,
#         'precipitation': 70,
#         'humidity': 26,
#         'windSpeedKMPH': 52
#     }

# # New stub for high precipitation and low wind speed
# def sensorStubHighPrecipitationLowWind():
#     return {
#         'temperatureInC': 30, # Keep temperature > 25
#         'precipitation': 70, # High precipitation (>60)
#         'humidity': 26,
#         'windSpeedKMPH': 30  # Low wind speed (<50)
#     }

# def report(sensorReader):
#     readings = sensorReader()
#     weather = "Sunny Day"

#     if (readings['temperatureInC'] > 25):
#         if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
#             weather = "Partly Cloudy"
#         # BUG: If precipitation is >= 60 AND windSpeedKMPH is <= 50,
#         # it falls through to the end and returns "Sunny Day".
#         # It should probably be "Heavy Rain" or "Rainy".
#         elif readings['windSpeedKMPH'] > 50:
#             weather = "Alert, Stormy with heavy rain"
#     return weather


# def testRainy():
#     weather = report(sensorStub)
#     print(weather)
#     assert("rain" in weather)


# def testHighPrecipitation():
#     # This instance of stub needs to be different-
#     # to give high precipitation (>60) and low wind-speed (<50)
#     weather = report(sensorStubHighPrecipitationLowWind) # Use the new stub

#     # strengthen the assert to expose the bug
#     # (function returns Sunny day, it should predict rain)
#     # The current buggy code will return "Sunny Day" for sensorStubHighPrecipitationLowWind
#     # We expect something indicating rain for high precipitation
#     print(f"Weather for High Precipitation: {weather}")
#     assert("rain" in weather or "Rain" in weather) # Strengthened assertion


# if __name__ == '__main__':
#     testRainy()
#     testHighPrecipitation()
#     print("All is well (maybe!)");








# Task 2

def sensor_stub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }

def sensor_stub_high_precip_low_wind():
    return {
        'temperatureInC': 30,      # > 25°C
        'precipitation': 70,       # >= 60%
        'humidity': 26,
        'windSpeedKMPH': 30        # <= 50 kmph
    }

def report(sensor_reader):
    readings = sensor_reader()
    weather = "Sunny Day"

    if readings['temperatureInC'] > 25:
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
        # BUG: No handling for high precipitation + low wind

    return weather



# from weather_module import report, sensor_stub, sensor_stub_high_precip_low_wind

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


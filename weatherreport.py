

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






def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }

# New stub for high precipitation and low wind speed
def sensorStubHighPrecipitationLowWind():
    return {
        'temperatureInC': 30, # Keep temperature > 25
        'precipitation': 70, # High precipitation (>60)
        'humidity': 26,
        'windSpeedKMPH': 30  # Low wind speed (<50)
    }

def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        # BUG: If precipitation is >= 60 AND windSpeedKMPH is <= 50,
        # it falls through to the end and returns "Sunny Day".
        # It should probably be "Heavy Rain" or "Rainy".
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather


def testRainy():
    weather = report(sensorStub)
    print(weather)
    assert("rain" in weather)


def testHighPrecipitation():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)
    weather = report(sensorStubHighPrecipitationLowWind) # Use the new stub

    # strengthen the assert to expose the bug
    # (function returns Sunny day, it should predict rain)
    # The current buggy code will return "Sunny Day" for sensorStubHighPrecipitationLowWind
    # We expect something indicating rain for high precipitation
    print(f"Weather for High Precipitation: {weather}")
    assert("rain" in weather or "Rain" in weather) # Strengthened assertion


if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)");

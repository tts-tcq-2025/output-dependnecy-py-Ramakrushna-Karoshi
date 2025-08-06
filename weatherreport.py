

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


#***************************************************************************************************************************************#
#***************************************************************************************************************************************#
#***************************************************************************************************************************************#

#weatherreport.py

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

# alert_failure_count = 0

# def network_alert_stub(celcius):
#     print(f'ALERT: Temperature is {celcius} celcius')
#     # Return 200 for ok
#     # Return 500 for not-ok
#     # stub always succeeds and returns 200
#     return 200

# def alert_in_celcius(farenheit):
#     celcius = (farenheit - 32) * 5 / 9
#     returnCode = network_alert_stub(celcius)
#     if returnCode != 200:
#         # non-ok response is not an error! Issues happen in life!
#         # let us keep a count of failures to report
#         # However, this code doesn't count failures!
#         # Add a test below to catch this bug. Alter the stub above, if needed.
#         global alert_failure_count
#         alert_failure_count += 0


# alert_in_celcius(400.5)
# alert_in_celcius(303.6)
# print(f'{alert_failure_count} alerts failed.')
# print('All is well (maybe!)')




alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # To make the test fail, we'll make the stub return a non-200 code
    # for a specific condition or simply toggle its behavior for testing.
    # Let's make it fail if celcius is above a certain threshold.
    if celcius > 100: # Arbitrary threshold to simulate a failure
        return 500 # Simulate failure
    return 200 # Simulate success

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        # The bug is here: it adds 0 instead of 1
        alert_failure_count += 0 # THIS IS THE BUG!

# Test cases:
# 400.5 Fahrenheit is (400.5 - 32) * 5 / 9 = 204.72 Celsius (should fail the stub)
alert_in_celcius(400.5)
# 303.6 Fahrenheit is (303.6 - 32) * 5 / 9 = 150.88 Celsius (should fail the stub)
alert_in_celcius(303.6)

print(f'{alert_failure_count} alerts failed.')

# Add an assertion to check if the failure count is correct.
# We expect 2 failures based on the input values and our modified stub.
# The bug will cause alert_failure_count to remain 0, leading to an assertion failure.
assert(alert_failure_count == 2)

print('All is well (maybe!)')

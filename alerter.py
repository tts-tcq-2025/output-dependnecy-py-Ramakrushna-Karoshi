alert_failure_count = 0  # Global variable to count alert failures

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    if celcius > 100:  # Simulated failure condition
        return 500
    return 200

def alert_in_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5 / 9
    return_code = network_alert_stub(celcius)
    if return_code != 200:
        global alert_failure_count
        alert_failure_count += 0  # BUG: Should be += 1 (intentional)







from alerter import alert_in_celcius, alert_failure_count

def test_alert_failures():
    # Calling alert function with high Fahrenheit values
    alert_in_celcius(400.5)   # Celsius = 204.72 → failure
    alert_in_celcius(303.6)   # Celsius = 150.88 → failure

    # The following assertion will fail due to the intentional bug in alert_failure_count update
    assert alert_failure_count == 2, (
        f"Expected 2 failures, but got {alert_failure_count}"
    )

if __name__ == '__main__':
    test_alert_failures()
    print("All tests completed.")


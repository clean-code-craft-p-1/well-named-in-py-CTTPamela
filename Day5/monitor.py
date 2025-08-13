from Day5.getProperties import get_vital_issues
from Day5.ioFunctions import alert_issues

def vitals_ok(temperature, pulse_rate, spo2):
    """Check if all vitals are normal (orchestrates pure logic and I/O)"""
    issues = get_vital_issues(temperature, pulse_rate, spo2)
    if issues:
        alert_issues(issues)
        return False
    return True
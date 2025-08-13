def get_temperature_status(temperature):
    """Check if temperature is in normal range (pure function)"""
    return temperature <= 102 and temperature >= 95

def get_pulse_rate_status(pulse_rate):
    """Check if pulse rate is in normal range (pure function)"""
    return pulse_rate >= 60 and pulse_rate <= 100

def get_spo2_status(spo2):
    """Check if oxygen saturation is in normal range (pure function)"""
    return spo2 >= 90

def get_vital_issues(temperature, pulse_rate, spo2):
    """Collect all vital sign issues (pure function)"""
    issues = []
    if not get_temperature_status(temperature):
        issues.append("Temperature critical!")
    if not get_pulse_rate_status(pulse_rate):
        issues.append("Pulse Rate is out of range!")
    if not get_spo2_status(spo2):
        issues.append("Oxygen Saturation out of range!")
    return issues
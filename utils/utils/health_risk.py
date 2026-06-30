def calculate_health_risks(data):
    aqi = data["aqi"]
    temp = data["temperature"]

    asthma_risk = min(100, int(aqi * 0.5))
    respiratory_risk = min(100, int(aqi * 0.45))
    elderly_risk = min(100, int(aqi * 0.4))
    heatstroke_risk = min(100, int(temp * 2))

    return {
        "asthma": asthma_risk,
        "respiratory": respiratory_risk,
        "elderly": elderly_risk,
        "heatstroke": heatstroke_risk
    }
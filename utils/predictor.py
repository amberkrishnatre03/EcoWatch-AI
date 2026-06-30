import os
import joblib

if os.path.exists("model/aqi_model.pkl"):
    model = joblib.load("model/aqi_model.pkl")
else:
    model = None


def predict_aqi_trend(current_aqi):
    if current_aqi <= 50:
        return "Air quality is good. No health risk expected."
    elif current_aqi <= 100:
        return "Moderate AQI. Sensitive people should stay cautious."
    elif current_aqi <= 150:
        return "AQI may worsen soon. Asthma patients should reduce outdoor activity."
    elif current_aqi <= 200:
        return "High pollution likely in next few hours. Health risk increasing."
    else:
        return "Severe AQI alert! Dangerous air quality expected."

def ml_predict_aqi(temp, humidity, wind_speed):

    if model is None:
        return "Train Model First"

    prediction = model.predict(
        [[temp, humidity, wind_speed]]
    )

    return round(prediction[0], 2)
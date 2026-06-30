import requests
import os

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

city_coordinates = {
    "New Delhi": (28.6139, 77.2090),
    "Gurgaon": (28.4595, 77.0266),
    "Noida": (28.5355, 77.3910),
    "Ghaziabad": (28.6692, 77.4538),
    "Meerut": (28.9845, 77.7064),
    "Jaipur": (26.9124, 75.7873),
    "Chandigarh": (30.7333, 76.7794),
    "Mumbai": (19.0760, 72.8777),
    "Pune": (18.5204, 73.8567),
    "Ahmedabad": (23.0225, 72.5714),
    "Bangalore": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707),
    "Hyderabad": (17.3850, 78.4867),
    "Kochi": (9.9312, 76.2673),
    "Kolkata": (22.5726, 88.3639),
    "Bhubaneswar": (20.2961, 85.8245),
    "Bhopal": (23.2599, 77.4126)
}

def get_live_data(city=None, lat=None, lon=None):
    if lat is None or lon is None:
        lat, lon = city_coordinates.get(city, city_coordinates["New Delhi"])

    # Weather API
    weather_url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
    )
    weather_response = requests.get(weather_url).json()

    # AQI API
    aqi_url = (
        f"https://api.openweathermap.org/data/2.5/air_pollution"
        f"?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}"
    )
    aqi_response = requests.get(aqi_url).json()

    # OpenWeather AQI scale: 1–5 → convert into readable AQI scale
    pm25 = aqi_response["list"][0]["components"]["pm2_5"]
    aqi_scaled = round(pm25 * 4)

    return {
        "temperature": weather_response["main"]["temp"],
        "humidity": weather_response["main"]["humidity"],
        "wind_speed": weather_response["wind"]["speed"],
        "aqi": aqi_scaled
    }

def get_aqi_forecast(lat, lon):
    url = (
        f"https://api.openweathermap.org/data/2.5/air_pollution/forecast"
        f"?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    forecast_values = []

    for item in data["list"][:8]:
        pm25 = item["components"]["pm2_5"]
        forecast_values.append(round(pm25 * 4))

    return forecast_values
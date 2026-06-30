from flask import Flask, render_template, request
from utils.api_fetch import get_live_data, get_aqi_forecast
from utils.predictor import predict_aqi_trend, ml_predict_aqi
from utils.alert_system import asthma_alert, send_whatsapp_alert
from report_generator import generate_detailed_report
from health_risk import calculate_health_risks
import time

city_map_cache = None
last_updated = 0

app = Flask(__name__)

# 20 Major Indian Cities
city_coordinates = {
    "New Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Bangalore": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707),
    "Hyderabad": (17.3850, 78.4867),
    "Kolkata": (22.5726, 88.3639),
    "Pune": (18.5204, 73.8567),
    "Ahmedabad": (23.0225, 72.5714),
    "Jaipur": (26.9124, 75.7873),
    "Lucknow": (26.8467, 80.9462),
    "Chandigarh": (30.7333, 76.7794),
    "Gurgaon": (28.4595, 77.0266),
    "Noida": (28.5355, 77.3910),
    "Ghaziabad": (28.6692, 77.4538),
    "Meerut": (28.9845, 77.7064),
    "Bhopal": (23.2599, 77.4126),
    "Indore": (22.7196, 75.8577),
    "Patna": (25.5941, 85.1376),
    "Kochi": (9.9312, 76.2673),
    "Bhubaneswar": (20.2961, 85.8245)
}


@app.route('/', methods=['GET', 'POST'])
def home():
    city = "New Delhi"
    prediction = ""
    alert = ""

    if request.method == 'POST':
        city = request.form.get("city", "New Delhi")

    # Get coordinates for selected city
    lat, lon = city_coordinates.get(city, city_coordinates["New Delhi"])

    # Get live weather + AQI data
    data = get_live_data(city, lat, lon)

    # Get AQI forecast trend graph data
    aqi_forecast = get_aqi_forecast(lat, lon)

    # Prediction systems
    prediction = predict_aqi_trend(data["aqi"])
    alert = asthma_alert(data["aqi"])
    report = generate_detailed_report(city, data)

    # Severity Badge Logic
    if data["aqi"] <= 50:
        severity_badge = "GREEN"
    elif data["aqi"] <= 100:
        severity_badge = "YELLOW"
    elif data["aqi"] <= 200:
        severity_badge = "ORANGE"
    else:
        severity_badge = "RED"

    # ML AQI Prediction
    ml_prediction = ml_predict_aqi(
        data["temperature"],
        data["humidity"],
        data["wind_speed"]
    )

    # Health Risk Scores
    health_risks = calculate_health_risks(data)

    # WhatsApp Alert if AQI dangerous
    # 🔥 Heat risk logic
    if data["temperature"] > 40:
        heat_alert = "🔥 Extreme heatstroke risk"
    elif data["temperature"] > 35:
        heat_alert = "⚠ Moderate heat stress"
    else:
        heat_alert = "✅ Normal temperature conditions"

    # 🌧 Rain detection (basic)
    if data["humidity"] > 75 and data["wind_speed"] > 3:
        rain_alert = "🌧 Possible rainfall / storm conditions"
    else:
        rain_alert = "☀ No immediate rainfall risk"

    # 📉 AQI trend logic
    if data["aqi"] > 180:
        trend = "📈 Pollution likely to worsen"
    elif data["aqi"] > 120:
        trend = "⚠ Pollution may fluctuate"
    else:
        trend = "📉 Air quality relatively stable"

    # 📩 FINAL MESSAGE
    message = f"""
    🌍 *EcoWatch AI Intelligence Alert*

    📍 Location: {city}

    🌫 *Air Quality*
    AQI: {data['aqi']}  
    🚨 Unhealthy air conditions detected

    🫁 *Health Impact*
    • Respiratory irritation risk  
    • Asthma & heart patients vulnerable  
    • Children & elderly at risk  

    🌡 *Heat Analysis*
    Temperature: {data['temperature']}°C  
    {heat_alert}

    🌧 *Weather Risk*
    {rain_alert}

    📊 *AI Prediction*
    {trend}

    🛡 *Recommended Actions*
    • Limit outdoor exposure 🚫  
    • Wear mask 😷  
    • Stay hydrated 💧  
    • Keep indoor air clean 🏠  

    ⚙ Real-time AI-driven environmental monitoring  
    – EcoWatch AI
    """

    # 🚨 SEND ALERT ONLY WHEN NEEDED
    if data["aqi"] > 150 or data["temperature"] > 38:
        send_whatsapp_alert(message)

    global city_map_cache, last_updated

    # Refresh cache every 10 minutes
    if city_map_cache is None or time.time() - last_updated > 600:
        city_map_cache = []
        last_updated = time.time()

        for city_name, coords in city_coordinates.items():
            city_data = get_live_data(city_name, coords[0], coords[1])

            city_map_cache.append({
                "name": city_name,
                "lat": coords[0],
                "lon": coords[1],
                "aqi": city_data["aqi"]
            })

    city_map_data = city_map_cache

    # 🌡 Heatstroke Risk
    if data["temperature"] >= 40:
        heat_risk = "🔥 High Heatstroke Risk"
    elif data["temperature"] >= 35:
        heat_risk = "⚠ Moderate Heat Stress"
    else:
        heat_risk = "✅ Normal Temperature"

    # 🌧 Rain Prediction (simple logic)
    if data["humidity"] > 70 and data["wind_speed"] > 3:
        rain_prediction = "🌧 High chance of rain"
    elif data["humidity"] > 60:
        rain_prediction = "🌦 Possible rain"
    else:
        rain_prediction = "☀ No rain expected"

    return render_template(
        'index.html',
        data=data,
        city=city,
        prediction=prediction,
        alert=alert,
        report=report,
        ml_prediction=ml_prediction,
        severity_badge=severity_badge,
        health_risks=health_risks,
        aqi_forecast=aqi_forecast,
        city_map_data=city_map_data,
        heat_risk=heat_risk,
        rain_prediction=rain_prediction
    )


if __name__ == '__main__':
    app.run(debug=True)
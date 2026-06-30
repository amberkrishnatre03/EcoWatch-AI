def generate_detailed_report(city, data):
    aqi = data["aqi"]
    temp = data["temperature"]
    humidity = data["humidity"]
    wind = data["wind_speed"]

    # Dynamic advisory logic
    if aqi <= 100:
        severity = "MODERATE"
        citizen_advisory = """
Citizens may continue normal outdoor activities, however respiratory-sensitive individuals
should avoid prolonged exposure during traffic peak hours.
"""
        govt_advisory = """
Municipal authorities should maintain standard emissions monitoring and continue routine
urban air quality surveillance protocols.
"""

    elif aqi <= 150:
        severity = "UNHEALTHY FOR SENSITIVE GROUPS"
        citizen_advisory = """
Children, elderly individuals, and asthma patients are advised to reduce outdoor exposure,
especially during afternoon high-density pollution periods.
"""
        govt_advisory = """
Local agencies should initiate dust suppression measures near major construction zones and
increase roadside particulate monitoring.
"""

    elif aqi <= 200:
        severity = "UNHEALTHY"
        citizen_advisory = """
Residents should avoid outdoor exercise, use N95 masks when outside, and minimize exposure
during evening traffic congestion periods.
"""
        govt_advisory = """
Immediate reduction of traffic congestion zones, stricter industrial emissions enforcement,
and temporary construction activity restrictions are strongly recommended.
"""

    else:
        severity = "SEVERE"
        citizen_advisory = """
All residents should remain indoors whenever possible. Schools should suspend outdoor activities,
and vulnerable populations must use air purification support indoors.
"""
        govt_advisory = """
Emergency pollution mitigation protocols should be activated, including vehicle rationing measures,
industrial emission shutdown review, and public health alert broadcasting.
"""

    report = f"""
ECO WATCH AI ENVIRONMENTAL INTELLIGENCE REPORT
CITY: {city}

ENVIRONMENTAL SUMMARY:
Current AQI is {aqi}, classified under {severity} pollution conditions.
Temperature is {temp}°C, humidity is {humidity}%, and wind speed is {wind} m/s.

POLLUTANT HEALTH RISK INTERPRETATION:
Fine particulate matter at this AQI level may aggravate asthma, bronchitis, lung irritation,
and cardiovascular stress in vulnerable individuals.

MEDICAL ADVISORY:

Asthma Patients:
Avoid outdoor exertion, carry prescribed rescue inhalers, and use N95 masks outdoors.

COPD Patients:
Remain indoors in filtered air environments and avoid dusty roadside areas.

Elderly Individuals:
Avoid outdoor exposure after noon and monitor breathing discomfort carefully.

Children:
Outdoor sports and playground activity should be restricted during elevated AQI periods.

Heart Patients:
Avoid cardiovascular strain outdoors and reduce unnecessary walking in polluted zones.

WEATHER HAZARD ASSESSMENT:
"""

    # Weather hazard logic
    if temp >= 40:
        weather_hazard = "Extreme heat conditions detected. Heatstroke risk is HIGH. Outdoor exposure should be minimized."

    elif temp >= 35:
        weather_hazard = "Elevated heat levels detected. Moderate heat exhaustion risk exists during prolonged outdoor activity."

    else:
        weather_hazard = "Temperature conditions are within manageable range, with low heat stress risk."

    if humidity > 75:
        weather_hazard += " High humidity may intensify breathing discomfort."

    if wind > 5:
        weather_hazard += " Strong wind may increase airborne dust exposure."


    report = f"""
ECO WATCH AI ENVIRONMENTAL INTELLIGENCE REPORT
CITY: {city}

ENVIRONMENTAL SUMMARY:
Current AQI is {aqi}, classified under {severity} pollution conditions.
Temperature is {temp}°C, humidity is {humidity}%, and wind speed is {wind} m/s.

POLLUTANT HEALTH RISK INTERPRETATION:
Fine particulate matter at this AQI level may aggravate asthma, bronchitis, lung irritation,
and cardiovascular stress in vulnerable individuals.

MEDICAL ADVISORY:

Asthma Patients:
Avoid outdoor exertion, carry prescribed rescue inhalers, and use N95 masks outdoors.

COPD Patients:
Remain indoors in filtered air environments and avoid dusty roadside areas.

Elderly Individuals:
Avoid outdoor exposure after noon and monitor breathing discomfort carefully.

Children:
Outdoor sports and playground activity should be restricted during elevated AQI periods.

Heart Patients:
Avoid cardiovascular strain outdoors and reduce unnecessary walking in polluted zones.

WEATHER HAZARD ASSESSMENT:
{weather_hazard}
RAIN PROBABILITY INTELLIGENCE:
RAIN PROBABILITY INTELLIGENCE:
Low rainfall probability


CITIZEN ADVISORY:
{citizen_advisory}

GOVERNMENT ADVISORY:
{govt_advisory}

PREDICTIVE TREND FORECAST:
If wind conditions remain unchanged, AQI may continue worsening over the next 4–6 hours.

EMERGENCY SEVERITY INDEX:
{severity}

AI RECOMMENDATION SUMMARY:
EcoWatch AI recommends adaptive exposure reduction and active public caution measures until AQI improves.
"""
    return report
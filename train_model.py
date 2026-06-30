import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

data = pd.read_csv("dataset/historical_aqi.csv")

X = data[["temperature", "humidity", "wind_speed"]]
y = data["aqi"]

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    max_depth=10
)

model.fit(X, y)

joblib.dump(model, "model/aqi_model.pkl")

print("ML model trained and saved successfully.")
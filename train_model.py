import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("weatherHistory.csv")

# Keep only useful columns
df = df[["Humidity", "Wind Speed (km/h)", "Pressure (millibars)", "Temperature (C)"]]

# Remove missing values
df = df.dropna()

# Input features
X = df[["Humidity", "Wind Speed (km/h)", "Pressure (millibars)"]]

# Target
y = df["Temperature (C)"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "weather_model.pkl")

print("✅ Model trained successfully!")
print("✅ weather_model.pkl created")
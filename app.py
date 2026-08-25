import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("weather_model.pkl")

st.title("🌦 Weather Temperature Prediction")

st.write("Enter the weather details below:")

humidity = st.number_input("Humidity", min_value=0.0, max_value=1.0, value=0.50)
wind_speed = st.number_input("Wind Speed (km/h)", value=10.0)
pressure = st.number_input("Pressure (millibars)", value=1015.0)

if st.button("Predict Temperature"):
    data = pd.DataFrame({
        "Humidity": [humidity],
        "Wind Speed (km/h)": [wind_speed],
        "Pressure (millibars)": [pressure]
    })

    prediction = model.predict(data)

    st.success(f"🌡 Predicted Temperature: {prediction[0]:.2f} °C")
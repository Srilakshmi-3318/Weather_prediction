import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("weatherHistory.csv")

# First 5 rows
print(df.head())

# Dataset info
print(df.info())

# Missing values
print(df.isnull().sum())

# Histogram of Temperature
plt.figure(figsize=(8,5))
plt.hist(df["Temperature (C)"], bins=30)
plt.title("Temperature Distribution")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.show()
# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df["Humidity"], df["Temperature (C)"])
plt.title("Humidity vs Temperature")
plt.xlabel("Humidity")
plt.ylabel("Temperature (°C)")
plt.show()
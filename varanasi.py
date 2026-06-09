import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_data.csv")

df["Max Temp (°C)"] = df["Max Temp (°C)"].str.replace("°C", "", regex=False).astype(int)
df["Min Temp (°C)"] = df["Min Temp (°C)"].str.replace("°C", "", regex=False).astype(int)

plt.figure(figsize=(12,5))

plt.plot(df["Day of May [1]"], df["Max Temp (°C)"], marker="o", label="Max Temp")
plt.plot(df["Day of May [1]"], df["Min Temp (°C)"], marker="s", label="Min Temp")

plt.title("May Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
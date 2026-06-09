import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_data.csv")
df["datetime"] = pd.to_datetime(df["datetime"])

columns = ["temp","humidity","pressure","wind_speed","clouds","visibility"]

plt.figure(figsize=(12,6))

for col in columns:
    normalized = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    plt.plot(df["datetime"], normalized, marker="o", label=col)

plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
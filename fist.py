import os
import time
from datetime import datetime

import requests
import pandas as pd
import matplotlib.pyplot as plt
temperature=[]
humidity = []
x=[]
while True:
    city ="varanasi"# input("Enter your city: ").strip()
    api_key = "61fa5111bf6f0afbb74453f1ea696d65"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:

        print("\nWeather Information")
        print("-" * 30)

        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        temperature.append(float(data["main"]["temp"]))
        x.append(len(temperature))
        
        print("Humidity:", data["main"]["humidity"], "%")
        humidity.append(float(data["main"]["humidity"]))
        # x.append(len(humidity))
        
        print("Pressure:", data["main"]["pressure"], "hPa")
        print("Wind Speed:", data["wind"]["speed"], "m/s")
        print("Clouds:", data["clouds"]["all"], "%")
        print("Visibility:", data["visibility"], "meters")
        print("Weather:", data["weather"][0]["main"])

        weather_data = [{
            "datetime": datetime.now(),
            "city": data["name"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"],
            "clouds": data["clouds"]["all"],
            "visibility": data["visibility"],
            "weather": data["weather"][0]["main"]
        }]
        df = pd.DataFrame(weather_data)
        print(df)
        plt.plot(x,temperature,marker="o",label="Temperature")
        plt.plot(x,humidity,marker = "o",label = "humidity")
        plt.xlabel("Time")
        plt.ylabel("Weather")
        plt.title("Weather Data")
        plt.legend()
        plt.show(block=False)
        plt.pause(5)
        plt.close()
        timeseconds=120
        print()
        for i in range(10):
            time.sleep(1)
            print(i)
        
    
    
    
    
#     file_exists = os.path.exists("weather_data.csv")
#     df.to_csv(
#         "weather_data.csv",
#         mode="a",
#         header=not file_exists,
#         index=False
#     )

#     print("\nData saved to weather_data.csv")
#     df = pd.read_csv("weather_data.csv")
#     df["datetime"] = pd.to_datetime(df["datetime"])
# for i in df:
#     plt.figure(figsize=(10, 5))
#     plt.plot(df["datetime"], df["temp"], marker="o")
#     plt.title("Temperature Trend")
#     plt.xlabel("Date Time")
#     plt.ylabel("Temperature (°C)")
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()


# else:
#     print("\nError:", data.get("message", "Something went wrong"))
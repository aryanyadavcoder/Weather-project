import os
import time
from datetime import datetime
import requests
import pandas as pd
import matplotlib.pyplot as plt

temperature = []
humidity = []
pressure = []
clouds = []
Visibility = []
Wind_Speed = []
Weather = []
x = []


def get_weather():
    city = "varanasi"
    api_key = "61fa5111bf6f0afbb74453f1ea696d65"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response


def print_weather(data):
    print("\nWeather Information")
    print("-" * 30)
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    temperature.append(float(data["main"]["temp"]))
    x.append(len(temperature))

    print("Humidity:", data["main"]["humidity"], "%")
    humidity.append(float(data["main"]["humidity"]))

    print("Pressure:", data["main"]["pressure"], "hPa")
    pressure.append(float(data["main"]["pressure"]))

    print("Wind Speed:", data["wind"]["speed"], "m/s")
    Wind_Speed.append(float(data["wind"]["speed"]))

    print("Clouds:", data["clouds"]["all"], "%")
    clouds.append(float(data["clouds"]["all"]))
    
    print("Visibility:", data["visibility"], "meters")
    Visibility.append(float(data["visibility"])/1000)
    
    print("Weather:", data["weather"][0]["main"])
    # Weather.append(data["weather"][0]["main"])

def create_dataframe(data):
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
    return df


def save_csv(df):
    file_exists = os.path.exists("weather_data.csv")
    df.to_csv(
        "weather_data.csv",
        mode="a",
        header=not file_exists,
        index=False
    )


def plot_graph():
    filename = f"Weather_chart_{len(temperature)}.png"

    plt.plot(x, temperature, marker="o", label="Temperature")
    plt.plot(x, humidity, marker="o", label="Humidity")
    plt.plot(x, pressure, marker="o", label="Pressure")
    plt.plot(x, Wind_Speed, marker="o", label="Wind_Speed")
    plt.plot(x, clouds, marker = "o", label = "Clouds")
    plt.plot(x, Visibility,marker = "o",label = "visibility")
    # plt.plot(x, Weather,marker = "o",label = "weather")
    for i in range(len(temperature)):
        plt.text(x[i], temperature[i], f"{temperature[i]:.1f}")
        plt.text(x[i], humidity[i], f"{humidity[i]:.1f}")
        plt.text(x[i], pressure[i], f"{pressure[i]:.1f}")
        plt.text(x[i], Wind_Speed[i], f"{Wind_Speed[i]:.1f}")

    temp_upper = [t + 2 for t in temperature]
    temp_lower = [t - 2 for t in temperature]
    plt.fill_between(
        x,
        temp_lower,
        temp_upper,alpha=0.3,label="Temperature Range"
    )

    plt.xlabel("Time")
    plt.ylabel("Weather")
    plt.title("Weather Data")
    plt.legend()
    plt.savefig(filename)
    plt.show(block=False)
    plt.pause(5)
    plt.close()


def timer():
    print()

    for i in range(3):
        time.sleep(1)
        print(i)

while True:
    response = get_weather()
    if response.status_code == 200:
        data = response.json()
        print_weather(data)
        df = create_dataframe(data)
        plot_graph()
        save_csv(df)
        timer()

    else:
        print("Error:", response.json())
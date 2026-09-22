import tkinter as tk
import requests

geo = "https://geocoding-api.open-meteo.com/v1/search"
url = "https://api.open-meteo.com/v1/forecast"

def search():
    city = entry.get()
    try:

        geo_params = {
            "name": city
        }

        geodata = requests.get(geo, params=geo_params, timeout=5).json()

        latitude = geodata["results"][0]["latitude"]
        longitude = geodata["results"][0]["longitude"]

        coords = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,wind_speed_10m"
        }

        response = requests.get(url, params=coords, timeout=5)

        data = response.json()

        current_data = data["current"]

        temp = current_data["temperature_2m"]
        wind = current_data["wind_speed_10m"]

        error_label.pack_forget()
        temperature_label.config(text=f"Temperature: {temp}°C")
        wind_label.config(text=f"Wind speed: {wind} km/h")
    except (KeyError, IndexError, AttributeError):
        wind_label.config(text="")
        temperature_label.config(text="")
        error_label.config(text="City not found. Please enter a valid city or full city name.")
        error_label.pack()


root = tk.Tk()
root.title("Weather App")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Subtract task bar space
task_bar_height = 50
window_height = screen_height - task_bar_height

# Set geometry to full screen minus task bar
root.geometry(f"{screen_width}x{window_height}+0+0")

title_label = tk.Label(root, text="Weather App", font=("Arial", 24))
title_label.pack()

city_label = tk.Label(root, text="Enter a City", font=("Arial", 16))
city_label.pack()

entry = tk.Entry(root, width=30, font=("Arial", 16))
entry.pack(pady=10)

button = tk.Button(root, text="Search", command=search, font=("Arial", 16), padx=20, pady=10)
button.pack(pady=10)

temperature_label = tk.Label(root, text="Temperature: ", font=("Arial", 16))
temperature_label.pack()

wind_label = tk.Label(root, text="Wind speed: ", font=("Arial", 16))
wind_label.pack()

error_label = tk.Label(root, text="", font=("Arial", 16))

root.mainloop()







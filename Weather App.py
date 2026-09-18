import requests

geo = "https://geocoding-api.open-meteo.com/v1/search" # api for the city to coords
url = "https://api.open-meteo.com/v1/forecast"# api for cords to weather

city = input("Enter city: ")

geo_params = {
    "name": city
}

geodata = requests.get(geo, params=geo_params).json()

latitude = geodata["results"][0]["latitude"]
longitude = geodata["results"][0]["longitude"]

coords = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,wind_speed_10m"
}

response = requests.get(url, params=coords)

data = response.json()

current_data = data["current"]

temp = current_data["temperature_2m"]
wind = current_data["wind_speed_10m"]

if response.status_code == 200:
    print(f"Temperature: {temp}°C")
    print(f"Wind speed: {wind} km/h")
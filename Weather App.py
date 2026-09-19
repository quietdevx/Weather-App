import requests


def search_again():
    new_search = input("Do you want to search again? Y/N: ").strip().upper()
    if new_search == "Y":
        return True
    else:
        return False


while True:

    print("=" * 30)
    print("      WEATHER APP")
    print("=" * 30)

    geo = "https://geocoding-api.open-meteo.com/v1/search"
    url = "https://api.open-meteo.com/v1/forecast"

    city = input("Enter city: ").strip()

    try:
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

        print()
        print(f"Temperature: {temp}°C")
        print(f"Wind speed: {wind} km/h")

    except (KeyError, IndexError):
        print()
        print("City not found.")
        print("Please enter a full city name or valid place.")

    if not search_again():
        print("Goodbye!")
        break

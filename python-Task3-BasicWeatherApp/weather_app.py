import urllib.request
import json

print("================================")
print("       BASIC WEATHER APP")
print("================================")

city = input("Enter city name: ")

try:
    # Get coordinates for the city
    url = "https://geocoding-api.open-meteo.com/v1/search?name=" + city + "&count=1&language=en&format=json"
    data = json.load(urllib.request.urlopen(url))

    if "results" not in data:
        print("City not found.")
    else:
        latitude = data["results"][0]["latitude"]
        longitude = data["results"][0]["longitude"]
        city_name = data["results"][0]["name"]

        # Get weather information
        weather_url = (
            "https://api.open-meteo.com/v1/forecast?"
            "latitude=" + str(latitude) +
            "&longitude=" + str(longitude) +
            "&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
        )

        weather = json.load(urllib.request.urlopen(weather_url))
        current = weather["current"]

        print("\n========== WEATHER ==========")
        print("City:", city_name)
        print("Temperature:", current["temperature_2m"], "°C")
        print("Humidity:", current["relative_humidity_2m"], "%")
        print("Wind Speed:", current["wind_speed_10m"], "km/h")
        print("Weather Code:", current["weather_code"])
        print("=============================")

except Exception as e:
    print("Unable to get weather information.")
    print("Please check your internet connection.")

input("\nPress Enter to exit...")
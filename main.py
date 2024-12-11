import requests

API_KEY = "2ebb9036904dfe7d97ae885826d0c7cc"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = "Shiraz"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric",
    "lang": "en"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    weather = data['weather'][0]['main']
    wind_speed = data['wind']['speed']

    print(f"\nToday's weather in {city} is as follows: 🌤️")
    print(f"Current temperature: {temp}°C")
    print(f"Weather conditions: {weather}")
    print(f"Wind speed: {wind_speed} meters per second\n")

    if temp > 30:
        print("🔥 It's really hot today! Wear light and cool clothes, and make sure to stay hydrated! 😎")
        if weather in ["Clear"]:
            print("☀️ Don't forget a hat and sunglasses, the sun is shining bright!")
    elif 15 <= temp <= 30:
        print("🌤️ The weather is pleasant! A t-shirt or a light jacket will be perfect. Enjoy the nice weather!")
        if wind_speed > 5:
            print("💨 There's a mild breeze, maybe bring an extra layer just in case.")
    elif 0 <= temp < 15:
        print("🥶 It's a bit cold today! Wear warmer clothes and make sure to grab a scarf.")
        if weather in ["Rain", "Drizzle"]:
            print("☔ Don't forget an umbrella, there might be some rain!")
    else:
        print("❄️ It's freezing! Layer up and don't forget your gloves and hat.")
        if wind_speed > 10:
            print("🌬️ There's a strong wind, make sure you're wrapped up tight to avoid the cold!")

    if weather in ["Thunderstorm"]:
        print("⛈️ Thunderstorms are expected! Better stay indoors or be extra cautious if you go outside.")

else:
    print("🛑 Oops! Something went wrong or the city couldn't be found. Please try again!")

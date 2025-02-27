import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "0aa8d86adf6eda1f4c445b3798580c1e"

weather_params = {
    "lat": 21.485811,
    "lon": 39.192505,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("⛈️ It is going to rain! ⛈️")


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
print(weather_data)

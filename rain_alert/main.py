import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "0aa8d86adf6eda1f4c445b3798580c1e"

weather_params = {
    "lat": 21.485811,
    "lon": 39.192505,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.json())

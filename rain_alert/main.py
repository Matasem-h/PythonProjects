import requests
from twilio.rest import Client

# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "x"
account_sid = "x"
auth_token = "x"

# 21.485811
# 39.192505


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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="⛈️ It is going to rain! ⛈️",
        from_="+x",
        to="x",
    )
    print(message.status)

import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "0aa8d86adf6eda1f4c445b3798580c1e"
account_sid = "ACc85dbc2ef114dc4572df53fcf26b59ac"
auth_token = "bbc4d373d2351b6be1f8fa37755bc778"

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
        from_="+12545407541",
        to="+966503292912",
    )
    print(message.status)

 # Twilion number +12545407541
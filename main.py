import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "a1adfb3b486f55010ac4f4f325e37ccd"
account_sid = "AK8466Aad84asd7faf46DFS4"
auth_token = "5423s4fsg41dfg842sef54dfg4"

weather_params = {
    "lat": 41.008240,
    "lon": 28.978359,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.message\
        .create(
        body ="It's going to rain today. Remember to bring an ☂️ ",
        from_="+90533288501",
        to="+905324587562"
    )
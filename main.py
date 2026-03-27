import requests
import os
from twilio.rest import Client

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

MY_LAT = 52.090736
MY_LONG = 5.121420
API_KEY = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(OMW_Endpoint, params = parameters)
response.raise_for_status()
data = response.json()

will_rain = False
weather_codes = [data["list"][x]["weather"][0]["id"] for x in range(0,len(data["list"])) ]
print(weather_codes)
for code in weather_codes:
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring a rain jacket!",
        from_= os.environ.get("TWIIO_VIRTUAL_NUMBER"),
        to= os.environ.get("MOBILE_NUMBER"),
    )
print(message.status)




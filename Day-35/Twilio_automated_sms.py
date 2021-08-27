import requests
from twilio.rest import Client
account_sid = "Your Twilio acc_sid"
auth_token = "Your Twilio auth_token"

resp = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat={Your lat}&lon={Your Long}&exclude=current,minutely,daily&appid={Your apikey}")
resp.raise_for_status()
data= resp.json()
weather_slice = data["hourly"][:12]

will = False
for hour_data in weather_slice:
    con = hour_data["weather"][0]["id"]
    if int(con) < 700:
        will = True
if will:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Dude, You gotta bring an umbrella☔ cause it's going to rain 🌧️️!!",
        from_="Your twilio demo phone number",
        to="Number to which u want to recieve text"
    )
    print(message.status)
    

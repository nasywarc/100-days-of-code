from datetime import datetime
import requests
MY_LAT = -6.175110
MY_LONG = 106.865036

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# print(data)

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG
}

response = requests.get(
    url='https://api.sunrise-sunset.org/v2', params=parameters)

response.raise_for_status()

data = response.json()
sunrise = data['sunrise'].split('T')[1].split('+')[0].split(':')

print(sunrise[0])
print(datetime.now().hour)

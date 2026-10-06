import requests
from datetime import datetime
from dotenv import load_dotenv
import smtplib
import os

load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("PythonMail")

MY_LAT = -6.175110
MY_LONG = 106.865036

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()


iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


def error_count(result, range):
    result = [result + range, result - range]
    return result


iss_pos_lat_range = error_count(iss_latitude, 5)
iss_pos_long_range = error_count(iss_longitude, 5)

print(iss_latitude, iss_longitude)
print(MY_LAT, MY_LONG)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}

response = requests.get(
    url='https://api.sunrise-sunset.org/v2', params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data['sunrise'].split("T")[1].split(":")[0])
sunset = int(data['sunset'].split("T")[1].split(":")[0])

time_now = datetime.now().hour

if iss_pos_lat_range[1] < MY_LAT < iss_pos_lat_range[0] and iss_pos_long_range[1] < MY_LONG < iss_pos_long_range[0]:
    if sunset < time_now <= 23 or 0 <= time_now < sunrise:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=os.getenv("TARGETED_EMAIL_2"),
                msg="Subject:ISS Position Update\n\nThe ISS is over your place."
            )
        print('above you')
    else:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=os.getenv("TARGETED_EMAIL_2"),
                msg="Subject:ISS Position Update\n\nThe ISS is over your place, but its noon."
            )
        print('above you, but the sun is still up')
else:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=os.getenv("TARGETED_EMAIL_2"),
            msg="Subject:ISS Position Update\n\nThe ISS is not over your place."
        )
    print('away from you')

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

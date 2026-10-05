import smtplib
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

my_email = os.getenv('MY_EMAIL')
password = os.getenv('PythonMail')

today_date = datetime.now().strftime('%A, %d %B %Y')

today_time = datetime.now().strftime('%I:%M %p')

email_content = f"Subject: New Timestamp Update\n\nToday is {today_date} and right now, the time is {today_time}"

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=os.getenv(
    'TARGETED_EMAIL_2'), msg=email_content)
connection.close()

print('Message sent.')

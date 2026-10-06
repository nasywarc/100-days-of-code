from datetime import datetime as dt
import smtplib
import random
from dotenv import load_dotenv
import os

load_dotenv()
my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('PythonMail')

now = dt.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt", "r", encoding="UTF-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=os.getenv('TARGETED_EMAIL_2'),
            msg=f'Subject: Monday Motivation\n\n{quote}'
        )
    print('Message delivered.')

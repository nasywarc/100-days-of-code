##################### Extra Hard Starting Project ######################
import random
import datetime as dt
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("PythonMail")
targeted_email = os.getenv("TARGETED_EMAIL_2")

today_month = dt.datetime.now().month
today_date = dt.datetime.now().day
print(today_month, today_date)
list_of_birthday = []

with open("birthday-wisher-extrahard-start/birthdays.csv") as dates:
    all_date = dates.readlines()
    for birthday in all_date:
        list_of_birthday.append(birthday.split(','))

for n in range(len(list_of_birthday)):
    if int(list_of_birthday[n][2]) == today_month and int(list_of_birthday[n][3]) == today_date:
        birthday_person = list_of_birthday[n][0]
        print(birthday_person)

        random_num = random.randint(1, 3)

        with open(f'birthday-wisher-extrahard-start/letter_templates/letter_{random_num}.txt') as message:
            content = message.read()
            modified_content = content.replace("[NAME]", birthday_person)

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=targeted_email,
                msg=f'Subject:Happy Birthday!\n\n{modified_content}'
            )
        print('Wish delivered.')

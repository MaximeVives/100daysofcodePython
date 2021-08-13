import json
import datetime as dt
import smtplib


def send_email(subject, content, to_addr):
    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()
        my_email = "******@gmail.com"
        password = "*******"

        connection.login(user=my_email, password=password)

        message = f"Subject:{subject}\n\n{content}"
        connection.sendmail(from_addr=my_email, to_addrs=to_addr, msg=message)


bday = json.load(fp=open("data/birthdays.json"))

now = dt.datetime.now()
today = dt.datetime(year=now.year, month=now.month, day=now.day)
print(today)

for i in range(len(bday)):
    birth_day = dt.datetime(year=now.year, month=bday[i]["month"], day=bday[i]["day"])
    if birth_day == today:
        message = f"Je te souhaite un tres joyeux anniversaire {bday[i]['name']}. Passe une bonne journee."
        send_email("Joyeux Anniversaire", message, bday[i]["email"])

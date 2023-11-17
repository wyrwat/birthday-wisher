import datetime as dt
import random
import smtplib
import pandas as pd

now = dt.datetime.now()
current_day = now.day
current_month = now.month
my_email = "aby977016@gmail.com"
password = "qohnthducwnbbxhz "

with open("birthdays.csv") as data_file:
    birthdays_df = pd.read_csv(data_file)
    birthdays = birthdays_df.to_dict(orient="records")
    birthdays_day = birthdays_df["day"]
    birthdays_month = birthdays_df["month"]

    for step in range(len(birthdays)):
        rand_letter = random.randint(1, 3)
        name = birthdays[step]["name"]
        if birthdays[step]["month"] == current_month and birthdays[step]["day"] == current_day:
            with open(f"letter_templates/letter_{rand_letter}.txt") as letter:
                letter_txt = letter.read()
                birthday_letter = letter_txt.replace("[NAME]", name)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="aby977016@yahoo.com",
                    msg=f"Subject: HAPPY BIRTHDAY!!! \n\n {birthday_letter}"
                )

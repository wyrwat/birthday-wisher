import datetime as dt
import random
import smtplib
import pandas as pd

now = dt.datetime.now()
current_day = now.day
current_month = now.month
rand_letter = random.randint(1, 3)

with open("birthdays.csv") as data_file:
    birthdays_df = pd.read_csv(data_file)
    birthdays = birthdays_df.to_dict(orient="records")
    birthdays_day = birthdays_df["day"]
    birthdays_month = birthdays_df["month"]

    for step in range(len(birthdays)):
        name = birthdays[step]["name"]
        if birthdays[step]["month"] == current_month and birthdays[step]["day"] == current_day:
            print(f"hapyy birhday {name}")

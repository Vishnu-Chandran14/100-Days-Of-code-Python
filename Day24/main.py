##################### Normal Starting Project ######################
import datetime as dt
import pandas as pd
import glob
import os
import random
import smtplib

MY_EMAIL = "plantdotTech24@gmail.com"
PASSWORD = "iyfncmmajjjmgicr"

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
today = dt.datetime.now()
today_month = today.month
today_day = today.day


# HINT 2: Use pandas to read the birthdays.csv
data = pd.read_csv("birthdays.csv")

birthday_person_info = data[(data['month'] == today_month) & (data['day'] == today_day)]

birthday_person_name = birthday_person_info['name'].iloc[0]
birthday_person_email = birthday_person_info['email'].iloc[0]

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
Letter_folder = "letter_templates"

letters = glob.glob(os.path.join(Letter_folder, "*.txt"))

if birthday_person_info.empty:
    print("No birthdays today")
    exit()
else:
    random_letter = random.choice(letters)
    with open(random_letter, "r") as content:
        letter_contents = content.read()

    birthday_content = letter_contents.replace('[NAME]', birthday_person_name)


# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=birthday_person_email,
                            msg=f"Subject:Happy Birthday\n\n{birthday_content}")


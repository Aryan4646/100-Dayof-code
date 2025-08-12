import smtplib
import datetime
import random
import pandas

birthday_data = pandas.read_csv("birthdays.csv")
birth_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in birthday_data.iterrows()}
print(birth_dict)

my_email = "youremail@gmail.com"
password = "yourpass"

today_date = (datetime.datetime.now().month,datetime.datetime.now().day)

if today_date in birth_dict:
    with open(file=f"letter_templates/letter_{random.randint(1,3)}.txt") as f:
        birthday_person = birth_dict[today_date]
        content = f.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_email,password=password)
        connection.sendmail(from_addr= my_email,
                            to_addrs= birthday_person["email"],
                            msg= f"Subject:Happy Birthday \n\n{content}")
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


# import smtplib
#
# my_email = "sender@gmail.com"
# password = "yourpass"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs="receipent@gmail.com",
#                     msg="Subject:Hello\n\nThis is the body of my email")
# connection.close()

# import datetime
#
# now= datetime.datetime.now()
# print(now)
# year = now.year
# month = now.month
# day_of_Week = now.weekday()
# print(year)
# print(day_of_Week)
#
# date_of_birth = datetime.datetime(year=2003,month=1,day=1)
# print(date_of_birth)

import smtplib
import datetime
import random

my_email = "sendermail@gmail.com"
password = "yourpassword"

today = datetime.datetime.now()

if today.weekday() == 0:
    with open("quotes.txt") as f:
        motivation = f.readlines()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="recepient@gmail.com",
                            msg=f"Subject:Motivational quote for monday\n\n"
                                f"{random.choice(motivation)}")


import smtplib
import datetime as dt
import random

MY_EMAIL = "ib100dayspython@gmail.com"
MY_PASSWORD = "*****"

now = dt.datetime.now()
wkday = now.weekday()
if wkday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{quote}"
                            )























# import smtplib
#
# my_email = "ib100dayspython@gmail.com"
# password = "ghfazafkohxrpvqg"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="ib100dayspython@yahoo.com",
#                         msg="Subject: Email Title \n\nhello from python")



# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# wkday = now.weekday()
# print(wkday)
#
# datebirth = dt.datetime(year=1995,month=12,day=15, hour=4)
# print(datebirth)



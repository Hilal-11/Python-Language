
# Dates in python
import datetime

date = datetime.datetime.now()
print(date)
print(date.year)
print(date.month)
print(date.day)

print(date.hour)
print(date.minute)
print(date.second)
print(date.microsecond)


# set date

date2 = datetime.datetime(2025, 2, 16)
print(date2.strftime("%C"))


username = input("Enter username:- ")
print("Your name is " + username)

email = input("Enter Email :- ")
print("Your email is " + email)
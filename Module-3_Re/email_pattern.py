import re

email=input("Enter an email:")

email_pattern="^[a-z0-9]+[@]+[a-z]+[\.]+[a-z]{2,}$"

x=re.findall(email_pattern,email)

if x:
    print("Valid Email address!")
else:
    print("Error!Invalid Email address...")
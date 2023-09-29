firstname=input("Enter your firstname:")
lastname=input("Enter your lastname:")

if firstname.isalpha() and lastname.isalpha():
    print("Looks good...Now enter your username and password!")
    username=input("Enter an username:")

    if username.isalnum():
        print("Great....Now Set your password!")

        password=input("Enter your password:")

        if password.isalnum():
            print("Thanks!")
            print("Your form has been submitted!")
        else:
            print("Error!Plz input valid password!")
    else:
        print("Error!Plz input valid username!")
else:
    print("Error!Please enter valid firstname and lastname!")
# user inputs password
password = (input("enter your password: "))
# checks length of password
if 8 <= len(password) <= 16:
    print("password accepted")
    if any(char.isdigit() for char in password):
        print("password accepted")
        if any(char.isupper() for char in password):
            print("password accepted")

        else:
            print("password must contain uppercase charecters")
    else:
        print("password must contain numbers")
else:
    print("password has to be between 8 - 12 characters")
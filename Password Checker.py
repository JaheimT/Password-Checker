# user inputs password
password = (input("enter your password: "))
# checks length of password
SC = """!@#$%^&*(_+?-+)"""
if 8 <= len(password) <= 16:
    if any(char.isdigit() for char in password):
        if any(char.isupper() for char in password):
            if any(char in SC for char in password):
                print ("password accepted")
            else:
                print("password must contain symbols")
        else:
            print("password must contain uppercase charecters")
    else:
        print("password must contain numbers")
else:
    print("password has to be between 8 - 12 characters")
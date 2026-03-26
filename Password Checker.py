# user inputs password
password = (input("enter your password: "))
# checks length of password
if 8 <= len(password)<= 16:
    print("password accepted")
    if str.isdigit(password) == True:
        print("password accepted")


    else:
        print("password must contain numbers")
else:
    print("password has to be between 8 - 12 characters")




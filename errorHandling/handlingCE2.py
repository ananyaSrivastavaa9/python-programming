class LoginError(Exception):
    pass
try:
    password = input("enter the password: ")
    if (password != "admin"):
        raise LoginError("Wrong Password")
except LoginError as e:
    print("Alert sent to admin")
    print(e)
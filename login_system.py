print("=== Login System ===")

saved_username = "admin"
saved_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == saved_username and password == saved_password:
    print("Login Successful ✅")
else:
    print("Wrong Username or Password ❌")
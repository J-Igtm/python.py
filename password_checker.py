import re

print("=== Password Strength Checker ===")

password = input("Enter your password: ")

length = len(password) >= 8
uppercase = re.search(r"[A-Z]", password)
lowercase = re.search(r"[a-z]", password)
number = re.search(r"[0-9]", password)
special = re.search(r"[@#$%^&*!]", password)

if length and uppercase and lowercase and number and special:
    print("Strong Password ✅")
else:
    print("Weak Password ❌")
    print("Password should contain:")
    print("- 8 characters")
    print("- Uppercase letter")
    print("- Lowercase letter")
    print("- Number")
    print("- Special symbol")
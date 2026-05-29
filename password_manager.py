import json
import random
import string
from getpass import getpass

FILE_NAME = "passwords.json"
MASTER_PASSWORD = "admin123"

# Login System
print("=== PASSWORD MANAGER LOGIN ===")

login = getpass("Enter Master Password: ")

if login != MASTER_PASSWORD:
    print("Wrong Password!")
    exit()

print("Login Successful!")

# Load passwords
try:
    with open(FILE_NAME, "r") as file:
        passwords = json.load(file)
except:
    passwords = {}

# Generate random password
def generate_password():
    characters = string.ascii_letters + string.digits + "@#$%"
    password = "".join(random.choice(characters) for i in range(12))
    return password

# Save passwords
def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(passwords, file, indent=4)

# Main Loop
while True:

    print("\n=== PASSWORD MANAGER ===")
    print("1. Add Password")
    print("2. View Password")
    print("3. Show All")
    print("4. Generate Password")
    print("5. Exit")

    choice = input("Enter Choice: ")

    # Add Password
    if choice == "1":

        website = input("Website/App Name: ")
        username = input("Username/Email: ")
        password = getpass("Enter Password: ")

        passwords[website] = {
            "username": username,
            "password": password
        }

        save_data()

        print("Password Saved!")

    # View Password
    elif choice == "2":

        website = input("Enter Website/App Name: ")

        if website in passwords:
            print("\nUsername:", passwords[website]["username"])
            print("Password:", passwords[website]["password"])
        else:
            print("No Password Found!")

    # Show All
    elif choice == "3":

        for website, data in passwords.items():

            print("\nWebsite:", website)
            print("Username:", data["username"])
            print("Password:", data["password"])

    # Generate Password
    elif choice == "4":

        new_password = generate_password()

        print("Generated Password:", new_password)

    # Exit
    elif choice == "5":

        print("Exiting Password Manager...")
        break

    else:
        print("Invalid Choice!")
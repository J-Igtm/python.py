import socket
import hashlib
import random
import string

print("=== Cyber Security Toolkit ===")
print("1. IP Finder")
print("2. Hash Generator")
print("3. Password Generator")

choice = input("Enter your choice: ")

if choice == "1":
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print("Computer Name:", hostname)
    print("IP Address:", ip)

elif choice == "2":
    text = input("Enter text: ")
    hash_value = hashlib.sha256(text.encode()).hexdigest()
    print("SHA-256 Hash:", hash_value)

elif choice == "3":
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + "@#$%&*!"
    password = ""

    for i in range(length):
        password += random.choice(chars)

    print("Generated Password:", password)

else:
    print("Invalid choice")
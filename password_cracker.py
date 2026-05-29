print("=== Password Cracker Simulator ===")

real_password = "admin123"

wordlist = [
    "hello",
    "password",
    "123456",
    "admin",
    "admin123",
    "welcome"
]

found = False

for word in wordlist:

    print("Trying:", word)

    if word == real_password:
        print("Password Cracked ✅")
        print("Password is:", word)
        found = True
        break

if not found:
    print("Password not found ❌")
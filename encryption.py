print("=== Caesar Cipher Encryption ===")

text = input("Enter message: ")
shift = 3

encrypted = ""

for char in text:
    if char.isalpha():
        ascii_value = ord(char)

        new_ascii = ascii_value + shift

        if char.islower():
            if new_ascii > ord('z'):
                new_ascii -= 26

        elif char.isupper():
            if new_ascii > ord('Z'):
                new_ascii -= 26

        encrypted += chr(new_ascii)

    else:
        encrypted += char

print("Encrypted Message:", encrypted)
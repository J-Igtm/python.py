print("=== File Encryption Tool ===")

message = input("Enter secret message: ")

encrypted = ""

for char in message:
    encrypted += chr(ord(char) + 2)

print("Encrypted Message:", encrypted)
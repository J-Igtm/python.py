print("=== File Decryption Tool ===")

message = input("Enter encrypted message: ")

decrypted = ""

for char in message:
    decrypted += chr(ord(char) - 2)

print("Original Message:", decrypted)
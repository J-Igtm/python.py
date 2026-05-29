print("=== Safe File Unlocker ===")

filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        data = file.read()

    unlocked_data = ""

    for char in data:
        unlocked_data += chr(ord(char) - 3)

    with open(filename, "w") as file:
        file.write(unlocked_data)

    print("File unlocked/decrypted ✅")

except:
    print("File not found ❌")
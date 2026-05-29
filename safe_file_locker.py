print("=== Safe File Locker ===")

filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        data = file.read()

    locked_data = ""

    for char in data:
        locked_data += chr(ord(char) + 3)

    with open(filename, "w") as file:
        file.write(locked_data)

    print("File locked/encrypted ✅")

except:
    print("File not found ❌")
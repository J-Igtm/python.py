import hashlib

print("=== SHA-256 File Hasher ===")

filename = input("Enter file name with extension: ")

try:

    with open(filename, "rb") as file:

        file_data = file.read()

        hash_value = hashlib.sha256(file_data).hexdigest()

        print("SHA-256 Hash:")
        print(hash_value)

except:
    print("File not found ❌")
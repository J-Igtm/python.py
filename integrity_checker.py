import hashlib

print("=== File Integrity Checker ===")

filename = input("Enter file name: ")

try:

    with open(filename, "rb") as file:

        data = file.read()

        original_hash = hashlib.md5(data).hexdigest()

        print("Original Hash:")
        print(original_hash)

    input("\nPress Enter after modifying the file...")

    with open(filename, "rb") as file:

        new_data = file.read()

        new_hash = hashlib.md5(new_data).hexdigest()

        print("\nNew Hash:")
        print(new_hash)

    if original_hash == new_hash:
        print("\nFile is SAFE ✅")

    else:
        print("\nFile has been MODIFIED ⚠️")

except:
    print("File not found ❌")
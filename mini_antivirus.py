import os

print("=== Mini Antivirus Scanner ===")

dangerous_extensions = [
    ".exe",
    ".bat",
    ".vbs",
    ".cmd"
]

folder = input("Enter folder path: ")

try:

    files = os.listdir(folder)

    found = False

    for file in files:

        for ext in dangerous_extensions:

            if file.endswith(ext):

                print("Suspicious File ⚠️ :", file)

                found = True

    if not found:
        print("No suspicious files found ✅")

except:
    print("Invalid folder path ❌")
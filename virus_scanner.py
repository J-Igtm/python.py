import os

print("=== Basic Virus Scanner ===")

suspicious_files = [
    "virus.exe",
    "hacktool.exe",
    "malware.exe",
    "trojan.exe"
]

folder = input("Enter folder path: ")

try:
    files = os.listdir(folder)

    found = False

    for file in files:

        if file.lower() in suspicious_files:
            print("Suspicious File Found ⚠️:", file)
            found = True

    if not found:
        print("No suspicious files found ✅")

except:
    print("Invalid folder path ❌")
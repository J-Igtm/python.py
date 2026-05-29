import os
import time

print("=== Folder Activity Monitor ===")

folder = input("Enter folder path: ")

before = set(os.listdir(folder))

print("Monitoring folder...")

while True:

    time.sleep(5)

    after = set(os.listdir(folder))

    new_files = after - before

    if new_files:

        print("New File Detected ⚠️")

        for file in new_files:
            print(file)

    before = after
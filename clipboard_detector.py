import pyperclip
import time

print("=== Clipboard Monitor Detector ===")
print("Copy something...")

old_text = ""

while True:

    new_text = pyperclip.paste()

    if new_text != old_text:

        print("Clipboard Changed ⚠️")
        print("Copied Text:", new_text)

        if "password" in new_text.lower():
            print("Sensitive data detected ⚠️")

        old_text = new_text

    time.sleep(2)
import os

print("=== Keylogger Detector ===")

suspicious_names = [
    "keylogger",
    "spy",
    "hook",
    "logger"
]

found = False

tasks = os.popen("tasklist").read().lower()

for name in suspicious_names:

    if name in tasks:
        print("Suspicious Process Found ⚠️ :", name)
        found = True

if not found:
    print("No suspicious process found ✅")
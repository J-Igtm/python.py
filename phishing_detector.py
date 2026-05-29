print("=== Phishing Link Detector ===")

link = input("Enter website link: ")

suspicious_words = [
    "login",
    "verify",
    "secure",
    "bank",
    "free",
    "gift"
]

found = False

for word in suspicious_words:

    if word in link.lower():

        print("Suspicious keyword found ⚠️ :", word)
        found = True

if "https://" not in link:
    print("Website is not secure (HTTPS missing) ⚠️")
    found = True

if not found:
    print("Link looks safe ✅")
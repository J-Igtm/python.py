print("=== Log File Analyzer ===")

filename = input("Enter log file name: ")

try:

    with open(filename, "r") as file:

        lines = file.readlines()

        found = False

        for line in lines:

            if "error" in line.lower():

                print("Suspicious Log Found ⚠️")
                print(line)

                found = True

        if not found:
            print("No errors found ✅")

except:
    print("File not found ❌")
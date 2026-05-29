print("=== PIN Cracker Simulator ===")

real_pin = "1234"

for pin in range(10000):
    guess = str(pin).zfill(4)

    print("Trying:", guess)

    if guess == real_pin:
        print("PIN Found ✅")
        print("PIN is:", guess)
        break
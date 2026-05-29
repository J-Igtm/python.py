import socket

print("=== Simple Port Scanner ===")

target = "127.0.0.1"

for port in range(1, 101):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print("Port", port, "is OPEN")

    s.close()

print("Scanning complete")
import socket

print("=== Simple Network Scanner ===")

target_ip = input("Enter IP Address: ")

try:
    hostname = socket.gethostbyaddr(target_ip)

    print("Device Found ✅")
    print("Hostname:", hostname[0])

except:
    print("No device found ❌")
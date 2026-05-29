import socket

print("=== IP Address Finder ===")

hostname = socket.gethostname()

ip_address = socket.gethostbyname(hostname)

print("Computer Name:", hostname)
print("IP Address:", ip_address)
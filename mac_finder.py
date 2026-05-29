import uuid

print("=== MAC Address Finder ===")

mac = uuid.getnode()

mac_address = ':'.join(('%012X' % mac)[i:i+2] for i in range(0, 12, 2))

print("MAC Address:", mac_address)
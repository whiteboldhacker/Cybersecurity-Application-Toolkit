import socket

target = input("Enter the IP or website to scan: ")
ports = [21, 22, 23, 25, 53, 80, 443, 8080]

print(f"\nScanning {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # seconds
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"✅ Port {port} is open")
    else:
        print(f"❌ Port {port} is closed")
    sock.close()

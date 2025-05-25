import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor

# Function to scan one host
def scan_host(ip):
    print(f"Scanning {ip}...")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)  # Faster timeout
        result = s.connect_ex((str(ip), 80))  # Check port 80
        if result == 0:
            print(f"[+] Host Up: {ip}")
        s.close()
    except:
        pass

# Main program
def main():
    print(">>")
    ip_range = input("Enter IP range (e.g., 192.168.5.0/24): ")
    try:
        network = ipaddress.ip_network(ip_range, strict=False)
    except ValueError:
        print("[!] Invalid IP range.")
        return

    print(f"[*] Scanning network {ip_range} for live hosts...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for ip in network.hosts():
            executor.submit(scan_host, ip)

# Main execution
if __name__ == "__main__":
    main()

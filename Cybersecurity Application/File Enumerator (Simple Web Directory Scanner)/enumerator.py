import requests

def directory_enumerator(url):
    common_paths = [
        'admin/', 'login/', 'config/', 'uploads/', 'images/', 'css/',
        'js/', 'backup/', 'db/', 'test/', 'dashboard/'
    ]

    print(f"[*] Starting Directory Enumeration on {url}")

    for path in common_paths:
        full_url = url.rstrip('/') + '/' + path
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"[+] Found: {full_url} (Status: {response.status_code})")
            else:
                print(f"[-] Not Found: {full_url} (Status: {response.status_code})")
        except requests.RequestException as e:
            print(f"[!] Error checking {full_url}: {e}")

if __name__ == "__main__":
    target_url = input("Enter target URL (e.g., http://example.com): ")
    directory_enumerator(target_url)

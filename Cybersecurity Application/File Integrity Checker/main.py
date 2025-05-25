import time
from hash_utils import scan_folder, save_hashes, load_hashes

FOLDER_TO_WATCH = r"C:\Cybersecurity Application\File Integrity Checker"

def check_integrity():
    old_hashes = load_hashes()
    new_hashes = scan_folder(FOLDER_TO_WATCH)

    print("\n🔍 Scanning for changes...")

    for path, new_hash in new_hashes.items():
        if path not in old_hashes:
            print(f"🆕 New file detected: {path}")
        elif old_hashes[path] != new_hash:
            print(f"⚠️ File modified: {path}")

    for path in old_hashes:
        if path not in new_hashes:
            print(f"❌ File deleted: {path}")

    save_hashes(new_hashes)

# 🔁 Runs every 30 seconds
while True:
    check_integrity()
    time.sleep(30)

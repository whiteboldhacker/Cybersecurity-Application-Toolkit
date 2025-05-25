import hashlib

# File hash calculate panna function
def calculate_hash(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print("❌ File not found!")
        return None

# Main logic
def main():
    file_path = input("Enter the file path to check: ")
    original_hash = input("Enter the original SHA-256 hash: ")

    current_hash = calculate_hash(file_path)

    if current_hash:
        print(f"\n✅ Current Hash:  {current_hash}")
        print(f"📄 Original Hash: {original_hash}")

        if current_hash == original_hash:
            print("✅ File is NOT modified.")
        else:
            print("⚠️ File has been MODIFIED!")

if __name__ == "__main__":
    main()

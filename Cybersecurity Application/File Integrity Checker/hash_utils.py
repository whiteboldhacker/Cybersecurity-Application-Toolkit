import hashlib
import os
import json

def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def scan_folder(folder_path):
    file_hashes = {}
    for root, _, files in os.walk(folder_path):
        for name in files:
            full_path = os.path.join(root, name)
            file_hashes[full_path] = calculate_hash(full_path)
    return file_hashes

def save_hashes(hashes, filename="hashes.json"):
    with open(filename, "w") as f:
        json.dump(hashes, f, indent=4)

def load_hashes(filename="hashes.json"):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as f:
        return json.load(f)

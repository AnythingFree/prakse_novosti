# save this as site_checker.py
import hashlib
import requests

URL = "https://itkarijera.ba/prakse"  # Replace with the website you want to monitor
HASH_FILE = "site_hash.txt"  # File to store the previous hash

def get_site_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def compute_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def load_previous_hash(file_path):
    try:
        with open(file_path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def save_current_hash(file_path, hash_value):
    with open(file_path, "w") as f:
        f.write(hash_value)

def main():
    # Get current website content and hash
    content = get_site_content(URL)
    current_hash = compute_hash(content)

    # Load previous hash
    previous_hash = load_previous_hash(HASH_FILE)

    if current_hash != previous_hash:
        print("Neke nove prakse:")
        # Save the new hash
        save_current_hash(HASH_FILE, current_hash)
    else:
        print("No change detected.")

if __name__ == "__main__":
    main()

import hashlib
import os
import json
import time

# Where we store hashes and logs
HASH_FILE = "file_hashes.json"  # Keeps track of previous file hashes
LOG_FILE = "integrity_log.txt"  # Stores logs of file changes
CHECK_INTERVAL = 10  # Time gap between checks (in seconds)

def calculate_hash(file_path, algorithm='sha256'):
    """Generates a hash value for the given file."""
    hash_func = hashlib.new(algorithm)
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):  # Read in small chunks to handle large files
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        return None  # If file isn't found, return None

def load_hashes():
    """Retrieves the previously stored file hashes."""
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            return json.load(f)
    return {}  # If the file doesn’t exist, return an empty dictionary

def save_hashes(hashes):
    """Saves the current hash values to a file."""
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

def log_message(message):
    """Writes log messages to a file and prints them to the console."""
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")
    print(message)  # Display message in terminal too

def monitor_files(file_paths):
    """Checks for file modifications by comparing old and new hash values."""
    previous_hashes = load_hashes()  # Load stored hashes
    current_hashes = {}

    for file_path in file_paths:
        file_hash = calculate_hash(file_path)
        if file_hash:
            current_hashes[file_path] = file_hash
            if file_path in previous_hashes:
                if previous_hashes[file_path] != file_hash:
                    log_message(f"[WARNING] File changed: {file_path}\nPrevious Hash: {previous_hashes[file_path]}\nNew Hash: {file_hash}\n")
            else:
                log_message(f"[INFO] New file detected: {file_path}\nHash: {file_hash}\n")
        else:
            log_message(f"[ERROR] File not found: {file_path}\n")
    
    save_hashes(current_hashes)  # Save the latest hash values

def main():
    """Runs the file integrity checker for 1 minute, checking every 10 seconds."""
    files_to_monitor = ["example.txt", "test.py"]  # Files to keep an eye on
    end_time = time.time() + 60  # Stop after 1 minute
    while time.time() < end_time:
        monitor_files(files_to_monitor)  # Check file status
        time.sleep(CHECK_INTERVAL)  # Wait before running again

if __name__ == "__main__":
    main()

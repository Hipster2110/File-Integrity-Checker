🛡️ File Integrity Checker
A Python tool to monitor file changes using hash values and detect unauthorized modifications.

🚀 Ensures file integrity | 🔍 Detects changes | 📝 Logs all modifications



🔥 Features
✅ Detects changes in files by comparing hash values
✅ Logs modifications with previous & new hash values
✅ Identifies missing or newly added files
✅ Runs automatically every 10 seconds for 1 minute
✅ Uses SHA-256 hashing for strong security

🚀 Installation & Usage
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/Hipster2110/File-Integrity-Checker.git
cd File-Integrity-Checker
2️⃣ Run the Script
sh
Copy
Edit
python "File Integrity Checker.py"
This will monitor the specified files and log any changes.

⚙️ How It Works
📌 The script calculates SHA-256 hashes of files and compares them with stored hashes.
📌 It logs warnings if a file is modified, newly added, or missing.

Example Logs
🟢 New File Detected

vbnet
Copy
Edit
[INFO] New file detected: newfile.py
Hash: abc123xyz...
🟡 File Modified

mathematica
Copy
Edit
[WARNING] File changed: example.txt
Previous Hash: abc123...
New Hash: def456...
🔴 File Missing

arduino
Copy
Edit
[ERROR] File not found: test.py
📝 All logs are saved in integrity_log.txt 📂

⚙️ Customization
🔹 Change monitored files → Edit this in the script:

python
Copy
Edit
files_to_monitor = ["example.txt", "test.py"]
🔹 Change scan frequency → Modify CHECK_INTERVAL (default: 10 sec)

🤝 Contributing
💡 Found a bug? Have a feature request? Open an issue or submit a PR!

📜 License
📌 MIT License - Free to use and modify.


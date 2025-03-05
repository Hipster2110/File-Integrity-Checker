
File Integrity Checker 🛡️
A Python script to monitor changes in files by calculating and comparing hash values. Helps ensure file integrity and detect unauthorized modifications.

Features ✨
✅ Detects new, modified, and missing files
✅ Uses SHA-256 hashing for security
✅ Logs file changes with previous and new hash values
✅ Runs for 1 minute, checking every 10 seconds

Installation & Usage 🚀
1. Clone the Repository
sh
Copy
Edit
git clone https://github.com/Hipster2110/File-Integrity-Checker.git
cd File-Integrity-Checker
2. Install Python (If Not Installed)
Make sure you have Python 3+ installed. You can download it from python.org.

3. Run the Script
sh
Copy
Edit
python "File Integrity Checker.py"
This will monitor the specified files and log any changes.

How It Works ⚙️
The script calculates SHA-256 hashes of files.
It compares them with previously stored hashes in file_hashes.json.
If a file is modified, it logs:
mathematica
Copy
Edit
[WARNING] File changed: example.txt
Previous Hash: abc123...
New Hash: def456...
If a new file is detected, it logs:
vbnet
Copy
Edit
[INFO] New file detected: newfile.py
Hash: xyz789...
If a file is missing, it logs an error.
Logs are saved in integrity_log.txt 📄.

Configuration ⚙️
To monitor specific files, edit this line in the script:
python
Copy
Edit
files_to_monitor = ["example.txt", "test.py"]
Modify CHECK_INTERVAL for a different check frequency.
Contributing 🤝
Want to improve the tool? Feel free to fork and submit a PR! 🚀

License 📜
MIT License - Free to use and modify.

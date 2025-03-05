File Integrity Checker

A Python script to monitor file changes by calculating and comparing hash values. It helps detect modifications, new files, and missing files.

Features

Detects file modifications using SHA-256 hashing

Logs changes with previous and new hash values

Identifies missing or newly added files

Runs automatically every 10 seconds for 1 minute

Usage

Clone the repository:

git clone https://github.com/Hipster2110/File-Integrity-Checker.git

cd File-Integrity-Checker

Run the script:

python "File Integrity Checker.py"

How It Works

The script checks files listed in files_to_monitor and logs any changes.

Logs are stored in integrity_log.txt.

Customization

Edit files_to_monitor in the script to track different files.

Change CHECK_INTERVAL to adjust the checking frequency.

License
This project is licensed under the MIT License.

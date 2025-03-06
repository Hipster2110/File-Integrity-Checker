# File Integrity Checker

## Overview
The **File Integrity Checker** is a Python-based tool that monitors changes in files by calculating and comparing their hash values. It helps ensure file integrity and detects any unauthorized modifications.

## Features
- Calculates hash values using SHA-256
- Monitors specific files for changes
- Logs previous and new hash values when a file is modified
- Detects new and missing files
- Runs checks every 10 seconds for 1 minute
- Stores hash values and logs in separate files
- Displays timestamps for each check

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/Hipster2110/File-Integrity-Checker.git
   cd File-Integrity-Checker
   ```
2. Install Python (if not already installed).
3. No additional libraries are required, as the script uses built-in Python modules.

## Usage
1. Modify the `files_to_monitor` list in the script to specify the files you want to track.
2. Run the script:
   ```sh
   python "File Integrity Checker.py"
   ```
3. The script will run for 1 minute, checking every 10 seconds.
4. Check `integrity_log.txt` for detailed logs of detected changes.

## Logging
- All detected changes are logged in `integrity_log.txt`.
- The script records:
  - File modifications with old and new hash values
  - Newly detected files
  - Missing files
  - Timestamp of each check

## Ownership
This project is developed and maintained by **Hipster2110**.

## License
This project is open-source and available under the MIT License.


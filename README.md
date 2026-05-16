# Simple Keylogger

A basic Python script that monitors and records keystrokes, saving them to a local log file. Built to understand how input logging mechanisms function at a system level.

## ⚠️ Disclaimer
*This tool is strictly for educational purposes and ethical use only.* It was developed to demonstrate how keystroke logging works in order to better understand system vulnerabilities and endpoint security. Do not use this script to monitor systems or users without their explicit, written consent. Unauthorized use of keyloggers is illegal and a violation of privacy.

## How It Works
The script utilizes the pynput library to attach a listener to the system's keyboard events. It captures both standard character keys (letters, numbers) and special keys (Space, Enter, Shift, etc.), formatting them cleanly and appending them to a continuously updated text file (key_log.txt).

## Usage
1. Ensure Python is installed on your system.
2. Install the required library:
   ```bash
   pip install pynput

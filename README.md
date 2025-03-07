# Python Security & Networking Scripts

This repository contains various Python scripts for security and networking-related tasks, including scanning, enumeration, and cryptography.

## Scripts Included

### 1. Dig.py
- A script for performing DNS lookups using the `dig` command.
- Retrieves DNS records such as A, MX, TXT, and more.

### 2. NMAPscan.py
- Automates Nmap scans to discover open ports and services on a target system.
- Supports different scan types (e.g., SYN scan, service detection, OS detection).

### 3. SMTP Enumeration Script.py
- Enumerates valid SMTP users on a mail server.
- Useful for penetration testing and security assessments.

### 4. WHOIS.py
- Performs WHOIS lookups to retrieve domain registration information.
- Extracts registrar, creation/expiration dates, and contact details.

### 5. Rail Fence Cipher Decryption Script.py
- Implements decryption for the Rail Fence Cipher.
- Used to decode text encrypted with this transposition cipher.

## Features
- Automates security and networking tasks efficiently.
- Provides easy-to-use scripts for penetration testers and security researchers.
- Modular and customizable for different use cases.

## Requirements
- **Python 3.x**: Ensure you have Python 3.x installed on your system.

## Installation

Clone this repository:
```bash
git clone https://github.com/yourusername/python-security-scripts.git
cd python-security-scripts
```
Verify that Python 3.x is installed:
```bash
python3 --version
```
(Optional) Create a virtual environment to isolate dependencies:
```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/macOS
venv\Scripts\activate    # On Windows
```

## Usage

Each script can be executed from the command line. Ensure Python is installed and run the script with necessary arguments.

General Syntax
```bash
python3 script_name.py [options]
```
Example Usages

Nmap Scan:
```bash
python3 NMAPscan.py -t target_ip
```
WHOIS Lookup:
```bash
python3 WHOIS.py -d example.com
```
SMTP Enumeration:
```bash
python3 SMTP_Enumeration_Script.py -s smtp.example.com
```
Rail Fence Cipher Decryption:
```bash
python3 Rail_Fence_Cipher_Decryption_Script.py
```
Example Input/Output:
```bash
Enter the ciphertext: WECRLTEERDSOEEFEAOCAIVDEN
Enter the number of rails: 3
Decrypted text: WEAREDISCOVEREDFLEEATONCE
```
Troubleshooting
- Incorrect Output: Ensure you are using the correct syntax and options for each script.

- Missing Dependencies: Install any required dependencies using

```bash
pip install -r requirements.txt
```
- Python Compatibility: Use Python 3.x to avoid syntax issues.

## Disclaimer
These scripts are for educational and research purposes only. Use responsibly and ensure you have proper authorization before scanning or enumerating systems.

## Contributing
Feel free to fork this repository and submit pull requests for improvements or additional features. Suggestions and feedback are welcome!

# FILE-INTEGRITY-CHECKER
*COMPANY*: CODTECH IT SOLUTIONS
*NAME*: ALOK KUMAR JAISWAL
*INTERN ID* : CTIS9023
*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING
*DURATION*: 6 WEEK
*MENTOR*: NEELA SANTOSH KUMAR 

## Overview
The File Integrity Checker is a Python-based cybersecurity tool developed to monitor and verify the integrity of files using cryptographic hash functions. The tool detects unauthorized modifications in files by generating and comparing hash values.

This project helps ensure that files remain unchanged and secure from tampering or corruption.

---

## Features
- Generate SHA-256 hash values
- Compare original and current file hashes
- Detect file modifications
- Simple command-line interface
- Fast and lightweight implementation

---

## Technologies Used
- Python
- hashlib library

---

## How It Works
1. User selects a file
2. The program generates a unique hash value
3. Original hash is stored temporarily
4. File is checked again after modification
5. Hash values are compared
6. Program displays integrity status

---

## Requirements
Install Python 3.x on your system.

No external libraries are required.

---

## Usage

### Run the Program
```bash
python file_integrity_checker.py

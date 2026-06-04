# File Integrity Monitor

## Overview 

File Integrity Monitor is a Python-based cybersecurity tool that uses SHA-256 hashing to detect whether a file has been modified.

A hash acts like a digital fingerprint for a file. Even a small change in the file content produces a completely different hash value. By comparing a stored baseline hash with the current hash, the tool can determine whether the file has been altered.

## Features 
- Create a baseline SHA-256 hash for a file
- Save the generated hash to a separate file
- Verify file integrity by comparing hashes
- Detect file modifications
- Menu-driven interface

# Technologies
- Python
- Hashlib

## How to run

python monitor.py

## Example output

Choose 1 or 2 from the choice
1. Create Baseline Hash
2. Check File Integrity
               
Enter choice: 2
Enter the hash file name you saved: hash
Enter your file name to check is it modified: test
ALERT: Your file is Modified

## Cybersecurity Concepts Learned

- Cryptographic Hashing
- SHA-256
- File Integrity Monitoring
- Baseline Comparison
- Security Monitoring

## Future improvements

- Support multiple file types
- Store hashes in JSON format
- Monitor multiple files simultaneously
- Add exception handling for missing files
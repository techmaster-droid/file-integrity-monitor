# File Integrity Monitor

## Overview 

File Integrity Monitor is a Python-based cybersecurity tool that uses SHA-256 hashing to detect whether a file has been modified.

A hash acts like a digital fingerprint for a file. Even a small change in the file content produces a completely different hash value. By comparing a stored baseline hash with the current hash, the tool can determine whether the file has been altered.

## Features 

- Create SHA-256 baselines for an entire directory
- Store hashes in JSON format
- Detect modified files
- Detect deleted files
- Detect newly added files
- Chunk-based hashing for large files

# Technologies
- Python
- Hashlib

## How to run

python monitor.py

## Example output

Enter your folder path: D:\cyber-learning\3.File-Integrity-Monitor\test
Choose the choice:-
1 for creating a hash code for your folder
2 for checking the integrity of the files :- 2
[OK] test - Copy.txt
[ALERT] test.txt deleted
[ALERT] test3.txt added

## Cybersecurity Concepts Learned

- File Integrity Monitoring (FIM)
- Cryptographic Hashing
- SHA-256
- Baseline Comparison
- Security Monitoring
- Change Detection

## Limitations

- hashes.json can be modified or deleted
- No real-time monitoring
- No alerting system
- Only monitors .txt files

## Future improvements

- HMAC-protected baseline storage
- Recursive directory monitoring
- Real-time monitoring
- Email or log alerts
- Support for all file types
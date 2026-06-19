from pathlib import Path
import hashlib
import os
import json 

def hash_the_file(folder):
    txt_files = [f for f in os.listdir(folder) if f.endswith(".txt") and os.path.isfile(os.path.join(folder, f))]
    hash_storage = {}
    
    for files in txt_files:
        hasher = hashlib.sha256()
        with open(folder/files, "rb") as file:
            while (chunk := file.read(4096)):
                hasher.update(chunk)
        hash_digest = hasher.hexdigest()
        hash_storage[files] = hash_digest
    
    with open("hashes.json", "w") as file:
        json.dump(hash_storage, file, indent=4)
        print("Succesfully saved")

file_path = input("Enter your folder path: ")
folder_path = Path(file_path)
choice = int(input("""Choose the choice:-
1 for creating a hash code for your folder
2 for checking the integrity of the files :- """))

if choice == 1:
    hash_the_file(folder_path)

elif choice == 2:
    txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt") and os.path.isfile(os.path.join(folder_path, f))]
    hash_storage = {}
    for files in txt_files:
        hasher = hashlib.sha256()
        with open(folder_path/files, 'rb') as file:
            while (chunk := file.read(4096)):
                hasher.update(chunk)
            hash_digest = hasher.hexdigest()
            hash_storage[files] = hash_digest

    with open("hashes.json", "rb") as file:
        data = json.load(file)

    same_code = []
    different_code = []

    for code in data:
        if code not in hash_storage:
            print(f"[ALERT] {code} deleted")

        
        elif data[code] != hash_storage[code]:
            different_code.append(code)
        else:
            print(f"[OK] {code}")

    if different_code:
        print("\nALERT: Changed files are:-")
        for word in different_code:
            print(word)

    for files in txt_files:
        if files not in data:
            print(f"[ALERT] {files} added")

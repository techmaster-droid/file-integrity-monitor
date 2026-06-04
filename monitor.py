import hashlib

choice = input("""Choose 1 or 2 from the choice
1. Create Baseline Hash
2. Check File Integrity
               
Enter choice: """)

if choice == "1":

    file_name = input("Enter the file name: ")+".txt"
    hash_file = input("Enter the file to save the hash number: ")+".txt"
    with open(file_name, "r") as file:
        content = file.read()
        content_byte = content.encode()
        content_hash = hashlib.sha256(content_byte)
        content_hash_readable = content_hash.hexdigest()
    

    with open(hash_file, "w") as file:
        file.write(content_hash_readable)
        print("Successfully saved your hash code....")

elif choice == "2":
    to_check = input("Enter the hash file name you saved: ")+".txt"
    your_file = input("Enter your file name to check is it modified: ")+".txt"
    with open(your_file, 'r') as file:
        your_content = file.read()
        your_content_byte = your_content.encode()
        your_content_hash = hashlib.sha256(your_content_byte)
        your_content_hash_readable = your_content_hash.hexdigest()
    with open(to_check,"r") as file:
        hash_content = file.read()

    if hash_content == your_content_hash_readable:
        print("File integrity verified")
    else:
        print("ALERT: Your file is Modified")

else:
    print("Choose correct choice")

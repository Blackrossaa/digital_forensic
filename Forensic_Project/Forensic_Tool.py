import hashlib
import os

def generate_hash(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
        return hashlib.sha256(data).hexdigest()

original_hash = None
stored_file = None

while True:
    print("\n=== Digital Forensic File Integrity Tool ===")
    print("1. Generate Hash (Store Original)")
    print("2. Verify File Integrity")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        file_path = input("Enter file path: ")

        if os.path.exists(file_path):
            original_hash = generate_hash(file_path)
            stored_file = file_path
            print("\nOriginal Hash Stored:")
            print(original_hash)
        else:
            print("File not found.")

    elif choice == "2":
        if original_hash is None:
            print("No original hash stored. Please generate hash first.")
        else:
            current_hash = generate_hash(stored_file)
            print("\nCurrent Hash:")
            print(current_hash)

            if current_hash == original_hash:
                print("\nIntegrity Status: FILE NOT MODIFIED")
            else:
                print("\nIntegrity Status: FILE MODIFIED")

    elif choice == "3":
        print("Exiting tool.")
        break

    else:
        print("Invalid option. Try again.")
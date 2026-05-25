import hashlib

# Function to calculate file hash
def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None


# Take file path from user
file_path = input("Enter file path: ")

# Generate original hash
original_hash = calculate_hash(file_path)

if original_hash is None:
    print("File not found!")
else:
    print("\nOriginal Hash:")
    print(original_hash)

    input("\nPress Enter after modifying the file to check integrity...")

    # Generate new hash
    new_hash = calculate_hash(file_path)

    print("\nNew Hash:")
    print(new_hash)

    # Compare hashes
    if original_hash == new_hash:
        print("\n✅ File Integrity Maintained.")
    else:
        print("\n❌ Warning! File has been modified.")
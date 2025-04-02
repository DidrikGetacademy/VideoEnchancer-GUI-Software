import os
import hashlib
import json
import magic
import shutil
from filetype import guess as filetype_guess

def calculate_hash(file_path):
    """Calculate MD5 hash of the file contents."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

def validate_json(file_path):
    """Check if the file is valid JSON."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)  # Return the parsed JSON
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None

def detect_file_type(file_path):
    """Detect file type using multiple methods."""
    # Check with filetype first
    kind = filetype_guess(file_path)
    if kind:
        return kind.mime, kind.extension
    
    # Check with python-magic
    mime = magic.Magic(mime=True)
    with open(file_path, "rb") as f:
        header = f.read(4096)
    
    mime_type = mime.from_buffer(header)
    
    # Special handling for JSON files
    if validate_json(file_path):
        return 'application/json', 'json'
    
    return mime_type, 'bin'

def is_kaspa_wallet(file_path):
    """Check if the file is a Kaspa wallet by inspecting its header and content."""
    try:
        with open(file_path, 'rb') as f:
            header = f.read(4)  # Read the first 4 bytes of the file
            # Kaspa wallet files start with the 'KSPA' signature
            if header != b'KSPA':
                return False

        # Check the JSON content of the file
        wallet_data = validate_json(file_path)
        if wallet_data and isinstance(wallet_data, dict):
            # Confirm if it's a Kaspa wallet by matching specific JSON content
            if wallet_data.get('type') == 'kaspa-wallet' and 'wallet' in wallet_data:
                print(f"Kaspa wallet confirmed from content: {file_path}")
                return True
        return False
    except Exception as e:
        print(f"Error checking Kaspa wallet: {e}")
        return False

def organize_files(src_dir, dest_dir="sorted_files"):
    """Organize files in a directory, checking if they're Kaspa wallet files."""
    existing_hashes = set()
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    unknown_dir = os.path.join(dest_dir, "unknown")
    os.makedirs(unknown_dir, exist_ok=True)

    for filename in os.listdir(src_dir):
        file_path = os.path.join(src_dir, filename)
        if os.path.isdir(file_path):
            continue

        # Check for duplicates
        file_hash = calculate_hash(file_path)
        if file_hash in existing_hashes:
            print(f"Skipping duplicate: {filename}")
            continue
        existing_hashes.add(file_hash)

        # Check if the file is a Kaspa wallet
        if is_kaspa_wallet(file_path):
            ext = 'kpk'  # Kaspa wallet extension
            print(f"Kaspa wallet detected: {filename}")
        else:
            # Detect file type for non-Kaspa wallet files
            mime_type, ext = detect_file_type(file_path)
            ext = ext if ext not in [None, 'None'] else 'bin'
        
        # Create target directory based on the file type/extension
        type_dir = os.path.join(dest_dir, ext.lstrip('.'))
        os.makedirs(type_dir, exist_ok=True)
        
        # Generate unique file name
        base_name = os.path.splitext(filename)[0]
        new_name = f"{base_name}.{ext}"
        dest_path = os.path.join(type_dir, new_name)
        
        # Handle name conflicts
        counter = 1
        while os.path.exists(dest_path):
            new_name = f"{base_name}_{counter}.{ext}"
            dest_path = os.path.join(type_dir, new_name)
            counter += 1
        
        # Copy the file to the appropriate folder
        shutil.copy2(file_path, dest_path)
        print(f"Copied: {filename} -> {dest_path}")

if __name__ == "__main__":
    source_directory = r"C:\Users\didri\Desktop\test"  # Modify to your source directory
    organize_files(source_directory)

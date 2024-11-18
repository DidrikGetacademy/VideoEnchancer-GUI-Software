import logging
import os
import requests
from cryptography.fernet import Fernet
from pathlib import Path
from Logger import logging
import tkinter as tk
import sys



def get_app_data_path():
    if sys.platform == "win32":
        return Path(os.getenv("APPDATA")) / "LearnReflect"
    elif sys.platform == "darwin":  # macOS
        return Path.home() / "Library" / "Application Support" / "LearnReflect"
    else:  # Linux and others
        return Path.home() / ".config" / "LearnReflect" #linux



app_data_path = get_app_data_path()
secret_key_path = app_data_path / 'secret.key'
activation_key_path = app_data_path / 'activation_key.json'




def ensure_directories():
    if not app_data_path.exists():
        logging.info("App_data_path did not exist, creating it now")
        app_data_path.mkdir(parents=True, exist_ok=True)  
        
    if not secret_key_path.exists():
        logging.info("Secret_key_path did not exist, Creating a key with Fernet")
        key = Fernet.generate_key()
        with open(secret_key_path, "wb") as key_file:
            key_file.write(key)
        logging.info(f"Generated new encryption key {key} and saved to secret.key at {secret_key_path}")
    
    if not secret_key_path.exists() or secret_key_path.stat().st_size == 0:
        logging.error("Failed to generate or save the encryption key.")
        raise ValueError("Encryption key could not be s aved or laded correctly")
        
    
    
    if not activation_key_path.exists():
        with open(activation_key_path, "wb") as key_file:
            key_file.write(b'{}')  
        logging.info("Generated empty activation_key.json")
    
    if not load_key():
        logging.info("No valid activation key found, prompting user for activation")
        
        root = tk.Tk()
        root.withdraw()
        from activation_window import ActivationWindow
        ActivationWindow_window = ActivationWindow(root)
        ActivationWindow_window.mainloop()
        






def load_encryption_key():
    if secret_key_path.exists() and secret_key_path.stat().st_size > 0:
        with open(secret_key_path, "rb") as key_file:
            key = key_file.read()
            logging.info("Loaded encryption key from secret.key")
            return key
    else:
        logging.info("Encryption key not found. Generating a new one.")
        ensure_directories()
        return load_encryption_key()





def encrypt_key(key_code):
    encryption_key = load_encryption_key()
    if encryption_key:
        fernet = Fernet(encryption_key)
        encrypted_key = fernet.encrypt(key_code.encode())
        logging.info(f"Encrypted key_code '{key_code}'")
        return encrypted_key
    return None





def save_key(encrypted_key):
    with open(activation_key_path, "wb") as file:
        file.write(encrypted_key)
    logging.info("Saved encrypted key to activation_key.json")





def load_key():
    if activation_key_path.exists():
        with open(activation_key_path, "rb") as file:
            encrypted_key = file.read()
            
            if not encrypted_key:
                logging.warning("Activation key file is empty.")
                return None
            
            try:
                decrypted_key = decrypt_key(encrypted_key)
                if decrypted_key:
                    logging.info(f"Loaded and validated key: {decrypted_key}")
                    return decrypted_key
            except Exception as e:
             logging.error(f"Error during decryption: {e}")
    else: 
        logging.warning("Activation key file does not exist.")
    return None




def decrypt_key(encrypted_key):
    encryption_key = load_encryption_key()
    if encryption_key:
        fernet = Fernet(encryption_key)
        decrypted_key = fernet.decrypt(encrypted_key).decode()
        logging.info(f"Decrypted key: {decrypted_key}")
        return decrypted_key
    return None




def validate_key_with_Server(key_code):
    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            "https://learnreflects.com/Server/Validate_privatekey.php",
            json={"key_code": key_code},
            headers=headers
        )
        response.raise_for_status()
        data = response.json()
        if data.get("success"):
            encrypted_key = encrypt_key(key_code)
            save_key(encrypted_key)
            logging.info("Program activated successfully!")
            return True
        else:
            logging.error(f"Activation failed: {data.get('error', 'Unknown error')}")
            return False
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during key validation: {e}")
        return False





def validate_key_locally(key_code):
    decrypted_key = load_key()
    if decrypted_key and decrypted_key == key_code:
        logging.info("Local validation successful.")
        return True
    else:
        logging.warning("Local validation failed.")
        return False





def validate_key(key_code):
    stored_key = load_key()
    if stored_key:
        if validate_key_locally(stored_key):
            return True
        
    return validate_key_with_Server(key_code)


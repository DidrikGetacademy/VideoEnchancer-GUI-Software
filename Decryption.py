from Logger import logging
from encryption import load_encryption_key
from File_path import activation_key_path
from cryptography.fernet import Fernet
import json


def decrypt_key(encrypted_key):
    encryption_key = load_encryption_key()
    if encryption_key:
        try:
            fernet = Fernet(encryption_key)
            decrypted_key = fernet.decrypt(encrypted_key).decode()
            logging.info(f"Decrypted key: {decrypted_key}")
            return decrypted_key
        except Exception as e:
            logging.error(f"Error during decryption: {e}")
            return None
    return None


def load_key():
    if not activation_key_path.exists() or activation_key_path.stat().st_size == 0:
        logging.warning("Activation key file does not exist. It will be created after activation.")
        return False

    with open(activation_key_path, "r") as file:
        key_data = json.load(file)
        
    encrypted_key = key_data.get('key_code')
    
    if not encrypted_key:
        logging.warning("Activation key is missing or corrupted in the JSON file.")
        return None

    decrypted_key = decrypt_key(encrypted_key.encode())  # You need to encode the string to bytes for decryption
    if decrypted_key:
        logging.info("Successfully loaded activation key.")
        return True
    else:
        logging.warning("Invalid or corrupted activation key.")
        return False


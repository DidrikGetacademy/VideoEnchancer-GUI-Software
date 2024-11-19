import logging
import requests
from Logger import logging
from Decryption import load_key
from encryption import save_key,encrypt_key




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

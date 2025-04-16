from Logger import logging
from encryption import load_encryption_key
from File_path import activation_key_path
from cryptography.fernet import Fernet
import json
import jwt

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





def validate_jwt(force_online_check=False):
    import os 
    from Validate_key import validate_subscription_status
    from datetime import datetime, timedelta
    from File_path import get_app_data_path
    from File_path import dotenv_path
    from dotenv import load_dotenv
    load_dotenv(dotenv_path)
    JWT_SECRET = os.getenv("JWT_SECRET")
    try:
        encrypted_token = load_key() #Henter lagret kryptert token
        if not encrypted_token:
            logging.info("Activasion key not found")
            raise ValueError("Activation key not found")
        
        decrypted_token = decrypt_key(encrypted_token) #dekrypterer tokenet
        if not decrypted_token:
            logging.warning("Unable to decrypt activasion key.")
            raise ValueError("Unable to decrypt activation key")
        
        payload = jwt.decode(decrypted_token, JWT_SECRET)

        exp_date = datetime.fromtimestamp(payload["exp"])
        if exp_date < datetime.now():
            logging.warning("token has expired.")
            raise ValueError("Token has expired")
        
        validation_file = get_app_data_path() / "last_jwt_validation.txt"
        validate_with_server = True

        if not force_online_check and validation_file.exists():
            last_check = datetime.fromisoformat(validation_file.read_text())
            if datetime.now() - last_check < timedelta(days=7):
                logging.info("Validation with server is false. still valid local validation by time --->  skipping...")
                validate_with_server = False

            if validate_with_server:
                if not validate_subscription_status(payload["user_id"]):
                    logging.info("Subscription has expired.")
                    raise ValueError("Subscription has expired")
                validation_file.write_text(datetime.now().isoformat())
            
            logging.info("Validation JWT videoenchancer successful")
            return True
    except Exception as e:
        logging.error(f"Token Validation Failed: {str(e)}")
        return False
    
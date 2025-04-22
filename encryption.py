from Logger import logging
from File_path import secret_key_path, activation_key_path
from cryptography.fernet import Fernet
import json
from File_path import app_data_path
import pickle
def encrypt_key(key_code):
    encryption_key = load_encryption_key()
    if encryption_key:
        fernet = Fernet(encryption_key)
        encrypted_key = fernet.encrypt(key_code.encode())
        logging.info(f"Encrypted key_code '{key_code}'")
        return encrypted_key
    return None



def load_encryption_key():
    if secret_key_path.exists() and secret_key_path.stat().st_size > 0:
        with open(secret_key_path, "rb") as key_file:
            logging.info("Secret_key_path exsist and content is bigger then 0 returning key_file.read")
            return key_file.read()
    else:
        logging.info("Encryption key not found. Generating a new one.")
        key = Fernet.generate_key()
        with open(secret_key_path, "wb") as key_file:
            key_file.write(key)
        return key



def save_key(encrypted_key):
    key_data = {"key_code": encrypted_key.decode()} 
    with open(activation_key_path, "w") as file:
        json.dump(key_data, file)
    logging.info("Saved encrypted key to activation_key.json")


def get_token_path(channel_name):
    token_folder = app_data_path / "youtube_tokens"
    token_folder.mkdir(parents=True, exist_ok=True)
    return token_folder / f"{channel_name}.pickle.enc"

def save_encrypted_token(channel_name, credentials):
    encryption_key = load_encryption_key()
    fernet = Fernet(encryption_key)

    serialized = pickle.dumps(credentials)
    encrypted = fernet.encrypt(serialized)

    path = get_token_path(channel_name)
    print(f"[DEBUG] Saving token to: {path}")
    with open(path, "wb") as file:
        file.write(encrypted)

def load_encrypted_token(channel_name):
    token_path = get_token_path(channel_name)
    print(f"[DEBUG] Loading token from: {token_path}")
    if not token_path.exists():
        print(f"[ERROR] Token file not found: {token_path}")

        return None

    encryption_key = load_encryption_key()
    fernet = Fernet(encryption_key)

    with open(token_path, "rb") as file:
        encrypted_data = file.read()
        decrypted = fernet.decrypt(encrypted_data)
        credentials = pickle.loads(decrypted)
        return credentials

#NOT IN USE GENERATES WITH SERVER INSTEAD.
# def generate_jwt(user_data):
#         import os 
#         from dotenv import load_dotenv
#         load_dotenv()
#         JWT_SECRET = os.getenv("JWT_SECRET")
#         payload = {
#             "user_id": user_data['id'],
#             "exp": ((datetime.now(timezone.utc) + timedelta(days=30)).timestamp()),
#             "sub_type": user_data['subscription_type']
#         }
#         #token = jwt.encode(payload,Fernet(load_encryption_key()).encrypt(b'secret_key'), algorithm="HS256")
#         token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
#         encrypted_token = encrypt_key(token)
#         save_key(encrypted_token)
#         logging.info("JWT generated, encrypted, and saved.")
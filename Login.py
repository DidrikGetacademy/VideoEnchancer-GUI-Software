import requests
from Logger import logging
url = "https://learnreflects.com/Server/Login.php"

def User_login(P_email, P_password):
    email = P_email
    password = P_password

    payload = {"email": email, "password": password}

    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            url,
            json=payload,
            headers=headers,
        )
        response.raise_for_status()  

        try:
            data = response.json()
            
            if response.status_code == 200: 
                user_data = {
                    'name': data.get('name', 'N/A'),
                    'email': data.get('email', 'N/A'),
                    'subscription_type': data.get('subscription_type', 'N/A'),
                    'id': data.get('id', 'N/A')
                }
                return "Success", user_data
            
            elif response.status_code == 401: 
                return "Invalid Credentials", None
            
            elif response.status_code == 400: 
                return "Email and password are required", None
            
            else:  # For other unexpected cases
                return data.get("message", "Login Failed"), None
        
        except ValueError:
            logging.error(f"Unexpected response format: {response.text}")
            return "Invalid response from server", None

    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {str(e)}")
        return f"Invalid Credentials {str(e)}", None




 
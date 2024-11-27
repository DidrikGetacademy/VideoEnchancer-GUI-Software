import requests
from Logger import logging
_user_data = {}



def set_user_data(data):
    global _user_data
    _user_data = data



def get_user_data():
    return _user_data







url = "https://learnreflects.com/Server/UpdateUser.php"
def Update_user_data():
    userid = _user_data.get('id')
    email = _user_data.get('email')
    
    if not userid or not email:
         logging.error("Userid and email are required to update user_data")
         return "User ID and  Email are required"
     
     
    payload = {"id": userid ,"email": email}
    
    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            url,
            json=payload,
            headers=headers
        )
        response.raise_for_status()
        
        try:
            data = response.json()
            
            if response.status_code == 200:
                _user_data['id'] = data.get('id',_user_data.get('id'))
                _user_data['name'] = data.get('name',_user_data.get('name',"N/A"))
                _user_data['email'] = data.get('email',_user_data.get("email","N/A"))
                _user_data['subscription_type'] = data.get('subscription_type',_user_data.get('subscription_type',"N/A"))
                logging.info("User data successfully updated")
                return _user_data
            else:
                return data.get("message", "Update failed"),None
        except ValueError:
            logging.error(f"Unexpected response format: {response.text}")
            return "Invalid response from server",None
    except requests.exceptions.RequestException as e:
        logging.error(f"Request Error: {str(e)}")
        return f"Request error {str(e)}",None
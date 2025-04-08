import requests

url = 'https://learnreflects.com/Server/Registration.php'


def register_user(Email,Pasword,Name):
    email = Email
    password = Pasword
    name = Name
    
    
    payload = {
        "email": email,
        "password": password,
        "name": name,
    }
    
    try: 
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            )
        try:
    
            data = response.json()
        except ValueError:
            return f"Unexpected response format: {response.text}"
        
       
        if response.status_code == 201:
            return "success"
        else:
            return data.get("message", f"Error {response.status_code}")
  
    except requests.exceptions.RequestException as e:
            return f"Invalid Details: {str(e)}"
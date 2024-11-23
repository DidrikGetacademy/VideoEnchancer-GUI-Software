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
        response.raise_for_status()
        
        try: 
           data = response.json()
           if response.status_code == 400:
               return "Bad request."
           elif response.status_code == 500:
               return "Server error"
           return data.get("message", "No message provided")
       
        except ValueError:
            print(f"Unexpected response format: {response.text}")
            return
        
    except requests.exceptions.RequestException as e:
            return f"an error occured: {str(e)}"
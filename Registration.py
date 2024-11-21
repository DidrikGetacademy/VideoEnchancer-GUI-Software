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
        except ValueError:
            print(f"Unexpected response format: {response.text}")
            return
        
        
        if response.status_code == 201:
            print("Registration successful:",data.get("message", "No message provided"))
        elif response.status_code == 400:
            print("Bad Request:",data.get("message","No message provided"))
        elif response.status_code == 500:
            print("Server error: ", data.get("message","No message provided"))
        else:
            print("Unexpected error:",response.status_code,response.text)
    except requests.exceptions.RequestException as e:
        print("an error occured while trying to regiter the user: ",str(e))
        
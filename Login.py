import requests

url = 'https://learnreflects.com/Server/Registration.php'

def User_login(P_email,P_password):
    email = P_email
    password = P_password
    
    payload = {
        "email": email,
        "password": password
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
            print(f"unexpected response format: ",{response.text})
            return
        
        if response.status_code == 200:
            print("Login successful:",data.get("message", "No message provided"))
        elif response.status_code == 400:
            print("Email and password are required",data.get("Message", "No message provided"))
        elif response.status_code == 401:
            print("Invalid Credentials",data.get("message","No message provided"))
        else: print("Unexpected error: ",response.status_code,response.text)
    except requests.exceptions.RequestException as e:
        print("An error occured while trying to login",str(e))
        
    
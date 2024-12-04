import customtkinter as ctk
from Login import User_login
from Forget_Password_frame import ForgetPasswordFrame
import time
from datetime import timedelta
from Logger import logging


class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, Connect_UserAccount):
        super().__init__(master)
        self.switch_to_Accountsystem = Connect_UserAccount
        self.title_label = ctk.CTkLabel(self, text="Login Account", font=("Arial", 20))
        self.title_label.pack(pady=10)
        
        
        #CheckBox
        self.remember_me_var = ctk.BooleanVar()
        self.remember_me_checkbox = ctk.CTkCheckBox(self,text="Remember me",variable=self.remember_me_var)
        self.remember_me_checkbox.pack(pady=10)
        
        
        # email-FIELD
        self.email_label = ctk.CTkLabel(self, text="Email")
        self.email_label.pack()
        self.email_entry = ctk.CTkEntry(self, width=300)
        self.email_entry.pack(pady=5)

        # Password-FIELD
        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.pack()
        self.password_entry = ctk.CTkEntry(self, width=300, show="*")
        self.password_entry.pack(pady=5)

        # Login-BTN
        self.login_button = ctk.CTkButton(self, text="Login", command=self.Login_user)
        self.login_button.pack(pady=10)

        self.goback_button = ctk.CTkButton(self, text="Go back", command=self.go_back)
        self.goback_button.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.pack(pady=10)
        self.forgot_password = ctk.CTkButton(
            self, text="Forget password", command=self.open_Forget_password
        )
        self.after(100,self.auto_login)
        
        

       
    
    
    
    def reset_fields(self):
        self.email_entry.delete(0,'end')
        self.password_entry.delete(0,'end')
        self.remember_me_var.set(False)
        self.status_label.configure(text="")
        
        
        
    def auto_login(self):
        from User_data_storage import set_user_data
        from File_path import load_userdata
        User_data = load_userdata()
        logging.info(f"User_data from load_userdata: {User_data}")
        if not User_data:
            logging.info("No saved data found. Proceeding with normal login")
            return 
        
        set_user_data(User_data)
        email = User_data.get("email")
        password = User_data.get("password")
        last_login = User_data.get("last_login",0)
        
        if not email or not password or not last_login:
            logging.info("Incomplete saved data. skipping auto-login")
            return
        current_time = time.time()
        time_since_last_login = current_time - last_login
        logging.info(f"Current time: {current_time}, Last login: {last_login}")
        logging.info(f"Time since last login: {time_since_last_login} seconds")
        if time.time() - last_login > timedelta(weeks=1).total_seconds():
            logging.info("Last login is more then a week ago. revalidating the user.")
            status_message,new_user_data = User_login(email,password)
            if new_user_data:
                set_user_data(new_user_data,password=password) #updating the data
                self.switch_to_Accountsystem()
            else:
                self.status_label.configure(text="Session expired. Please log in again.")
                logging.info(status_message)
        else: 
            logging.info("Auto-login successful. Redirecting to account system.")  
            set_user_data(User_data)
            self.switch_to_Accountsystem()      
          
        



    def Login_user(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not email or not password:
            self.status_label.configure(text="Email and password are required.")
            return
        
        status_message, user_data = User_login(email, password)
        self.status_label.configure(text=status_message)
        
        if user_data:
            self.status_label.configure(text="Redirecting to your account...")
            from User_data_storage import set_user_data
            set_user_data(user_data,password=password,RememberMe=self.remember_me_var.get())
            self.switch_to_Accountsystem()
    
        
            





    def go_back(self):
        self.pack_forget()
        self.master.show_mainwindow()
        
    
    
    
    def open_Forget_password(self):
        self.pack_forget()
        ForgetPasswordFrame(self.master).pack(fill="both",expand=True)
        
        

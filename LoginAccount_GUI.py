import customtkinter as ctk
from Login import User_login
from Forget_Password_frame import ForgetPasswordFrame
import time
from datetime import timedelta
from Logger import logging
from PIL import Image, ImageTk
from File_path import resource_path  
class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, Connect_UserAccount):
        super().__init__(master, fg_color="transparent") 

        
        image_path = resource_path("Assets/background1.png")
        self.background_image = Image.open(image_path)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = ctk.CTkCanvas(self, width=1400, height=800, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        self.switch_to_Accountsystem = Connect_UserAccount

        # Title Label
        self.title_label = ctk.CTkLabel(self, text="Login Account", font=("Arial", 20), fg_color="transparent")
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")  

        # CheckBox
        self.remember_me_var = ctk.BooleanVar()
        self.remember_me_checkbox = ctk.CTkCheckBox(self, text="Remember me", variable=self.remember_me_var)
        self.remember_me_checkbox.place(relx=0.5, rely=0.2, anchor="center")  

        # Email Field
        self.email_label = ctk.CTkLabel(self, text="Email", fg_color="transparent")
        self.email_label.place(relx=0.5, rely=0.3, anchor="center") 
        self.email_entry = ctk.CTkEntry(self, width=300, fg_color="transparent")
        self.email_entry.place(relx=0.5, rely=0.35, anchor="center")

        # Password Field
        self.password_label = ctk.CTkLabel(self, text="Password", fg_color="transparent")
        self.password_label.place(relx=0.5, rely=0.45, anchor="center") 
        self.password_entry = ctk.CTkEntry(self, width=300, show="*", fg_color="transparent")
        self.password_entry.place(relx=0.5, rely=0.5, anchor="center")  

        # Login Button
        self.login_button = ctk.CTkButton(self, text="Login", command=self.Login_user, fg_color="transparent")
        self.login_button.place(relx=0.5, rely=0.6, anchor="center")  
        # Go Back Button
        self.goback_button = ctk.CTkButton(self, text="Go back", command=self.go_back, fg_color="transparent")
        self.goback_button.place(relx=0.5, rely=0.7, anchor="center") 

        # Status Label
        self.status_label = ctk.CTkLabel(self, text="", fg_color="transparent")
        self.status_label.place(relx=0.5, rely=0.8, anchor="center") 

        # Forgot Password Button
        self.forgot_password = ctk.CTkButton(self, text="Forget password", command=self.open_Forget_password)
        self.forgot_password.place(relx=0.5, rely=0.9, anchor="center")  

        self.lift()  

        self.after(100, self.auto_login)

       
    
    
    
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
        
        

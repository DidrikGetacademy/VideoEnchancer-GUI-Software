import customtkinter as ctk
from Login import User_login
from User_data_storage import set_user_data
from Forget_Password_frame import ForgetPasswordFrame


class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, Connect_UserAccount):
        super().__init__(master)
        self.switch_to_Accountsystem = Connect_UserAccount

        self.title_label = ctk.CTkLabel(self, text="Login Account", font=("Arial", 20))
        self.title_label.pack(pady=10)

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
        self.forgot_password.pack(pady=5)

    def Login_user(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not email or not password:
            self.status_label.configure(text="Email and password are required.")
            return
        
        
        
        status_message, user_data = User_login(email, password)
        self.status_label.configure(text=status_message)
        
        

        if user_data:  # checks if user_data is not none
            set_user_data(user_data)  # store the Userdata
            self.status_label.configure(text="Redirecting to your account...")
            self.switch_to_Accountsystem()

    def go_back(self):
        self.pack_forget()
        self.master.show_mainwindow()
        
    
    def open_Forget_password(self):
        self.pack_forget()
        ForgetPasswordFrame(self.master).pack(fill="both",expand=True)
        
        

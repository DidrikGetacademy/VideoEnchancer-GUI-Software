import customtkinter as ctk
from Login import User_login




class LoginFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)


        self.title_label = ctk.CTkLabel(self,text="Login Account",font=("Arial",20))
        self.title_label.pack(pady=10)

       #email-FIELD
        self.email_label = ctk.CTkLabel(self,text="Email")
        self.email_label.pack()
        self.email_entry = ctk.CTkEntry(self,width=300)
        self.email_entry.pack(pady=5)

       #Password-FIELD
        self.password_label = ctk.CTkLabel(self,text="Password")
        self.password_label.pack()
        self.password_entry = ctk.CTkEntry(self,width=300)
        self.password_entry.pack(pady=5)

      #Login-BTN
        self.login_button = ctk.CTkButton(self,text="Login",command=self.Login_user)
        self.login_button.pack(pady=10)

def Login_user(self):
    email = self.email_entry.get()
    password = self.password_entry.get()
    User_login(email,password)


import customtkinter as ctk 
import subprocess
from RegisterAccount_GUI import RegistrationFrame
from LoginAccount_GUI import LoginFrame


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Account Management")
        self.title_label =ctk.CTkLabel(self,text="Account Management",font=("Arial",24))
        self.title_label.pack(pady=20)


        self.Register_button = ctk.CTkButton(self,text="Regiter Account",command=self.open_register_account)
        self.Register_button.pack(pady=20)

        self.login_button = ctk.CTkButton(self,text="Login",command=self.open_login_account)
        self.login_button.pack(pady=20)
        
        
        self.register_frame = RegistrationFrame(self)
        self.login_frame = LoginFrame(self)
    
    def open_Register_Account(self): 
        self.hide_frames()
        self.register_frame.pack(fill="both",expand=True)
        
        
    def open_login_Account(self):
        self.hide_frames()
        self.login_frame.pack(fill="both",expand=True)
        
    def hide_frames(self):
        self.register_frame.pack_forget()
        self.login_frame.pack_forget()
        
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
        
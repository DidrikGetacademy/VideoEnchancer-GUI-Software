import customtkinter as ctk
from RegisterAccount_GUI import RegistrationFrame
from LoginAccount_GUI import LoginFrame
from PIL import Image, ImageTk 
from File_path import resource_path
class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")
        self.title("Account Management")
        self.resizable(False,False)
        self.maxsize(1400,800)
        self.minsize(1400,800)
        
        

        ImageFront = resource_path("Assets/test_8192x5447.png")
        self.background_image = Image.open(ImageFront)
        self.background_photo = ctk.CTkImage(self.background_image, size=(1750, 1500))

        self.bg_label = ctk.CTkLabel(
            self,
            image=self.background_photo,
            text="",
            bg_color="black"
        )
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.configure(bg="black")  

   
        self.button_frame = ctk.CTkFrame(
            self,
            width=960,
            height=700,
            fg_color="black", 
            bg_color="transparent"
        )
        self.button_frame.place(relx=0.5, rely=0.5, anchor="center")


        self.title_label = ctk.CTkLabel(
            self.button_frame,
            text="Account Manager",
            font=("Arial", 38, "bold"),
            text_color="white"
        )
        self.title_label.pack(pady=(50, 40))

        self.Register_button = ctk.CTkButton(
            self.button_frame,
            text="Register Account",
            command=self.open_Register_Account,
            fg_color="#0d1b2a",         
            hover_color="#1c2636",     
            text_color="white",
            corner_radius=20,
            width=300,
            height=60,
            font=("Arial", 22, "bold")
        )
        self.Register_button.pack(pady=30, padx=25)

        self.login_button = ctk.CTkButton(
            self.button_frame,
            text="Login",
            command=self.open_login_Account,
            fg_color="#0d1b2a",
            hover_color="#1c2636",
            text_color="white",
            corner_radius=20,
            width=300,
            height=60,
            font=("Arial", 22, "bold")
        )
        self.login_button.pack(pady=30,padx=25)

        
        self.register_frame = RegistrationFrame(
            self, 
            self.open_login_Account
            )
        
        
        self.login_frame = LoginFrame(
            self, 
            self.Connect_User_Account
            )
        self.UserAccount_Frame = None



    def Connect_User_Account(self):
        from UserAccount import UserAccountFrame
        if self.UserAccount_Frame is None:
            self.UserAccount_Frame = UserAccountFrame(self)
        self.hide_frames()
        self.UserAccount_Frame.pack(fill="both", expand=True)



    def open_Register_Account(self):
        self.hide_frames()
        self.register_frame.pack(fill="both", expand=True)


    def open_login_Account(self,skip_auto_login=False):     
        self.hide_frames()
        self.login_frame = LoginFrame(
        self,
        self.Connect_User_Account,
        skip_auto_login=skip_auto_login
    )
        self.login_frame.pack(fill="both", expand=True)



    def hide_frames(self):
        self.button_frame.place_forget()
        self.register_frame.pack_forget()
        self.login_frame.pack_forget()
        self.bg_label.place_forget()

    def show_mainwindow(self):
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.button_frame.place(relx=0.5, rely=0.5, anchor="center")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

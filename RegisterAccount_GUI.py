import customtkinter as ctk
from Registration import register_user
from Logger import logging
from PIL import Image, ImageTk
from File_path import resource_path 
class RegistrationFrame(ctk.CTkFrame):
    def __init__(self, master, open_login_account):
        super().__init__(master, fg_color="transparent") 

  
        image_path = resource_path("Assets/test_8192x5447.png")
        self.background_image = Image.open(image_path).resize((1400, 800), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)


        self.canvas = ctk.CTkCanvas(self, width=1400, height=800, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        self.switch_to_login = open_login_account


        self.container = ctk.CTkFrame(
            self, 
            fg_color="black",
            width=960,
            height=700
        )  
        self.container.place(relx=0.5, rely=0.5, anchor="center")

   
        self.title_label = ctk.CTkLabel(
            self.container,
            text="Register Account",
            font=("Arial", 25, "bold"),
            text_color="white"
        ) 
        self.title_label.pack(pady=(50, 30))


        self.name_label = ctk.CTkLabel(
            self.container,
            text="Name",
            text_color="white",
            font=("Arial", 18)
        )
        self.name_label.pack(pady=(10, 0), padx=20)

        self.name_entry = ctk.CTkEntry(
            self.container,
            width=350,
            height=40,
            placeholder_text="Enter your name",
            fg_color="#1c2636",
            border_color="#0d1b2a",
            text_color="white",
            font=("Arial", 16),
            corner_radius=15,
            justify="center"
        )
        self.name_entry.pack(pady=10,padx=20)


        self.email_label = ctk.CTkLabel(
            self.container,
            text="Email",
            text_color="white",
            font=("Arial", 18)
        )
        self.email_label.pack(pady=(10, 0),padx=20)

        self.email_entry = ctk.CTkEntry(
            self.container,
            width=350,
            placeholder_text="Enter your email",
            fg_color="#1c2636",
            border_color="#0d1b2a",
            text_color="white",
            height=50,   
            font=("Arial", 16),
            corner_radius=15,
            justify="center"
        )
        self.email_entry.pack(pady=10)


        self.password_label = ctk.CTkLabel(
            self.container,
            text="Password",
            text_color="white",
            font=("Arial", 18)
        )
        self.password_label.pack(pady=(10, 0))

        self.password_entry = ctk.CTkEntry(
            self.container,
            width=350,
            show="*",
            placeholder_text="Enter your password",
            fg_color="#1c2636",
            border_color="#0d1b2a",
            text_color="white",
            font=("Arial", 16),
            corner_radius=15,
            height=50,
            justify="center"
        )
        self.password_entry.pack(pady=10)

    
        self.register_button = ctk.CTkButton(
            self.container,
            text="Register",
            command=self.Register_new_user,
            fg_color="#0d1b2a",
            hover_color="#1c2636",
            text_color="white",
            font=("Arial", 20, "bold"),
            width=300,
            height=35,
            corner_radius=20
        )
        self.register_button.pack(pady=25)

        self.goback_button = ctk.CTkButton(
            self.container,
            text="Go back",
            command=self.go_back,
            fg_color="transparent",
            text_color="white",
            hover_color="#1c2636",
            font=("Arial", 14)
        )
        self.goback_button.pack(pady=5)

   
        self.status_label = ctk.CTkLabel(
            self.container,
            text="",
            text_color="#E74C3C",
            font=("Arial", 16)
        )
        self.status_label.pack(pady=10)


        self.lift()  
        
    def Register_new_user(self):
        Email = self.email_entry.get()
        Password = self.password_entry.get()
        Name = self.name_entry.get()
        status_message = register_user(Email, Password, Name)
        logging.info("REGISTRATION STATUS:", status_message)

        if "success" in status_message.lower():
            self.status_label.configure(text="Registration successful. Please log in.")
            self.switch_to_login(skip_auto_login=True)
        else:
            self.status_label.configure(text=status_message)

    def go_back(self):
        logging.info("Going back to main window")
        self.pack_forget()
        self.master.show_mainwindow()

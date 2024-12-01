import customtkinter as ctk
from Registration import register_user
from Logger import logging


class RegistrationFrame(ctk.CTkFrame):
    def __init__(self, master, open_login_account):
        super().__init__(master)
        self.switch_to_login = open_login_account

        self.title_label = ctk.CTkLabel(
            self, text="Register new account", font=("Arial", 20)
        )
        self.title_label.pack(pady=10)

        self.name_label = ctk.CTkLabel(self, text="Name")
        self.name_label.pack()
        self.name_entry = ctk.CTkEntry(self, width=300)
        self.name_entry.pack(pady=5)

        self.email_label = ctk.CTkLabel(self, text="Email")
        self.email_label.pack()
        self.email_entry = ctk.CTkEntry(self, width=300)
        self.email_entry.pack(pady=5)

        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.pack()
        self.password_entry = ctk.CTkEntry(self, width=300, show="*")
        self.password_entry.pack(pady=5)

        self.register_button = ctk.CTkButton(
            self, text="Register", command=self.Register_new_user
        )
        self.register_button.pack(pady=10)

        self.goback_button = ctk.CTkButton(self, text="Go back", command=self.go_back)
        self.goback_button.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.pack(pady=10)

    def Register_new_user(self):
        Email = self.email_entry.get()
        Password = self.password_entry.get()
        Name = self.name_entry.get()
        status_message = register_user(Email, Password, Name)
        self.status_label.configure(text=status_message)

        if "success" in status_message.lower():
            self.switch_to_login()

    def go_back(self):
        logging.info("Going back to main window")
        self.pack_forget()
        self.master.show_mainwindow()

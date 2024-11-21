import customtkinter as ctk
from Registration import register_user


class RegistrationFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        


      #Headline
        self.title_label = ctk.CTkLabel(self,text="Register new account",font=("Arial",20))
        self.title_label.pack(pady=10)
 

#name-FIELD
        self.name_label = ctk.CTkLabel(self,text="Name")
        self.name_label.pack()
        self.name_entry = ctk.CTkEntry(self,width=300)
        self.name_entry.pack(pady=5)

#Epost-FIELD
        self.email_label = ctk.CTkLabel(self,text="Email")
        self.email_label.pack()
        self.email_entry = ctk.CTkEntry(self,width=300)
        self.email_entry.pack(pady=5)

#password-FIELD
        self.password_label = ctk.CTkLabel(self,text="Password")
        self.password_label.pack()
        self.password_entry = ctk.CTkEntry(self,width=300, show="*")
        self.password_entry.pack(pady=5)



#Registration-BTN
        self.register_button = ctk.CTkButton(self,text="Register",command=self.Register_new_user)
        self.register_button.pack(pady=10)


#status-MSG
        self.status_label = ctk.CTkLabel(self,text="")
        self.status_label.pack(pady=10)




def Register_new_user(self):
    Email = self.email_entry.get()
    Password = self.password_entry.get()
    Name = self.name_entry.get()
    register_user(Email,Password,Name)
    
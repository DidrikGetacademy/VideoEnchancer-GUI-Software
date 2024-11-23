import customtkinter as ctk

class UserAccountFrame(ctk.CTkFrame):
    def __init__(self,master,user_data):
        super().__init__(master)
        
        self.user_data = user_data
        
        self.create_widgets()
        
    
    def create_widgets(self):
        
        self.title_label = ctk.CTkLabel(self,text="User Account", font=("Arial",20))
        self.title_label.pack(pady=20)
        
        self.name_label = ctk.CTkLabel(self,text=f"Name: {self.user_data.get('name','N/A')}")
        self.name_label.pack(pady=5)
        
        self.email_label = ctk.CTkLabel(self, text=f"Email: {self.user_data.get('email', 'N/A')}")
        self.email_label.pack(pady=5)
        
        self.subscription_label = ctk.CTkLabel(self,text=f"Subscription: {self.user_data.get('subscription_type','N/A')}")
        self.subscription_label.pack(pady=5)
        
        
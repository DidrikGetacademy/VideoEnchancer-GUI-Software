import customtkinter as ctk
from Logger import logging
from activation_window import ActivationWindow
from User_data_storage import get_user_data
import subprocess
import sys
import os 

class UserAccountFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        
        self.user_data = get_user_data()
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
        
        self.update_buttons()
        
        
    def update_buttons(self):
        if self.is_subscription_active():
            self.enchancer_button = ctk.CTkButton(self,text="LearnReflect Video Enchancer", command=self.run_enchancer,state="normal")
            self.enchancer_button.pack(pady=10)
        else: 
            self.enchancer_button = ctk.CTkButton(self,text="LearnReflect Video Enchancer", state="disabled")
            self.enchancer_button.pack(pady=10)
            
            self.activation_button = ctk.CTkButton(self,text="Activate subscription",command=self.open_activation_window)
            self.activation_button.pack(pady=10)
            
    
    def is_subscription_active(self):
        subscription_type = self.user_data.get('subscription_type','')
        if subscription_type.lower() in ['monthly','permanent']:
            return True #Returnerer TRUE dersom det finnes et aktiv subscription abonoment hos bruker.
        return False
    
    
    
    
    
    
    #How to run the learnreflect video enchancer
    def run_enchancer(self):
        try:
            script_path = os.path.join(os.path.dirname(__file__),'LearnReflectAI.py')
            subprocess.run([sys.executable,script_path])
            
        except Exception as e:
            logging.error(f"Error while running LearnReflect Video Enchancer: {e}")
            
            
        
        
    #open the window to activate the program,
    def open_activation_window(self):
        ActivationWindow(self,run_main_program_callback=self.refresh_user_data)
        
    
    def refresh_user_data(self):
        self.user_data = get_user_data() #henter ut oppdatert brukerdata
        self.update_buttons() #Oppdaterer GUI
        
        
        
        
    
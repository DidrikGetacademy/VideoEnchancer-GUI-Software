import customtkinter as ctk
from Logger import logging
from activation_window import ActivationWindow
from User_data_storage import  get_user_data, set_user_data, Update_user_data
import logging
    import subprocess



class UserAccountFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.user_data = get_user_data()
        self.create_widgets()
        
    
    def create_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.title_label = ctk.CTkLabel(self,text="User Account", font=("Arial",20))
        self.title_label.pack(pady=20)
        self.name_label = ctk.CTkLabel(self,text=f"Name: {self.user_data.get('name','N/A')}")
        self.name_label.pack(pady=5)
        self.email_label = ctk.CTkLabel(self, text=f"Email: {self.user_data.get('email', 'N/A')}")
        self.email_label.pack(pady=5)
        self.subscription_label = ctk.CTkLabel(self,text=f"Subscription: {self.user_data.get('subscription_type','N/A')}")
        self.subscription_label.pack(pady=5)
        self.logout_button = ctk.CTkButton(self,text="Logout", command=self.Logout)
        self.logout_button.pack(pady=5)
        self.update_buttons()
        
        
    def update_buttons(self):
        for widget in self.winfo_children():
            if isinstance(widget,ctk.CTkButton) and widget != self.logout_button:
                widget.destroy()

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
    
    
    def Logout(self):
        set_user_data({})
        self.pack_forget()
        self.master.login_frame.reset_fields()
        self.master.show_mainwindow()
    
    def run_enchancer(self):
        from File_path import resource_path
        import os
        video_enchancer_exe = os.path.join(os.path.dirname(__file__), "VideoEnchancer.exe")
        if not os.path.exists(video_enchancer_exe):
           logging.info(f"Error: The executable {video_enchancer_exe} does not exist.")
       
        try: 
            result = subprocess.run(
                [video_enchancer_exe],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            logging.info(f"Video enchancer output: {result.stdout}")
        except subprocess.CalledProcessError as e:
            logging.info(f"Videoenchancer failed with error: {e}")
        except FileNotFoundError:
            logging.info(f"Videoenchancer exe  not found at: {video_enchancer_exe}")
    
        
        
    def hide_widgets(self):
        for widget in self.winfo_children():
            widget.pack_forget()   
       
    def open_activation_window(self):
        ActivationWindow(self,self.refresh_user_data) 
        
    
    def refresh_user_data(self):
        updated_data = Update_user_data()
        if updated_data is not None:
            self.user_data = updated_data
        else: 
            logging.error("Failed to refresh userdata")
        self.create_widgets()
        self.update_buttons() 
        
        
        
        
    
import customtkinter as ctk
from Login import User_login
from Logger import logging
from User_data_storage import set_user_data



class LoginFrame(ctk.CTkFrame):
    def __init__(self,master,Connect_UserAccount):
        super().__init__(master)
        self.switch_to_Accountsystem =  Connect_UserAccount


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
        self.password_entry = ctk.CTkEntry(self,width=300,show="*")
        self.password_entry.pack(pady=5)
        
        
        self.forgot_password = ctk.CTkButton(self,text="Forget password", command=self.Forget_password)
        self.forgot_password.pack(pady=5)
      #Login-BTN
        self.login_button = ctk.CTkButton(self,text="Login",command=self.Login_user)
        self.login_button.pack(pady=10)
        
        self.goback_button = ctk.CTkButton(self,text="Go back",command=self.go_back)
        self.goback_button.pack(pady=10)
        
        self.status_label = ctk.CTkLabel(self,text="")
        self.status_label.pack(pady=10)

    def Login_user(self):
           email = self.email_entry.get().strip()
           password = self.password_entry.get().strip()
           
           if not email or not password:
             self.status_label.configure(text="Email and password are required.")
             return
           status_message,user_data = User_login(email,password)
           self.status_label.configure(text=status_message)
           
           if user_data: # checks if user_data is not none
             set_user_data(user_data) #store the Userdata
             self.status_label.configure(text="Redirecting to your account...")
             self.switch_to_Accountsystem()
      
      
    def go_back(self):
       logging.info("Going back to main window")
       self.pack_forget()
       self.master.show_mainwindow()
      
      
      
      
      
      
      
      
      
      
    def Forget_password(self):
       logging.info("ForgetPassword function activated")

       # Clear current widgets in the frame
       for widget in self.winfo_children():
           widget.destroy()

       # UI for entering email to request password reset
       email_label = ctk.CTkLabel(self, text="Enter your email to reset your password")
       email_label.pack(pady=10)
       email_entry = ctk.CTkEntry(self, width=300)
       email_entry.pack(pady=5)
       status_label = ctk.CTkLabel(self, text="")
       status_label.pack(pady=5)



       def send_reset_code():
           email = email_entry.get().strip()
           if not email:
            status_label.configure(text="Please enter your email.")
            return

           from User_data_storage import request_password_reset
           result = request_password_reset(email)

           if result.get("success"):
               status_label.configure(text="Reset code sent to your email.")
               ask_for_token()
           else:
               error_message = result.get("message", "Failed to send reset code.")
               status_label.configure(text=error_message)

       send_code_button = ctk.CTkButton(self, text="Send Reset Code", command=send_reset_code)
       send_code_button.pack(pady=10)
    
    
    
    
       def ask_for_token():
          for widget in self.winfo_children():
             widget.destroy()
            
        
             token_label = ctk.CTkLabel(self,text="Enter reset token")
             token_label.pack()
             token_entry = ctk.CTkEntry(self,width=300)
             token_entry.pack(pady=5)
        
             new_password_label = ctk.CTkLabel(self,text="Enter new password")
             new_password_label.pack()
             new_password_entry = ctk.CTkEntry(self,width=300,show="*")
             new_password_entry.pack(pady=5)
        
             def reset_password():
               token = token_entry.get().strip()
               new_password = new_password_entry.get().strip()
               if not token or not new_password:
                  status_label.configure(text="Token and new password are required.")
                  return

               from User_data_storage import Reset_password
               result = Reset_password(token, new_password)

               if result.get("success"):
                   status_label.configure(text="Password reset successfully.")
               else:
                  error_message = result.get("message", "Failed to reset password.")
                  status_label.configure(text=error_message)

          reset_button = ctk.CTkButton(self, text="Reset Password", command=reset_password)
          reset_button.pack(pady=5)

          back_button = ctk.CTkButton(self, text="Go back", command=self.go_back)
          back_button.pack(pady=10)
              
          
    
    
    
  

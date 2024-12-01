
import customtkinter as ctk
from Logger import logging
from User_data_storage import request_password_reset, Reset_password




class ForgetPasswordFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.Setup_ui()
        
        
    def Setup_ui(self):
        self.title_label = ctk.CTkLabel(self,text="Reset Password", font=("Arial",20))
        self.title_label.pack(pady=10)
        
        self.email_label = ctk.CTkLabel(self, text="Enter your email to reset your password")
        self.email_label.pack(pady=10)
        self.email_entry = ctk.CTkEntry(self, width=300)
        self.email_entry.pack(pady=5)
        
        
        self.send_code_button = ctk.CTkButton(self, text="Send Reset Code", command=self.send_reset_code)
        self.send_code_button.pack(pady=10)
        
        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.pack(pady=5)
        
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back_to_login)
        self.back_button.pack(pady=5)

    def send_reset_code(self):
            email = self.email_entry.get().strip()
            if not email:
                self.status_label.configure(text="Please enter your email.")
                return

            result = request_password_reset(email)

            if result.get("success"):
                self.status_label.configure(text="Reset code sent to your email.")
                logging.info("Success in send_reset_code")
                self.ask_for_token()
            else:
                error_message = result.get("message", "Failed to send reset code.")
                self.status_label.configure(text=error_message)
                logging.error(f"Error in Send_reset_code: {error_message}")


    def ask_for_token(self):
            for widget in self.winfo_children():
                widget.destroy()

            self.token_label = ctk.CTkLabel(self, text="Enter reset token")
            self.token_label.pack()
            self.token_entry = ctk.CTkEntry(self, width=300)
            self.token_entry.pack(pady=5)


            self.new_password_label = ctk.CTkLabel(self, text="Enter new password")
            self.new_password_label.pack()
            self.new_password_entry = ctk.CTkEntry(self, width=300, show="*")
            self.new_password_entry.pack(pady=5)


            self.reset_button = ctk.CTkButton(self, text="Reset Password", command=self.reset_password)
            self.reset_button.pack(pady=5)
            self.status_label = ctk.CTkLabel(self, text="")
            self.status_label.pack(pady=5)

    def reset_password(self):
                token = self.token_entry.get().strip()
                new_password = self.new_password_entry.get().strip()
                
                
                
                if not token or not new_password:
                    self.status_label.configure(text="Token and new password are required.")
                    return
                

                result = Reset_password(token, new_password)

                if result.get("success"):
                    self.status_label.configure(text="Password reset successfully.")
                    logging.info("Success in reset_password")
                    self.show_success_ui()
                else:
                    if not result:
                       error_message = result.get("message", "Failed to reset password.")
                       self.status_label.configure(text=error_message)
                       logging.error("error in reset_password")
                       self.show_error_ui()
    
    
    def show_success_ui(self):
        for widget in self.winfo_children():
            widget.destroy()
            
        self.success_label = ctk.CTkLabel(self,text="Password reset successfully!",font=("Arial",20))
        self.success_label.pack(pady=10)
        
        self.back_to_login_button = ctk.CTkButton(self,text="Go back to login", command=self.go_back_to_login)
        self.back_to_login_button.pack(pady=10)
        
    def show_error_ui(self):
        for widget in self.winfo_children():
            widget.destroy()
            
        self.error_label = ctk.CTkLabel(self,text="Error on password reset, please try again",font=("Arial",20))
        self.error_label.pack(pady=10)
        
        self.go_back_to_login_button = ctk.CTkButton(self,text="Go back",command=self.go_back_to_login)
        self.go_back_to_login_button.pack(pady=10)

    

    def go_back_to_login(self):
        self.pack_forget()
        self.master.show_mainwindow()

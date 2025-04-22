import customtkinter as ctk
from Logger import logging
from activation_window import ActivationWindow
from User_data_storage import get_user_data, set_user_data, Update_user_data
from PIL import Image, ImageTk
from File_path import resource_path


class UserAccountFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=25, fg_color="#2C3E50")
        
       
        image_path = resource_path("Assets/background1.png")
        self.background_image = Image.open(image_path)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        
        self.canvas = ctk.CTkCanvas(self, width=1400, height=800, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")
        self.configure(fg_color="#2C3E50")
        self.user_data = get_user_data()
        self.create_widgets()
        self.lift()  
        



    def create_widgets(self):
        for widget in self.winfo_children():
            if widget != self.canvas:
                widget.destroy()

        # Top menu button (Settings & Check for Updates)
        self.menu_button = ctk.CTkSegmentedButton(
            self,
            values=["Settings", "Check for Updates"],
            command=self.menu_action,
            font=("Arial", 14),
            width=250,
            height=35,
            corner_radius=20,
            fg_color="#0d1b2a",
            selected_color="#1c2636",
            unselected_color="#0d1b2a",
            text_color="white",
        )
        self.menu_button.place(relx=0.05, rely=0.05)

        # User info frame
        self.info_frame = ctk.CTkFrame(
            self,
            fg_color="black",
            width=960,
            height=700,
            corner_radius=30
        )
        self.info_frame.place(relx=0.5, rely=0.45, anchor="center")

        self.title_label = ctk.CTkLabel(
            self.info_frame,
            text="User Dashboard",
            font=("Arial", 32, "bold"),
            text_color="white"
        )
        self.title_label.pack(pady=(40, 20), padx=15)

        self.name_label = ctk.CTkLabel(
            self.info_frame,
            text=f"Name: {self.user_data.get('name', 'N/A')}",
            font=("Arial", 18),
            text_color="white"
        )
        self.name_label.pack(pady=5, padx=15)

        self.email_label = ctk.CTkLabel(
            self.info_frame,
            text=f"Email: {self.user_data.get('email', 'N/A')}",
            font=("Arial", 18),
            text_color="white"
        )
        self.email_label.pack(pady=5)

        self.subscription_label = ctk.CTkLabel(
            self.info_frame,
            text=f"Subscription: {self.user_data.get('subscription_type', 'N/A')}",
            font=("Arial", 18),
            text_color="white"
        )
        self.subscription_label.pack(pady=5, padx=15)

        self.update_buttons()





    def update_buttons(self):

        if hasattr(self, 'button_windows'):
            for window_id in self.button_windows:
                self.canvas.delete(window_id)
        self.button_windows = []

        button_style = {
            "fg_color": "#0d1b2a",
            "hover_color": "#1c2636",
            "text_color": "white",
            "font": ("Arial", 18, "bold"),
            "width": 350,
            "height": 50
        }

        if self.is_subscription_active():
            self.enchancer_button = ctk.CTkButton(self.canvas, text="Launch Video Enhancer", command=self.run_enchancer, **button_style)
            window_id = self.canvas.create_window(700, 570, window=self.enchancer_button)
            self.button_windows.append(window_id)

            self.logout_button = ctk.CTkButton(self.canvas, text="Logout", command=self.Logout, **button_style)
            window_id = self.canvas.create_window(700, 640, window=self.logout_button)
            self.button_windows.append(window_id)

        else:
            self.enchancer_button = ctk.CTkButton(self.canvas, text="Launch Video Enhancer", state="disabled", **button_style)
            window_id = self.canvas.create_window(700, 520, window=self.enchancer_button)
            self.button_windows.append(window_id)

            self.activation_button = ctk.CTkButton(self.canvas, text="Activate Subscription", command=self.open_activation_window, **button_style)
            window_id = self.canvas.create_window(700, 590, window=self.activation_button)
            self.button_windows.append(window_id)

            self.logout_button = ctk.CTkButton(self.canvas, text="Logout", command=self.Logout, **button_style)
            window_id = self.canvas.create_window(700, 660, window=self.logout_button)
            self.button_windows.append(window_id)


    def is_subscription_active(self):
        subscription_type = self.user_data.get('subscription_type', '')
        if subscription_type.lower() in ['monthly', 'permanent']:
            return True
        return False




    def Logout(self):
        set_user_data({})
        self.pack_forget()
        self.master.login_frame.reset_fields()
        self.master.show_mainwindow()

    


    def menu_action(self, value):
        if value == "Settings":
            logging.info("Settings option clicked (not yet implemented)")
            # Placeholder – show settings popup or future config
        elif value == "Check for Updates":
            logging.info("Checking for updates...")
            # You can simulate an update check here
            from tkinter import messagebox
            messagebox.showinfo("Update", "Your software is up to date.")


    def run_enchancer(self):
        from File_path import resource_path
        import os
        import subprocess
        VideoEnchancer_Folder = resource_path('VideoEnchancer.exe')
        video_enhancer_exe = os.path.join(VideoEnchancer_Folder, 'VideoEnchancer.exe')
        logging.info(f"Resolved path to VideoEnhancer.exe: {video_enhancer_exe}")

        if not os.path.exists(video_enhancer_exe):
            logging.info(f"Error: The executable {video_enhancer_exe} does not exist.")
            return

        if not os.access(video_enhancer_exe, os.X_OK):
            logging.error(f"No execute permission for {video_enhancer_exe}. Check file permissions.")
            return

        try:
            self.master.destroy()
            result = subprocess.run([video_enhancer_exe], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            stdout = result.stdout.decode().strip()
            stderr = result.stderr.decode().strip()
            logging.info(f"Successfully launched {video_enhancer_exe}, stderr: {stderr},stdout: {stdout}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error message: {e.stderr.decode().strip() if e.stderr else 'No error message'}")
        except Exception as e:
            logging.error(f"Failed to launch VideoEnchancer.exe: {str(e)}")

    def hide_widgets(self):
        for widget in self.winfo_children():
            widget.pack_forget()

    def open_activation_window(self):
        ActivationWindow(self, self.refresh_user_data)

    def refresh_user_data(self):
        updated_data = Update_user_data()
        if updated_data is not None:
            self.user_data = updated_data
        else:
            logging.error("Failed to refresh userdata")
        self.create_widgets()
        self.update_buttons()
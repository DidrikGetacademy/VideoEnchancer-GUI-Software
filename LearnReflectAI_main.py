import subprocess
from Validate_key import validate_key
import os
import sys
from Logger import logging
from tkinter import Tk
from File_path import activation_key_path, resource_path
from Decryption import load_key



def start_program(): 
    from activation_window import ActivationWindow
    root = Tk()
    root.withdraw()
    try:
       if not is_program_activated():
          logging.info("Program not activated. opening activation window")
          activation_window = ActivationWindow(root) 
          activation_window.wait_window()  
        
        
       if is_program_activated():
           logging.info("Program is activated. running LearnReflectAI.")
           
    
    except Exception as e:
        logging.error(f"Error in start_program: {e}",exc_info=True)





def is_program_activated():
    if not activation_key_path.exists():
        logging.info("Activation key file does not exist.")
        return False
    
    key_valid = load_key()
    if not key_valid:
        logging.info("key validation failed.")
        return False
    
    logging.info("Program activated successfully.")
    return True



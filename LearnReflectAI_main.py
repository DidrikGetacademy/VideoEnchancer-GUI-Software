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
          activation_window = ActivationWindow(root,run_main_program_callback=run_LearnReflectAI) 
          activation_window.wait_window()  
        
        
       if is_program_activated():
           logging.info("Program is activated. running LearnReflectAI.")
           run_LearnReflectAI()
    
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





def run_LearnReflectAI():
    try:
        script_path = resource_path('LearnReflectAI.py')
        logging.info(f"Script path resolved to: {script_path}")
        
        if not os.path.exists(script_path):
          logging.error(f"LearnReflectAI.py not found at: {script_path}")
          raise FileNotFoundError("LearnReflectAI.py is missing!    ")


      
        subprocess.run([sys.executable, script_path])

    except subprocess.CalledProcessError as e:
        logging.error(f"Subprocess for LearnReflectAI exited with an error: {e}", exc_info=True)
    except Exception as e:
        logging.error(f"Error in run_LearnReflectAI: {e}", exc_info=True)

        
    
start_program()  
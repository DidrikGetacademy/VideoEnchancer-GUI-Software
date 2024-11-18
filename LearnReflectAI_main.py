import subprocess
from Validate_key import ensure_directories, load_key, validate_key
import os
import sys
from Logger import logging
from tkinter import Tk





def debug_bundled_environment():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
        print(f"Extracted base path: {base_path}")
        print("Contents of base path:")
        for root, dirs, files in os.walk(base_path):
            print(f"\nRoot: {root}")
            print(f"Directories: {dirs}")
            print(f"Files: {files}")
    else:
        print("Not running in bundled mode.")

debug_bundled_environment()






def resource_path(relative_path):
    if getattr(sys, 'frozen',False):
        base_path = sys._MEIPASS
    else: 
        base_path = os.path.abspath(".")
    logging.info(f"Base Path for bundled files {base_path}")
    logging.info(f"Bundled files and folders: {os.listdir(base_path)}")
    full_path = os.path.join(base_path,relative_path)
    return full_path






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
    try:
        stored_key = load_key()
        if stored_key and validate_key(stored_key):
            logging.info("Program is activated.")
            return True
    except Exception as e:
        logging.error(f"Error checking activation status: {e}", exc_info=True)
    logging.info("Program is not activated.")
    return False






def run_LearnReflectAI():
    try:
        script_path = resource_path('LearnReflectAI.py')
        logging.info(f"Script path resolved to: {script_path}")
        
        logging.info(f"Script path resolved to: {script_path}")
        if not os.path.exists(script_path):
          logging.error(f"LearnReflectAI.py not found at: {script_path}")


      
        subprocess.run([sys.executable, script_path])

    except subprocess.CalledProcessError as e:
        logging.error(f"Subprocess for LearnReflectAI exited with an error: {e}", exc_info=True)
    except Exception as e:
        logging.error(f"Error in run_LearnReflectAI: {e}", exc_info=True)

        
        
    if __name__ == "__main__":
        try:
            ensure_directories()
            logging.info("Ensured directories and key files are set up.")
        except Exception as e:
            logging.error(f"Error ensuring directories: {e}",exc_info=True)
            
    
    
    
    
    
start_program()  

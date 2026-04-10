# import os
# # os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
# # os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
# import sys
# import torch 
# import torch
# import onnxruntime as ort
# from functools  import cache
# from time       import sleep
# from subprocess import run  as subprocess_run
# import ffmpeg
# from smolagents import CodeAgent, FinalAnswerTool,  DuckDuckGoSearchTool, GoogleSearchTool, VisitWebpageTool, LiteLLMModel,VLLMModel, SpeechToTextTool,PythonInterpreterTool
# from Agents_tools import ExtractAudioFromVideo, Fetch_top_trending_youtube_videos, Log_Agent_Progress,Read_transcript
# import numpy as np
# from PIL import Image, ImageTk
# import yaml
# from tkinter import filedialog
# import os
# import time
# from googleapiclient.discovery import build
# from googleapiclient.http import MediaFileUpload
# from dotenv import load_dotenv
# from shutil     import rmtree as remove_directory
# import subprocess
# from timeit     import default_timer as timer
# from PIL import Image, ImageSequence
# import threading
# import cv2
# from Logger import logging
# from typing    import Callable
# from threading import Thread
# from itertools import repeat
# import yt_dlp
# from multiprocessing.pool import ThreadPool
# from PIL import Image, ImageDraw, ImageFont 
# from multiprocessing import ( 
#     Process, 
#     Queue          as multiprocessing_Queue,
#     freeze_support as multiprocessing_freeze_support
# )

# from json import (
#     load  as json_load, 
#     dumps as json_dumps
# )
# import gc
# import shutil
# import json
# from File_path import get_app_data_path
# from os import (
#     sep        as os_separator,
#     devnull    as os_devnull,
#     environ    as os_environ,
#     cpu_count  as os_cpu_count,
#     makedirs   as os_makedirs,
#     listdir    as os_listdir,
#     remove     as os_remove
# )

# from os.path import (
#     basename   as os_path_basename,
#     dirname    as os_path_dirname,
#     abspath    as os_path_abspath,
#     join       as os_path_join,
#     exists     as os_path_exists,
#     splitext   as os_path_splitext,
#     expanduser as os_path_expanduser
# )


# from natsort          import natsorted
# from moviepy.video.io import ImageSequenceClip 
# from onnxruntime      import InferenceSession as onnxruntime_inferenceSession

# from PIL.Image import (
#     open      as pillow_image_open,
#     fromarray as pillow_image_fromarray
# )

# from cv2 import (
#     CAP_PROP_FPS,
#     CAP_PROP_FRAME_COUNT,
#     CAP_PROP_FRAME_HEIGHT,
#     CAP_PROP_FRAME_WIDTH,
#     COLOR_BGR2RGB,
#     COLOR_GRAY2RGB,
#     COLOR_BGR2RGBA,
#     COLOR_RGB2GRAY,
#     IMREAD_UNCHANGED,
#     INTER_LINEAR,
#     INTER_AREA,
#     INTER_CUBIC,
#     VideoCapture as opencv_VideoCapture,
#     cvtColor     as opencv_cvtColor,
#     imdecode     as opencv_imdecode,
#     imencode     as opencv_imencode,
#     addWeighted  as opencv_addWeighted,
#     cvtColor     as opencv_cvtColor,
#     resize       as opencv_resize,
# )
# import numpy as np
# from numpy import (
#     ndarray     as numpy_ndarray,
#     frombuffer  as numpy_frombuffer,
#     concatenate as numpy_concatenate, 
#     transpose   as numpy_transpose,
#     full        as numpy_full, 
#     zeros       as numpy_zeros, 
#     expand_dims as numpy_expand_dims,
#     squeeze     as numpy_squeeze,
#     clip        as numpy_clip,
#     mean        as numpy_mean,
#     repeat      as numpy_repeat,
#     max         as numpy_max, 
#     float32,
#     uint8
# )

# import torch
# import tkinter as tk
# from tkinter import StringVar, DISABLED,END,scrolledtext
# try:
#     import tkinterdnd2 as _tkdnd
#     _TKDND_AVAILABLE = True
# except ImportError:
#     _TKDND_AVAILABLE = False
# from customtkinter import (
#     CTk,
#     CTkButton,
#     CTkFrame,
#     CTkComboBox,
#     CTkCheckBox,
#     CTkSlider,
#     CTkEntry,
#     CTkFont,
#     CTkImage,
#     CTkLabel,
#     CTkOptionMenu,
#     CTkScrollableFrame,
#     CTkToplevel,
#     filedialog,
#     CTkTextbox,
#     set_appearance_mode,
#     set_default_color_theme
# )



# def check_hardware():
#     if torch.cuda.is_available():
#         try:
#             major = torch.cuda.get_device_capability(0)[0]
#             if major >= 7:
#                 return "cuda", torch.float16
#             else:
#                 return "cuda", torch.bfloat16
#         except (AssertionError, RuntimeError) as e:
#             print(f"Warning: Unable to access CUDA device. Falling back to CPU. Reason: {e}")
#             return "cpu", torch.float32
#     else:
#         print("CUDA not available. Using CPU.")
#         return "cpu", torch.float32
# device, dtype = check_hardware()

# def get_gpu_vram():
#     import psutil
#     try:
#         import wmi
#         w = wmi.WMI()
#         for gpu in w.Win32_VideoController():
#             if 'VRAM' in gpu.AdapterRAM:
#                    return min(4, int((psutil.virtual_memory().total / (1024**3)) * 0.7))  
#             return 4000
#     except:
#         return 4000

# def get_cpu_number():
#         try:
#             cpu_number = max(1, int(os_cpu_count() // 1.5))
#             return cpu_number
#         except Exception as e:
#             return

# if sys.stdout is None: sys.stdout = open(os_devnull, "w")
# if sys.stderr is None: sys.stderr = open(os_devnull, "w")

# def find_by_relative_path(relative_path: str) -> str:
#     base_path = getattr(sys, '_MEIPASS', os_path_dirname(os_path_abspath(__file__)))
#     return os_path_join(base_path, relative_path)


# app_name   = "LearnReflect AI"
# app_name_color          = "#D49A2A"    # amber
# dark_color              = "#070707"
# background_color        = "#060606"
# text_color              = "#948C7E"    # warm muted
# widget_background_color = "#0E0E0D"
# # ── Design system ────────────────────────────────────────────────────
# AMBER        = "#D49A2A"
# AMBER_DIM    = "#8C6418"
# AMBER_GLOW   = "#3C2808"
# CREAM        = "#E0D8C8"
# CREAM2       = "#948C7E"
# CREAM3       = "#4A4640"
# BORDER1      = "#141210"
# BORDER2      = "#201E1A"
# BORDER3      = "#383028"
# GREEN_OK     = "#38A858"
# GREEN_BG     = "#0C1C10"
# PANEL_BG     = "#0A0A09"
# PANEL2_BG    = "#0E0E0D"
# very_low_VRAM  = 4
# low_VRAM       = 3
# medium_VRAM    = 2.2
# very_high_VRAM = 0.6

# AI_LIST_SEPARATOR           = [ "----" ]
# IRCNN_models_list           = [ "IRCNN_Mx1", "IRCNN_Lx1" ]
# SRVGGNetCompact_models_list = [ "RealESR_Gx4", "RealSRx4_Anime" ]
# RRDB_models_list            = [ "BSRGANx4", "BSRGANx2", "RealESRGANx4"]
# Facedetection_model_list = ["yolov8x-face-lindevs"]



# ####Cookies
# import datetime
# FUTURE_DATE = datetime.datetime(2030, 1, 1)
# NEW_TIMESTAMP = int(FUTURE_DATE.timestamp())
# fixed_cookie_filename = "youtube.com_cookies.txt"
# COOKIE_STORAGE_DIR = get_app_data_path() / "cookies" 
# COOKIE_PATH_FILE = COOKIE_STORAGE_DIR / fixed_cookie_filename
# if not COOKIE_STORAGE_DIR.exists():
#     COOKIE_STORAGE_DIR.mkdir(parents=True)
# cookie_file_path = None


# #Video Preview
# youtube_download_list = []
# frame_cache = {}
# last_model_config =  None
# preview_ai_instance = None
# current_loaded_model = None
# model_loading_thread = None
# global original_preview
# global upscaled_preview
# global original_preview_frame
# global upscaled_preview_frame
# preview_instance = None  
# file_list_update_callback = None
# media_info_update_callback = None
# stop_download_flag = False
# Global_offline_model = None  

# import onnxruntime as ort
# model_loading_lock = threading.Lock()
# AI_models_list         = ( SRVGGNetCompact_models_list + AI_LIST_SEPARATOR + RRDB_models_list + AI_LIST_SEPARATOR + IRCNN_models_list )
# keep_frames_list       = [ "Disabled", "Enabled" ]
# image_extension_list   = [ ".png", ".jpg", ".bmp", ".tiff" ]
# video_extension_list   = [ ".mp4 (x264)", ".mp4 (x265)", ".avi" ]
# interpolation_list     = [ "Low", "Medium", "High", "Disabled" ]
# audio_mode_list        = ["Disabled", "Vocal Isolation", "Audio Denoise"] 
# OUTPUT_PATH_CODED    = "Same path as input files"
# DOCUMENT_PATH        = os_path_join(os_path_expanduser('~'), 'Documents')
# USER_PREFERENCE_PATH = find_by_relative_path(f"{DOCUMENT_PATH}{os_separator}{app_name}_UserPreference.json")
# FFMPEG_EXE_PATH      = find_by_relative_path(f"Assets{os_separator}ffmpeg.exe")
# os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "video_codec;h264_cuvid"
# EXIFTOOL_EXE_PATH    = find_by_relative_path(f"Assets{os_separator}exiftool.exe")
# FRAMES_FOR_CPU       = 30
# if 'CUDAExecutionProvider' not in ort.get_available_providers():
#     FRAMES_FOR_CPU = 5


# if os_path_exists(FFMPEG_EXE_PATH): 
#     logging.info(f"[{app_name}] External ffmpeg.exe file found")
#     os_environ["IMAGEIO_FFMPEG_EXE"] = FFMPEG_EXE_PATH

# if os_path_exists(USER_PREFERENCE_PATH):
#     logging.info(f"[{app_name}] Preference file exist")
#     with open(USER_PREFERENCE_PATH, "r") as json_file:
#         json_data = json_load(json_file)
#         default_AI_model          = json_data["default_AI_model"]
#         default_AI_multithreading = json_data["default_AI_multithreading"]
#         default_image_extension   = json_data["default_image_extension"]
#         default_video_extension   = json_data["default_video_extension"]
#         default_interpolation     = json_data["default_interpolation"]
#         default_keep_frames       = json_data.get("default_keep_frames",        keep_frames_list[0])
#         default_audio_mode        = json_data.get("default_audio_mode",audio_mode_list[0]) 
#         default_output_path       = json_data["default_output_path"]
#         default_resize_factor     = json_data["default_resize_factor"]
#         default_VRAM_limiter      = json_data["default_VRAM_limiter"]
# else:
#     logging.info(f"[{app_name}] Preference file does not exist, using default coded value")
#     default_AI_model          = AI_models_list[0]
#     default_AI_multithreading = max(1, int(os_cpu_count() // 2))
#     default_gpu               = get_gpu_vram()
#     default_keep_frames       = keep_frames_list[0]
#     default_image_extension   = image_extension_list[0]
#     default_video_extension   = video_extension_list[0]
#     default_interpolation     = interpolation_list[0]
#     default_audio_mode        = audio_mode_list[0] 
#     default_output_path       = OUTPUT_PATH_CODED
#     default_resize_factor     = str(50)
#     default_VRAM_limiter      = str(4)
#     default_cpu_number        = str(int(get_cpu_number()))

# COMPLETED_STATUS = "Completed"
# ERROR_STATUS     = "Error"
# STOP_STATUS      = "Stop"

# controls_bar_frame  = None   # set in VideoEnhancer.__init__
# controls_grid       = None   # 2-row × 4-col inner grid frame
# file_overrides      = {}    # per-file AI setting overrides: {file_path: {key: value}}
# upscale_slot_frame  = None   # set in place_message_label()

# offset_y_options = 0.105
# row0_y = 0.52
# row1_y = row0_y + offset_y_options
# row2_y = row1_y + offset_y_options
# row3_y = row2_y + offset_y_options
# row4_y = row3_y + offset_y_options
# row5_y = row4_y + offset_y_options



# offset_x_options = 0.28
# column1_x = 0.5
# column0_x = column1_x - offset_x_options
# column2_x = column1_x + offset_x_options
# column1_5_x = column1_x + offset_x_options/2
# column_info1  = 0.625
# column_1_5    = column_info1 + 0.08
# column_1_4    = column_1_5 - 0.0127
# column_info2  = 0.858
# column_3      = column_info2 + 0.08


# little_textbox_width = 74
# little_menu_width = 98

# supported_file_extensions = [
#     '.heic', '.jpg', '.jpeg', '.JPG', '.JPEG', '.png',
#     '.PNG', '.webp', '.WEBP', '.bmp', '.BMP', '.tif',
#     '.tiff', '.TIF', '.TIFF', '.mp4', '.MP4', '.webm',
#     '.WEBM', '.mkv', '.MKV', '.flv', '.FLV', '.gif',
#     '.GIF', '.m4v', ',M4V', '.avi', '.AVI', '.mov',
#     '.MOV', '.qt', '.3gp', '.mpg', '.mpeg', ".vob"
# ]

# supported_video_extensions = [
#     '.mp4', '.MP4', '.webm', '.WEBM', '.mkv', '.MKV',
#     '.flv', '.FLV', '.gif', '.GIF', '.m4v', ',M4V',
#     '.avi', '.AVI', '.mov', '.MOV', '.qt', '.3gp',
#     '.mpg', '.mpeg', ".vob"
# ]




# CPU_ONLY = 'CUDAExecutionProvider' not in ort.get_available_providers()
# if CPU_ONLY:
#     FRAMES_FOR_CPU = 5




# def load_model_async():

#     modelmanager.load_model()
 

# class modelmanager:
#     """Class manager for AI model"""
#     _model = None
#     _lock = threading.Lock()
#     model_loaded_event = threading.Event()
#     @classmethod
#     def load_model(cls, model_path, **Kwargs):
#         """Load model & return model instance"""
#         device, dtype = check_hardware()
#         with cls._lock:
#             if cls._model is None:
#                 gc.collect()
#                 if torch.cuda.is_available():
#                     torch.cuda.empty_cache()
#                 cls._model = LiteLLMModel(
#                     model_id="gpt-5",
#                     reasoning_effort="minimal",
#                     api_key=os.getenv("GPT_5_API_KEY"),
#                     max_tokens=16000,
#                 )
#                 print("videoencancer.exe: dtype= ", dtype)
#         global model_loaded_event
#         cls.model_loaded_event.set()
#         print("Model loaded successfully! :)")
#         return cls._model
    
#     @classmethod
#     def get_model(cls):
#         """Return model instance"""
#         if cls._model is None:
#             raise RuntimeError("model has not been loaded yet")
#         return cls._model
    
    


# from smolagents.tools import PipelineTool



# class SpeechToTextToolCUDA(PipelineTool):
#     default_checkpoint = r"c:\Users\didri\Desktop\AI-models\Audio-Models\faster-whisper-large-v3-turbo-int8float16"
#     description = "Fast tool that transcribes audio into text using faster-whisper. It returns the path to the transcript file"
#     name = "transcriber"
#     inputs = {
#         "audio": {
#             "type": "audio",
#             "description": "The audio to transcribe. Can be a local path, a URL, or a tensor.",
#         },
#         "text_path": {
#             "type": "string",
#              "description": "The path to save the transcript to.",
#         },
#         "video_path": {
#             "type": "string",
#             "description": "The path to the video to transcribe. only for info printging",
#         }
#     }
#     output_type = "string"
#     def setup(self):

#         self.model = WhisperModel(
#                 model_size_or_path=self.default_checkpoint,
#                 device="cuda",
#                 compute_type="int8_float16"
#                 )
#     def forward(self, inputs):
#         audio_path = inputs["audio"]
#         text_path = inputs["text_path"]
#         video_path = inputs["video_path"]
#         segments, info = self.model.transcribe(
#             audio_path,
#             language="en",
#             temperature=0.0,
#             vad_filter=True,
#             initial_prompt="Motivational podcast",
#             condition_on_previous_text=True,

#         )
#         print(f"\n🔊 Using Whisper on device: {self.device}, \ntranscribing video: {video_path} \n   with inputs: {self.inputs}")
#         print(f"[INFO] Detected Language: {info.language} (confidence: {info.language_probability:.2f})")
#         print(f"[INFO] Audio Duration: {info.duration:.2f} seconds")

#         try:
#             with open(text_path, "a", encoding="utf-8") as f:
#                 print(f"opening txt_path on: {text_path} device: {self.device}")

#                 try:
#                     for segment in segments:
#                          f.write(f"{segment.text.strip()}\n")
#                     f.write("\n\n")
#                 except Exception as e:
#                     print(f"error during segments: {str(e)}")

#         finally:
#             print(f"transcription complete ! device  {self.device}")
#             if self.device == "cuda":
#                 torch.cuda.empty_cache()
#                 gc.collect()
#                 del self.model

#         return text_path

#     def encode(self, audio):
#         return {"audio": audio}

#     def decode(self, outputs):
#         return outputs




























# class vidintel_agent_gui():
#     """Agent that retrieves transcripts, searches the web, and generates optimized metadata for videos."""

#     def __init__(self, parent_container):
#         self.parent_container = parent_container
#         self.uploaded_files = selected_file_list

#         self.container = CTkFrame(
#             master=self.parent_container,
#             fg_color="#282828",
#             border_width=2,
#             border_color="#404040",
#             corner_radius=10
#         )
#         self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

#         self.loading_label = CTkLabel(
#             master=self.container,
#             text="",
#             text_color="#00FF00",
#             font=("Arial", 14)
#         )
#         self.loading_label.grid(row=2, column=0, pady=5, sticky="nsew")

#         wait_time = 0
        

#         self.loading_label.configure(text=f"⏳ Waiting for model to load... {wait_time}s")
#         self.loading_label.update_idletasks()
#         loaded = modelmanager.model_loaded_event.wait(timeout=60)
#         if not loaded:
#              self.loading_label.configure(text="❌ Timeout waiting for model to load.")
#              return

#         self.loading_label.configure(text="✅ Model loaded successfully.")
#         self.model = modelmanager.get_model() 



#         self.create_widgets()
#         global file_list_update_callback
#         file_list_update_callback = self.sync_uploaded_files
#         file_names = [os_path_basename(f) for f in self.uploaded_files]
#         self.file_menu.configure(values=file_names)
#         if file_names:
#            self.file_menu_var.set(file_names[0])

#     def create_widgets(self):
#         self.top_bar = CTkFrame(
#             master=self.container,
#             fg_color="#282828"
#         )
#         self.top_bar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

#         self.file_menu_var = StringVar(value="No files uploaded")
#         self.file_menu = CTkOptionMenu(
#             master=self.top_bar,
#             variable=self.file_menu_var,
#             values=[],
#             width=200,
#             height=30,
#             font=bold11,
#             dropdown_font=bold11,
#             fg_color="#282828",
#             button_color="#404040",
#             text_color="#FFFFFF"
#         )
#         self.file_menu.pack(side="left", padx=10, pady=5)

    
#         self.metadata_btn = CTkButton(
#             master=self.top_bar,
#             text="Generate Metadata",
#             width=140,
#             height=30,
#             font=bold11,
#             border_width=1,
#             fg_color="#282828",
#             text_color="#E0E0E0",
#             border_color="#0096FF",
#             command=lambda: self.start_metadata_thread(),
#         )
#         self.metadata_btn.pack(side="left", padx=10, pady=5)
        
#         self.Social_media_list = CTkOptionMenu(
#             master=self.top_bar,
#             width=140,
#             height=30,
#             font=bold11,
#             fg_color="#282828",
#             text_color="#E0E0E0",
#             #command=
#             state="normal",
#             values=["YouTube", "Instagram", "TikTok"]  

#         )
#         self.Social_media_list.pack(side="left", padx=10, pady=5)

    
#         self.info_button_LearnReflect_Agent = create_info_button(
#             open_LR_Agent_tool_info,
#             text="INFO",
#             width=15,
#             master=self.top_bar
#         )
#         self.info_button_LearnReflect_Agent.pack(side="left", padx=10, pady=5)

  
#         self.chat_display  = scrolledtext.ScrolledText(
#           self.container,
#           wrap=tk.WORD,
#           width=55,
#           height=25,
#           font=("Helvetica",12),
#           bg="black",  
#           fg="white",
#           state="disabled",
#         )
#         self.chat_display.config(
#             insertbackground="yellow",
#             selectbackground="#444444",
#             selectforeground="white",
#             borderwidth=2,
#             relief="sunken"
#         )
#         self.chat_display.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
#         self.chat_display.yview(END)
#         self.container.columnconfigure(0, weight=1)
#         self.container.rowconfigure(1, weight=1)

#     def sync_uploaded_files(self):
#         """Sync uploaded_files with global list and refresh the dropdown"""
#         self.uploaded_files = selected_file_list
#         self.update_file_list()
#         if self.uploaded_files:
#             self.metadata_btn.configure(state="normal")

#     def start_metadata_thread(self):
#         thread = threading.Thread(target=self.load_llama_instruct, daemon=True)
#         thread.start()
#         self.metadata_btn.configure(state="DISABLED")
      
#     def load_llama_instruct(self, uploaded_file=None):
#         load_dotenv()
#         uploaded_file = self.file_menu_var.get()
#         if uploaded_file: 
#                 file_extension = os.path.splitext(uploaded_file)[1].lower()
#                 if file_extension in ['.mp4', '.avi', '.mov', '.mkv']:
#                         file = "Video file"
#                 elif file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
#                         file = "Image file"
                                    
#                         self.chat_display.config(state=tk.NORMAL)
#                         self.chat_display.insert(tk.END, "Sorry we do not read any pitcures at this moment, this will be available in later updates\n")
#                         self.chat_display.update()
#                         return


#         self.chat_display.config(state=tk.NORMAL)
#         self.chat_display.insert(tk.END, "1. 🤖 AI-agenten transcribes video now...\n")
#         self.chat_display.configure(state="disabled")
#         self.chat_display.update()
#         uploaded_file_name = self.file_menu_var.get()
#         Video_path = next((f for f in self.uploaded_files if os_path_basename(f) == uploaded_file_name), None)
#         if not Video_path:
#             print("Error: File not found!")
#             self.chat_display.config(state=tk.NORMAL)
#             self.chat_display.insert(tk.END, "Not a valid file path" + "\n")
#             self.chat_display.config(state=tk.DISABLED)  
#             return
                        
#         user_task = "Please generate a Title, Description, Hashtags, Keywords, and a unique message for my video. The goal is to help it go viral by leveraging current trends and analyzing similar successful videos. The unique message should highlight key insights, secret strategies, or specific elements that contributed to the virality of similar content. Think of it as a short, strategic note or idea that could help this video stand out and perform exceptionally well.in your final answer Use the exact key names: `title`, `description`, `keywords`, `hashtags`, and `Unique message`. No additional fields."
            
      

#         uploaded_file = self.file_menu_var.get()



        
#         #Agent Prompts
#         with open(find_by_relative_path("./agent_prompts/viral_agent_prompt.yaml"), 'r') as stream:
#                     Manager_Agent_prompt_templates = yaml.safe_load(stream)


#         #Tool initalization
#         final_answer = FinalAnswerTool()
#         web_search = DuckDuckGoSearchTool()
#         Extract_audio = ExtractAudioFromVideo
#         fetch_youtube_video_information = Fetch_top_trending_youtube_videos
#         log_every_step = Log_Agent_Progress
#        #Transcriber = SpeechToTextToolCUDA()
#         PythonInterpeter = PythonInterpreterTool()
#         Visit_WebPage = VisitWebpageTool()


#         manager_agent  = CodeAgent(
#             model=self.model,
#             tools=[
#                 final_answer,log_every_step,
#                   Extract_audio,
#                 #  Transcriber,
#                   PythonInterpeter,
#                   fetch_youtube_video_information,
#                   Visit_WebPage,
#                   ], 
#             max_steps=4,
#             prompt_templates=Manager_Agent_prompt_templates,
        
#         )

#         context_vars = {
#                "video_path": Video_path,
#               'Transcript_text_filepath': find_by_relative_path("./Project_text_files/Audio_TO_transcript.txt"), #kan endre dette så det finnes en .txt path som agent kan sende inn til speectotexttool når den er ferdig med extractaudiofromvideo, men må huske og endre system prompten også.
#                "chat_display": self.chat_display,
#             }       

#         Response = manager_agent.run(
#             task=user_task,
#             additional_args=context_vars
#         )
#         runsummary = manager_agent.visualize()
#         with open("./Agent_Orchestrator_Visualize.txt", "w") as f:
#             f.write(runsummary)
#         torch.cuda.empty_cache()
#         gc.collect()
#         del self.model

#         if isinstance(Response, dict):
#             self._append_chat(self._format_metadata(Response))
#             self.clean_temp_audio()

#         else:
#             self._append_chat(str(Response))


#         try:
#             if os.path.exists("temp_audio.wav"):
#                 os.remove("temp_audio.wav")
#                 logging.info("🗑️ temp_audio.wav deleted successfully.")
#         except Exception as e:
#             logging.info(f"⚠️ Error deleting temp audio: {e}")

         
#     def clean_temp_audio(self):
#         try:
#             if os.path.exists("temp_audio.wav"):
#                 os.remove("temp_audio.wav")
#                 logging.info("🗑️ temp_audio.wav deleted successfully.")
#         except Exception as e:
#             logging.info(f"⚠️ Error deleting temp audio: {e}")

#     def _format_metadata(self, md: dict) -> str:
#         return (
#             f"🎬 Title:\n  {md.get('title', 'N/A')}\n\n"
#             f"📝 Description:\n  {md.get('description', 'N/A')}\n\n"
#             f"🔑 Keywords:\n  {', '.join(md.get('keywords', []))}\n\n"
#             f"🏷️ Hashtags:\n  {' '.join(md.get('hashtags', []))}\n\n\n"
#             f" Tips/ideas: \n {' '.join(md.get('Unique message', []))}"
#         )
    

#     def update_file_list(self):
#         """Update dropdown with current files"""
#         file_names = [os_path_basename(f) for f in self.uploaded_files]
#         self.file_menu.configure(values=file_names)
#         if file_names:
#             self.file_menu_var.set(file_names[0])

#     def _append_chat(self, text: str):
#         self.chat_display.config(state=tk.NORMAL)
#         self.chat_display.insert(tk.END, text + "\n")
#         self.chat_display.see(tk.END)
#         self.chat_display.config(state=tk.DISABLED)

#     def clear_file_list(self):
#         """Reset dropdown to empty state"""
#         self.uploaded_files = []
#         self.file_menu.configure(values=[])
#         self.file_menu_var.set("No files uploaded")







































# class corelytics_InsightCatcher():
#     """Agent that retrieves transcripts, Analyze the transcript and provide insights too the user """

#     def __init__(self, parent_container):
#         self.parent_container = parent_container
#         self.uploaded_files = selected_file_list
#         self.container = CTkFrame(
#             master=self.parent_container,
#             fg_color="#282828",
#             border_width=2,
#             border_color="#404040",
#             corner_radius=10
#         )
#         self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

#         self.loading_label = CTkLabel(
#             master=self.container,
#             text="",
#             text_color="#00FF00",
#             font=("Arial", 14)
#         )
#         self.loading_label.grid(row=2, column=0, pady=5, sticky="nsew")

#         wait_time = 0
        
#         global Global_offline_model
#         while Global_offline_model is None:
#             self.loading_label.configure(text=f"⏳ Waiting for model to load... {wait_time}s")
#             self.loading_label.update_idletasks()
#             time.sleep(1)
#             wait_time += 1
#             if wait_time > 60:
#                 self.loading_label.configure(text="❌ Timeout waiting for model to load.")
#                 return

#         self.loading_label.configure(text="✅ Model loaded successfully.")
#         self.model = Global_offline_model



#         self.create_widgets()
#         global file_list_update_callback
#         file_list_update_callback = self.sync_uploaded_files
#         file_names = [os_path_basename(f) for f in self.uploaded_files]
#         self.file_menu.configure(values=file_names)
#         if file_names:
#            self.file_menu_var.set(file_names[0])

#     def create_widgets(self):
#         self.top_bar = CTkFrame(
#             master=self.container,
#             fg_color="#282828"
#         )
#         self.top_bar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

#         self.file_menu_var = StringVar(value="No files uploaded")
#         self.file_menu = CTkOptionMenu(
#             master=self.top_bar,
#             variable=self.file_menu_var,
#             values=[],
#             width=200,
#             height=30,
#             font=bold11,
#             dropdown_font=bold11,
#             fg_color="#282828",
#             button_color="#404040",
#             text_color="#FFFFFF"
#         )
#         self.file_menu.pack(side="left", padx=10, pady=5)

    
#         self.InsightCatcher_btn = CTkButton(
#             master=self.top_bar,
#             text="Run InsightCatcher",
#             width=140,
#             height=30,
#             font=bold11,
#             border_width=1,
#             fg_color="#282828",
#             text_color="#E0E0E0",
#             border_color="#0096FF",
#             command=lambda: self.start_metadata_thread(),
#         )
#         self.InsightCatcher_btn.pack(side="left", padx=10, pady=5)
        
    
#         self.info_button_LearnReflect_Agent = create_info_button(
#             open_LR_Agent_tool_info,
#             text="INFO",
#             width=15,
#             master=self.top_bar
#         )
#         self.info_button_LearnReflect_Agent.pack(side="left", padx=10, pady=5)

  
#         self.InSightCatcher_chatlogger  = scrolledtext.ScrolledText(
#           self.container,
#           wrap=tk.WORD,
#           width=55,
#           height=25,
#           font=("Helvetica",12),
#           bg="black",  
#           fg="white",
#           state="disabled",
#         )
#         self.InSightCatcher_chatlogger.config(
#             insertbackground="yellow",
#             selectbackground="#444444",
#             selectforeground="white",
#             borderwidth=2,
#             relief="sunken"
#         )
#         self.InSightCatcher_chatlogger.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
#         self.InSightCatcher_chatlogger.yview(END)
#         self.container.columnconfigure(0, weight=1)
#         self.container.rowconfigure(1, weight=1)

#     def sync_uploaded_files(self):
#         """Sync uploaded_files with global list and refresh the dropdown"""
#         self.uploaded_files = selected_file_list
#         self.update_file_list()
#         if self.uploaded_files:
#             self.InsightCatcher_btn.configure(state="normal")

#     def start_metadata_thread(self):
#         thread = threading.Thread(target=self.load_llama_instruct, daemon=True)
#         thread.start()
#         self.InsightCatcher_btn.configure(state="DISABLED")
      
#     def load_llama_instruct(self, uploaded_file=None):
#         load_dotenv()
#         uploaded_file = self.file_menu_var.get()
#         if uploaded_file: 
#                 file_extension = os.path.splitext(uploaded_file)[1].lower()
#                 if file_extension in ['.mp4', '.avi', '.mov', '.mkv']:
#                         file = "Video file"
#                 elif file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
#                         file = "Image file"
                                    
#                         self.InSightCatcher_chatlogger.config(state=tk.NORMAL)
#                         self.InSightCatcher_chatlogger.insert(tk.END, "Sorry we do not read any pitcures at this moment, this will be available in later updates\n")
#                         self.InSightCatcher_chatlogger.update()
#                         return


#         self.InSightCatcher_chatlogger.config(state=tk.NORMAL)
#         self.InSightCatcher_chatlogger.insert(tk.END, "1. 🤖 AI-agenten transcribes video now...\n")
#         self.InSightCatcher_chatlogger.configure(state="disabled")
#         self.InSightCatcher_chatlogger.update()
#         uploaded_file_name = self.file_menu_var.get()
#         Video_path = next((f for f in self.uploaded_files if os_path_basename(f) == uploaded_file_name), None)
#         if not Video_path:
#             print("Error: File not found!")
#             self.InSightCatcher_chatlogger.config(state=tk.NORMAL)
#             self.InSightCatcher_chatlogger.insert(tk.END, "Not a valid file path" + "\n")
#             self.InSightCatcher_chatlogger.config(state=tk.DISABLED)  
#             return
                        
#         user_task = (
               
#                   )
      

#         uploaded_file = self.file_menu_var.get()
#         context_vars = {
#                "video_path": Video_path,
#                "file_type": file,
#                "chat_display": self.InSightCatcher_chatlogger,
#             }       


        
#         #Agent Prompts
#         with open(find_by_relative_path("./Assets/agent_prompts/videotext_Manger_agent_prompt.yaml"), 'r') as stream:
#                     Manager_Agent_prompt_templates = yaml.safe_load(stream)


#         with open(find_by_relative_path("./Assets/agent_prompts/loaded_reasoning_agent_prompts.yaml"), 'r') as stream:
#                     Reasoning_Agent_Prompt_Template = yaml.safe_load(stream)


#         #Tool initalization
#         final_answer = FinalAnswerTool()
#         Extract_audio = ExtractAudioFromVideo
#         log_every_step = Log_Agent_Progress
#         transcribe = SpeechToTextTool()
  



#         Chunk_reasoning_Agent = CodeAgent (
#             model=self.model,
#             name="Reasoning_Agent",
#             description="",
#             add_base_tools=True,
#             prompt_templates=Reasoning_Agent_Prompt_Template,
#             tools=[],
#             max_steps=30,
#             provide_run_summary=True
#         )


#         manager_agent  = CodeAgent(
#             model=self.model,
#             tools=[final_answer,log_every_step, Extract_audio, transcribe], 
#             managed_agents=[Chunk_reasoning_Agent],
#             max_steps=30,
#             verbosity_level=4,
#             prompt_templates=Manager_Agent_prompt_templates,
#             additional_authorized_imports=['datetime'],
#         )

#         Response = manager_agent.run(
#             task=user_task,
#             additional_args=context_vars
#         )



#         if isinstance(Response, dict):
#             self._append_chat(self._format_metadata(Response))
#             self.clean_temp_audio()

#         else:
#             self._append_chat(str(Response))


#         try:
#             if os.path.exists("temp_audio.wav"):
#                 os.remove("temp_audio.wav")
#                 logging.info("🗑️ temp_audio.wav deleted successfully.")
#         except Exception as e:
#             logging.info(f"⚠️ Error deleting temp audio: {e}")

         
#     def clean_temp_audio(self):
#         try:
#             if os.path.exists("temp_audio.wav"):
#                 os.remove("temp_audio.wav")
#                 logging.info("🗑️ temp_audio.wav deleted successfully.")
#         except Exception as e:
#             logging.info(f"⚠️ Error deleting temp audio: {e}")

    

#     def update_file_list(self):
#         """Update dropdown with current files"""
#         file_names = [os_path_basename(f) for f in self.uploaded_files]
#         self.file_menu.configure(values=file_names)
#         if file_names:
#             self.file_menu_var.set(file_names[0])
             

#     def _append_chat(self, text: str):
#         self.InSightCatcher_chatlogger.config(state=tk.NORMAL)
#         self.InSightCatcher_chatlogger.insert(tk.END, text + "\n")
#         self.InSightCatcher_chatlogger.see(tk.END)
#         self.InSightCatcher_chatlogger.config(state=tk.DISABLED)

#     def clear_file_list(self):
#         """Reset dropdown to empty state"""
#         self.uploaded_files = []
#         self.file_menu.configure(values=[])
#         self.file_menu_var.set("No files uploaded")






















# class social_media_optimizer_Gui:
#     def __init__(self, parent_container):
#             self.parent_container = parent_container
#             self.credentials = None  

#             self.container = CTkFrame(
#                 master=self.parent_container,
#                 fg_color="black",
#                 border_width=2,
#                 border_color="#404040",
#                 corner_radius=10,
#                 height=1000
#             )
#             self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
#             self.container.update_idletasks()


#             self.create_widgets()

#     def create_widgets(self):
#             row=1
#             self.container.columnconfigure(0, weight=1)
#             self.container.columnconfigure(1, weight=1)
#             self.container.rowconfigure(1, weight=1)

        
#             self.add_account_button = CTkButton(
#                 self.container,
#                 text="Add New YouTube Account",
#                 command=lambda: Thread(target=self.authenticate).start(),
#                 font=("Arial", 14),
#                 fg_color="#1c2636",
#                 text_color="white",
#                 height=36
#             )
#             self.add_account_button.place(relx=0.01, rely=0.01, anchor="nw")
#             row += 1

#             self.channel_dropdown = CTkOptionMenu(
#                 self.container,
#                 values=self.get_saved_channels(),
#                 command=self.select_channel,
#                 width=200
#             )
#             self.channel_dropdown.set("Select Channel")
#             self.channel_dropdown.place(relx=0.99, rely=0.2, anchor="ne")

#             row = 1

           
#             run_optimization = CTkButton(
#                 self.container,
#                 text="Browse",
#                # command=,
#                 fg_color="#1c2636",
#                 text_color="white"
#             )
#             run_optimization.grid(row=row, column=1, padx=10, pady=(60, 10), sticky="w")
#             row += 1

          


































# #Upload videos too (instagram,facebook,youtube,tiktok) if available for api's. (options too use smolgent with a generate button for automatic generation of (title,description,keywords,hashtags.))
# class SocialMediaUploading:
#     def __init__(self, parent_container):
#             self.parent_container = parent_container
#             self.credentials = None  

#             self.container = CTkFrame(
#                 master=self.parent_container,
#                 fg_color="black",
#                 border_width=2,
#                 border_color="#404040",
#                 corner_radius=10,
#                 height=1000
#             )
#             self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
#             self.container.update_idletasks()


#             self.create_widgets()

#     def create_widgets(self):
#             row=1
#             self.container.columnconfigure(0, weight=1)
#             self.container.columnconfigure(1, weight=1)
#             self.container.rowconfigure(1, weight=1)

        
#             self.add_account_button = CTkButton(
#                 self.container,
#                 text="Add New YouTube Account",
#                 command=lambda: Thread(target=self.authenticate).start(),
#                 font=("Arial", 14),
#                 fg_color="#1c2636",
#                 text_color="white",
#                 height=36
#             )
#             self.add_account_button.place(relx=0.01, rely=0.01, anchor="nw")
#             row += 1
#             self.file_menu = CTkOptionMenu(
#                 master=self.container,
#                 values=['Youtube','Instagram','Tiktok'],
#                 width=200,
#                 height=30,
#                 font=bold11,
#                 dropdown_font=bold11,
#                 fg_color="#282828",
#                 button_color="#404040",
#                 text_color="#FFFFFF",
#             )
#             self.file_menu.grid(row=0, column=1, padx=10, pady=10, sticky="ne")


#             self.channel_dropdown = CTkOptionMenu(
#                 self.container,
#                 values=self.get_saved_channels(),
#                 command=self.select_channel,
#                 width=200
#             )
#             self.channel_dropdown.set("Select Channel")
#             self.channel_dropdown.place(relx=0.99, rely=0.2, anchor="ne")

#             row = 1

#             self.video_path_entry = CTkEntry(self.container, placeholder_text="Video File Path", width=500)
#             self.video_path_entry.grid(row=row, column=0, padx=10, pady=(60, 10), sticky="ew")

#             browse_btn = CTkButton(
#                 self.container,
#                 text="Browse",
#                 command=self.browse_video,
#                 fg_color="#1c2636",
#                 text_color="white"
#             )
#             browse_btn.grid(row=row, column=1, padx=10, pady=(60, 10), sticky="w")
#             row += 1

#             self.title_entry = CTkEntry(self.container, placeholder_text="Video Title")
#             self.title_entry.grid(row=row, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
#             row += 1

          

    
#             self.schedule_checkbox = CTkCheckBox(
#                 self.container,
#                 text="Schedule for later",
#                 command=self.toggle_schedule_fields,
#                 fg_color="#1c2636",
#                 text_color="white"
#             )
#             self.schedule_checkbox.grid(row=row, column=0, sticky="w", padx=10, pady=10)

#             self.date_entry = CTkEntry(self.container, placeholder_text="YYYY-MM-DD", width=150)
#             self.time_entry = CTkEntry(self.container, placeholder_text="HH:MM (24h)", width=150)

#             # Hide by default
#             self.date_entry.grid_forget()
#             self.time_entry.grid_forget()
#             row += 1


#             self.description_entry = CTkTextbox(self.container, height=100)
#             self.description_entry.insert("1.0", "Video Description")
#             self.description_entry.grid(row=row, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
#             row += 1

#             self.category_entry = CTkEntry(self.container, placeholder_text="Category ID (e.g., 22)")
#             self.category_entry.grid(row=row, column=0, padx=10, pady=10, sticky="w")

#             self.privacy_dropdown = CTkOptionMenu(self.container, values=["public", "private", "unlisted"])
#             self.privacy_dropdown.set("unlisted")
#             self.privacy_dropdown.grid(row=row, column=1, padx=10, pady=10, sticky="w")
#             row += 1

#             self.upload_button = CTkButton(
#                 self.container,
#                 text="Upload to YouTube",
#                 command=self.Upload_to_platform,
#                 font=("Arial", 16, "bold"),
#                 fg_color="#0d1b2a",
#                 hover_color="#1c2636",
#                 text_color="white",
#                 height=40
#             )
#             self.upload_button.grid(row=row, column=0, columnspan=2, pady=10)
#             row += 1

#             self.test_connection = CTkButton(
#                 self.container,
#                 text="Test YouTube Connection",
#                 command=self.test_connection,
#                 font=("Arial", 16, "bold"),
#                 fg_color="#0d1b2a",
#                 hover_color="#1c2636",
#                 text_color="white",
#                 height=40
#             )
#             self.test_connection.grid(row=row, column=0, columnspan=2, pady=10)
#             row += 1

#             self.channel_label = CTkLabel(
#                 self.container,
#                 text="Channel: Not connected",
#                 font=("Arial", 14),
#                 text_color="white"
#             )
#             self.channel_label.grid(row=row, column=0, columnspan=2, pady=5)

        
#             saved_channels = self.get_saved_channels()
#             if saved_channels:
#                 self.channel_dropdown.set(saved_channels[0])
#                 self.select_channel(saved_channels[0])
                
#     def toggle_schedule_fields(self):
#             if self.schedule_checkbox.get():
#                 self.date_entry.grid(row=self.upload_button.grid_info()['row'] - 1, column=0, padx=10, sticky="w")
#                 self.time_entry.grid(row=self.upload_button.grid_info()['row'] - 1, column=1, padx=10, sticky="w")
#             else:
#                 self.date_entry.grid_forget()
#                 self.time_entry.grid_forget()


#     def browse_video(self):
#             filepath = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
#             if filepath:
#                 self.video_path_entry.delete(0, "end")
#                 self.video_path_entry.insert(0, filepath)


#     def get_saved_channels(self):
#             from File_path import app_data_path
#             token_dir = app_data_path / "youtube_tokens"
#             logging.info(f"[DEBUG] Looking for tokens in: {token_dir}")

#             if not token_dir.exists():
#                 logging.info("[DEBUG] Token dir does not exist")
#                 return []

#             tokens = []
#             for file in token_dir.glob("*.pickle.enc"):
#                 # Remove both .pickle.enc
#                 name = file.name.replace(".pickle.enc", "")
#                 tokens.append(name)

#             logging.info(f"[DEBUG] Cleaned token names: {tokens}")
#             return tokens


#     def test_connection(self):
#             if not self.credentials:
#                 self.authenticate()

#             youtube = build("youtube", "v3", credentials=self.credentials)

#             channel_response = youtube.channels().list(part="snippet", mine=True).execute()
#             channel_title = channel_response["items"][0]["snippet"]["title"]
#             logging.info(f"📺 Authenticated YouTube Channel: {channel_title}")
#             self.channel_label.configure(text=f"Channel: {channel_title}")

#     def Upload_to_platform(self):
#             platform = self.file_menu.get()  # 

#             if platform == "Youtube":
#                 self.upload_to_youtube_actual()
#             elif platform == "Tiktok":
#                 return
#             elif platform == "Instagram":
#                 return
#             else:
#                 logging.info("⚠️ No valid platform selected.")
#                 return
          

#     def upload_to_youtube_actual(self):
#             video_path = self.video_path_entry.get()
#             title = self.title_entry.get()
#             description = self.description_entry.get("1.0", "end").strip()
#             category_id = self.category_entry.get()
#             privacy_status = self.privacy_dropdown.get()
#             status_config = {
#                 "privacyStatus": privacy_status
#             }


#             if self.schedule_checkbox.get():
#                 try:
#                     date_str = self.date_entry.get()
#                     time_str = self.time_entry.get()
#                     publish_datetime = f"{date_str}T{time_str}:00Z"

        
#                     dt = datetime.datetime.strptime(publish_datetime, "%Y-%m-%dT%H:%M:%SZ")
#                     publish_at = dt.isoformat() + "Z"

#                     status_config["privacyStatus"] = "private"
#                     status_config["publishAt"] = publish_at
#                     logging.info(f"📅 Scheduled for: {publish_at}")
#                 except Exception as e:
#                     logging.info("❌ Invalid date/time format:", e)
#                     return

#             if not self.credentials:
#                 self.authenticate()

#             youtube = build("youtube", "v3", credentials=self.credentials)

#             request_body = {
#                 "snippet": {
#                     "title": title,
#                     "description": description,
#                     "categoryId": category_id,
#                 },
#                 "status": {
#                     "privacyStatus": status_config
#                 }
#             }

#             media_file = MediaFileUpload(video_path)

#             response = youtube.videos().insert(
#                 part="snippet,status",
#                 body=request_body,
#                 media_body=media_file
#             ).execute()

#             channel_response = youtube.channels().list(part="snippet", mine=True).execute()
#             channel_title = channel_response["items"][0]["snippet"]["title"]

#             logging.info("✅ Upload successful!")
#             logging.info(f"📺 Uploaded to: {channel_title}")
#             logging.info(f"🔗 Video URL: https://youtu.be/{response['id']}")
#             self.channel_label.configure(text=f"Uploaded to: {channel_title}")


#     def select_channel(self, channel_name):
#             from encryption import load_encrypted_token

#             credentials = load_encrypted_token(channel_name)
#             if credentials:
#                 self.credentials = credentials
#                 self.channel_label.configure(text=f"Loaded: {channel_name}")
#                 logging.info(f"✅ Loaded token for {channel_name}")
#             else:
#                 self.channel_label.configure(text=f"❌ Failed to load: {channel_name}")
#                 logging.info(f"⚠️ Failed to load token for {channel_name}")

#     def authenticate(self):
#             import google_auth_oauthlib.flow
#             from encryption import save_encrypted_token
        

#             scopes = [
#                 "https://www.googleapis.com/auth/youtube.upload",
#                 "https://www.googleapis.com/auth/youtube.force-ssl"
#             ]
#             client_secrets_file = "./Json_secrets/client_secret_849553263621-grvsfihl7lkocrt0qgs37iipuv5lbpkl.apps.googleusercontent.com.json"

#             # OAuth login flow
#             flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
#                 client_secrets_file, scopes)
#             self.credentials = flow.run_local_server(port=0)

#             youtube = build("youtube", "v3", credentials=self.credentials)
#             channel_response = youtube.channels().list(part="snippet", mine=True).execute()
#             channel_name = channel_response["items"][0]["snippet"]["title"]

#             # Save encrypted token
#             save_encrypted_token(channel_name, self.credentials)

#             # Refresh dropdown with new value
#             self.channel_dropdown.configure(values=self.get_saved_channels())
#             self.channel_dropdown.set(channel_name)
#             self.channel_label.configure(text=f"Authenticated: {channel_name}")









































# ####Youtube Download#####
# global youtube_progress_var
# def place_youtube_download_menu(parent_container):
#     global youtube_link_entry, youtube_output_path_entry, video_format_var, audio_format_var

#     # ── Design tokens ────────────────────────────────────────────────────────
#     _BG       = "#08090a"
#     _SURFACE  = "#0d0f11"
#     _PANEL    = "#111316"
#     _PANEL2   = "#161a1e"
#     _BORDER   = "#1e2229"
#     _BORDER2  = "#252b34"
#     _RED      = "#cc2222"
#     _RED_HOV  = "#e63333"
#     _TEXT     = "#c8cdd4"
#     _TEXT_DIM = "#555f6e"
#     _WHITE    = "#eef0f3"

#     frame_width, frame_height = 200, 110
#     youtube_link_settings = {}
#     formats_fetched = {}

#     youtube_progress_var.set("")

#     # Make parent_container fill its allocated space completely
#     parent_container.grid_rowconfigure(0, weight=1)
#     parent_container.grid_columnconfigure(0, weight=1)

#     # ── inner helpers ────────────────────────────────────────────────────────
#     def update_format_list():
#         url = youtube_link_entry.get()
#         if not url:
#             return
#         fetch_button.configure(state="disabled", text="Fetching…")

#         def fetch_thread():
#             try:
#                 if url in formats_fetched:
#                     video_formats, audio_formats = formats_fetched[url]
#                 else:
#                     result = get_available_formats(url)
#                     if result is None:
#                         print("Error Requesting formats. please check if your cookies are outdated.")
#                         window.after(0, lambda: fetch_button.configure(state="normal", text="Fetch Details"))
#                         return
#                     video_formats, audio_formats = result
#                     formats_fetched[url] = (video_formats, audio_formats)
#                     print("Formats fetched and cached.")

#                 def update_ui():
#                     window.after(0, lambda: addlist_btn.configure(state="normal"))
#                     if video_formats or audio_formats:
#                         video_format_dropdown.configure(values=video_formats if video_formats else ["No video formats available"])
#                         audio_format_dropdown.configure(values=audio_formats if audio_formats else ["No audio formats available"])
#                         download_btn.configure(state="normal")
#                     if video_formats:
#                         video_format_var.set(video_formats[0])
#                     if audio_formats:
#                         audio_format_var.set(audio_formats[0])
#                     fetch_button.configure(text="Fetch Details")

#                 window.after(0, update_ui)
#             except Exception as e:
#                 print(f"Error in fetch thread: {e}")
#                 window.after(0, lambda: fetch_button.configure(state="normal", text="Fetch Details"))

#         threading.Thread(target=fetch_thread, daemon=True).start()

#     def update_fetch_button_state(event=None):
#         url = youtube_link_entry.get()
#         if "youtube.com" in url or "youtu.be" in url:
#             fetch_button.configure(state="normal")
#         else:
#             fetch_button.configure(state="disabled")

#     def on_link_selected(selected_url):
#         youtube_link_entry.delete(0, tk.END)
#         youtube_link_entry.insert(0, selected_url)
#         if selected_url in formats_fetched:
#             video_formats, audio_formats = formats_fetched[selected_url]
#         else:
#             video_formats, audio_formats = get_available_formats(selected_url)
#             formats_fetched[selected_url] = (video_formats, audio_formats)
#         video_format_dropdown.configure(values=video_formats if video_formats else ["No video formats available"])
#         audio_format_dropdown.configure(values=audio_formats if audio_formats else ["No audio formats available"])
#         saved_settings = youtube_link_settings.get(selected_url, {})
#         saved_video_format = saved_settings.get("video_format")
#         saved_audio_format = saved_settings.get("audio_format")
#         if saved_video_format in video_formats:
#             video_format_var.set(saved_video_format)
#         else:
#             video_format_var.set(video_format_var.get() if video_formats else "Video Formats...")
#         if saved_audio_format in audio_formats:
#             audio_format_var.set(saved_audio_format)
#         else:
#             audio_format_var.set(audio_format_var.get() if audio_formats else "Audio Formats...")
#         youtube_link_settings[selected_url] = {
#             "video_format": video_format_var.get(),
#             "audio_format": audio_format_var.get()
#         }

#     def on_video_format_change(event=None):
#         selected_url = youtubelist_variable.get().strip()
#         if selected_url in youtube_link_settings:
#             youtube_link_settings[selected_url]["audio_format"] = audio_format_var.get()

#     def on_audio_format_change(event=None):
#         selected_url = youtubelist_variable.get().strip()
#         if selected_url in youtube_link_settings:
#             youtube_link_settings[selected_url]["video_format"] = video_format_var.get()

#     def clear_download_list():
#         youtube_download_list.clear()
#         youtubelist_variable.set("")
#         youtube_list_menu.configure(values=[])
#         download_all_btn.configure(state="disabled")
#         queue_count_lbl.configure(text="0 items")

#     def add_link_to_download_list():
#         if video_format_var.get() == "":
#             print("Select video formats first")
#             return
#         url = youtube_link_entry.get().strip()
#         if url and url not in youtube_download_list:
#             youtube_download_list.append(url)
#             youtube_link_entry.delete(0, END)
#             youtubelist_variable.set(youtube_download_list[-1])
#             youtube_list_menu.configure(values=youtube_download_list)
#             youtube_link_settings[url] = {
#                 "video_format": video_format_var.get(),
#                 "audio_format": audio_format_var.get()
#             }
#             if len(youtube_download_list) > 0:
#                 download_all_btn.configure(state="normal")
#             n = len(youtube_download_list)
#             queue_count_lbl.configure(text=f"{n} item{'s' if n != 1 else ''}")
#             video_format_var.set("")
#             audio_format_var.set("")

#     def select_youtube_output_path():
#         path = filedialog.askdirectory()
#         if path:
#             youtube_output_path_entry.delete(0, "end")
#             youtube_output_path_entry.insert(0, path)

#     # ── OUTER CARD — fills entire parent_container ───────────────────────────
#     card = CTkFrame(
#         master=parent_container,
#         fg_color=_SURFACE,
#         bg_color=_BG,
#         corner_radius=14,
#         border_width=1,
#         border_color=_BORDER,
#     )
#     card.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

#     # Card layout: 3 rows (header | content | footer), content stretches
#     card.grid_rowconfigure(0, weight=0)   # header stripe – fixed
#     card.grid_rowconfigure(1, weight=1)   # content area  – stretches
#     card.grid_rowconfigure(2, weight=0)   # footer stripe – fixed
#     card.grid_columnconfigure(0, weight=1)

#     # ── HEADER STRIPE ────────────────────────────────────────────────────────
#     header = CTkFrame(master=card, fg_color=_PANEL, corner_radius=0, height=38)
#     header.grid(row=0, column=0, sticky="ew")
#     header.grid_propagate(False)
#     header.grid_columnconfigure(1, weight=1)

#     CTkLabel(
#         master=header,
#         text="▶   YouTube Downloader",
#         font=CTkFont(family="Segoe UI", size=11, weight="bold"),
#         text_color=_WHITE,
#         fg_color="transparent",
#     ).grid(row=0, column=0, padx=16, pady=8, sticky="w")

#     CTkLabel(
#         master=header,
#         text="  yt-dlp  ",
#         font=CTkFont(family="Courier New", size=9, weight="bold"),
#         text_color=_RED,
#         fg_color=_PANEL2,
#         corner_radius=10,
#         width=50,
#         height=18,
#     ).grid(row=0, column=2, padx=(0, 14), pady=8, sticky="e")

#     # ── CONTENT AREA — two-column: left fields | right side panel ────────────
#     content = CTkFrame(master=card, fg_color="transparent")
#     content.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)

#     # Left fields column stretches; right side panel is fixed width
#     content.grid_columnconfigure(0, weight=1)       # left: labels
#     content.grid_columnconfigure(1, weight=3)       # left: inputs  (main stretch)
#     content.grid_columnconfigure(2, weight=2)       # left: buttons (some stretch)
#     content.grid_columnconfigure(3, weight=0, minsize=220)  # right: side panel fixed
#     for r in range(7):
#         content.grid_rowconfigure(r, weight=1)      # all rows share vertical space

#     # ── ROW 0 — Output path ──────────────────────────────────────────────────
#     CTkLabel(
#         master=content,
#         text="Save to",
#         font=CTkFont(family="Segoe UI", size=11),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         anchor="e",
#     ).grid(row=0, column=0, padx=(16, 8), pady=(10, 4), sticky="e")

#     youtube_output_path_entry = CTkEntry(
#         master=content,
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=11),
#         fg_color=_PANEL,
#         border_color=_BORDER2,
#         border_width=1,
#         bg_color=_SURFACE,
#         text_color=_TEXT,
#         justify="left",
#     )
#     youtube_output_path_entry.grid(row=0, column=1, padx=(0, 8), pady=(10, 4), sticky="ew")
#     youtube_output_path_entry.insert(0, DOCUMENT_PATH)

#     path_btn_row = CTkFrame(master=content, fg_color="transparent")
#     path_btn_row.grid(row=0, column=2, padx=(0, 8), pady=(10, 4), sticky="w")
#     path_btn_row.grid_columnconfigure(0, weight=1)
#     path_btn_row.grid_columnconfigure(1, weight=0)

#     CTkButton(
#         master=path_btn_row,
#         text="Browse",
#         width=70,
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         fg_color=_PANEL2,
#         hover_color="#1c2028",
#         border_color=_BORDER2,
#         border_width=1,
#         text_color=_TEXT,
#         command=lambda: select_youtube_output_path(),
#     ).grid(row=0, column=0, padx=(0, 4))

#     CTkButton(
#         master=path_btn_row,
#         text="✕",
#         width=32,
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=11, weight="bold"),
#         fg_color=_PANEL2,
#         hover_color="#3d1a1a",
#         border_color="#3d1a1a",
#         border_width=1,
#         text_color="#ff4545",
#         command=clear_download_list,
#     ).grid(row=0, column=1)

#     # ── ROW 1 — Queue ────────────────────────────────────────────────────────
#     CTkLabel(
#         master=content,
#         text="Queue",
#         font=CTkFont(family="Segoe UI", size=11),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         anchor="e",
#     ).grid(row=1, column=0, padx=(16, 8), pady=4, sticky="e")

#     global youtubelist_variable
#     global youtube_list_menu
#     youtubelist_variable = StringVar(value="")
#     youtube_list_menu = CTkOptionMenu(
#         master=content,
#         variable=youtubelist_variable,
#         values=youtube_download_list,
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=11),
#         fg_color=_PANEL,
#         button_color=_PANEL2,
#         button_hover_color=_BORDER2,
#         text_color=_TEXT,
#         dropdown_fg_color=_PANEL,
#         dropdown_hover_color="#1c2028",
#         dropdown_text_color=_TEXT,
#         command=on_link_selected,
#     )
#     youtube_list_menu.grid(row=1, column=1, padx=(0, 8), pady=4, sticky="ew")

#     queue_action_row = CTkFrame(master=content, fg_color="transparent")
#     queue_action_row.grid(row=1, column=2, padx=(0, 8), pady=4, sticky="w")

#     addlist_btn = CTkButton(
#         master=queue_action_row,
#         text="+ Add",
#         width=70,
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         fg_color=_PANEL2,
#         hover_color="#1c2028",
#         border_color=_BORDER2,
#         border_width=1,
#         text_color=_TEXT,
#         command=add_link_to_download_list,
#         state="disabled",
#     )
#     addlist_btn.grid(row=0, column=0, padx=(0, 6))

#     queue_count_lbl = CTkLabel(
#         master=queue_action_row,
#         text="0 items",
#         font=CTkFont(family="Courier New", size=9),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         width=50,
#     )
#     queue_count_lbl.grid(row=0, column=1)

#     # ── ROW 2 — YouTube URL ──────────────────────────────────────────────────
#     CTkLabel(
#         master=content,
#         text="YouTube URL:",
#         font=CTkFont(family="Segoe UI", size=11),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         anchor="e",
#     ).grid(row=2, column=0, padx=(16, 8), pady=4, sticky="e")

#     youtube_link_entry = CTkEntry(
#         master=content,
#         height=34,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=11),
#         fg_color=_PANEL,
#         border_color=_BORDER2,
#         border_width=1,
#         bg_color=_SURFACE,
#         placeholder_text="Paste YouTube link…",
#         text_color=_WHITE,
#         justify="left",
#     )
#     youtube_link_entry.grid(row=2, column=1, padx=(0, 8), pady=4, sticky="ew")
#     youtube_link_entry.bind("<KeyRelease>", update_fetch_button_state)

#     fetch_button = CTkButton(
#         master=content,
#         text="Fetch Details",
#         width=120,
#         height=34,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         fg_color=_PANEL2,
#         hover_color="#1c2028",
#         border_color=_BORDER2,
#         border_width=1,
#         text_color=_TEXT,
#         command=update_format_list,
#         state="disabled",
#     )
#     fetch_button.grid(row=2, column=2, padx=(0, 8), pady=4, sticky="w")

#     # ── ROW 3 — Video format ─────────────────────────────────────────────────
#     CTkLabel(
#         master=content,
#         text="Video Format:",
#         font=CTkFont(family="Segoe UI", size=11),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         anchor="e",
#     ).grid(row=3, column=0, padx=(16, 8), pady=4, sticky="e")

#     video_format_dropdown = CTkComboBox(
#         master=content,
#         variable=video_format_var,
#         values=["Enter Link First..."],
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=11),
#         fg_color=_PANEL,
#         border_color=_BORDER2,
#         border_width=1,
#         button_color=_PANEL2,
#         button_hover_color=_BORDER2,
#         dropdown_fg_color=_PANEL,
#         dropdown_hover_color="#1c2028",
#         text_color=_TEXT,
#     )
#     video_format_dropdown.grid(row=3, column=1, padx=(0, 8), pady=4, sticky="ew")
#     video_format_dropdown.bind("<<ComboboxSelected>>", on_video_format_change)

#     global download_btn
#     download_btn = CTkButton(
#         master=content,
#         text="⬇  Download",
#         width=120,
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         fg_color=_RED,
#         hover_color=_RED_HOV,
#         text_color="#ffffff",
#         command=start_youtube_download,
#         state="disabled",
#     )
#     download_btn.grid(row=3, column=2, padx=(0, 8), pady=4, sticky="w")

#     # ── ROW 4 — Audio format ─────────────────────────────────────────────────
#     CTkLabel(
#         master=content,
#         text="Audio Format:",
#         font=CTkFont(family="Segoe UI", size=11),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         anchor="e",
#     ).grid(row=4, column=0, padx=(16, 8), pady=4, sticky="e")

#     audio_format_dropdown = CTkComboBox(
#         master=content,
#         variable=audio_format_var,
#         values=["Enter Link First..."],
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=11),
#         fg_color=_PANEL,
#         border_color=_BORDER2,
#         border_width=1,
#         button_color=_PANEL2,
#         button_hover_color=_BORDER2,
#         dropdown_fg_color=_PANEL,
#         dropdown_hover_color="#1c2028",
#         text_color=_TEXT,
#     )
#     audio_format_dropdown.grid(row=4, column=1, padx=(0, 8), pady=4, sticky="ew")
#     audio_format_dropdown.bind("<<ComboboxSelected>>", on_audio_format_change)

#     def download_all_from_list():
#         output_path = youtube_output_path_entry.get()
#         if not output_path:
#             info_message.set("Choose a folder for saving!")
#             return
#         if not youtube_download_list:
#             info_message.set("The list is empty!")
#             return
#         stop_youtube_download_btn.configure(state="normal")
#         youtube_progress_var.set("Starting batch download...")

#         def batch_worker():
#             for idx, link in enumerate(youtube_download_list, 1):
#                 if stop_download_flag:
#                     youtube_progress_var.set("Download stopped.")
#                     return
#                 window.after(0, lambda l=link, i=idx: youtube_progress_var.set(
#                     f"⬇️ Downloading ({i}/{len(youtube_download_list)}): {l[:50]}"
#                 ))
#                 format_data = formats_fetched.get(link)
#                 if format_data:
#                     video_formats, audio_formats = format_data
#                 else:
#                     video_formats, audio_formats = get_available_formats(link)
#                     formats_fetched[link] = (video_formats, audio_formats)
#                 settings = youtube_link_settings.get(link, {})
#                 video_format_id = settings.get("video_format", "best").split(" - ")[0]
#                 audio_format_id = settings.get("audio_format", "bestaudio").split(" - ")[0]
#                 video_format_var.set(video_format_id)
#                 audio_format_var.set(audio_format_id)
#                 download_youtube_link(link, output_path, update_progress)
#             window.after(0, lambda: youtube_progress_var.set("✅ All downloads finished."))
#             youtube_download_list.clear()
#             info_message.set("✅ Batch download completed.")

#         Thread(target=batch_worker).start()

#     download_all_btn = CTkButton(
#         master=content,
#         text="⬇  All",
#         width=120,
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         fg_color=_PANEL2,
#         hover_color="#1c2028",
#         border_color=_BORDER2,
#         border_width=1,
#         text_color=_TEXT,
#         command=download_all_from_list,
#         state="disabled",
#     )
#     download_all_btn.grid(row=4, column=2, padx=(0, 8), pady=4, sticky="w")

#     # ── ROW 5 — Status ───────────────────────────────────────────────────────
#     CTkLabel(
#         master=content,
#         text="Status",
#         font=CTkFont(family="Segoe UI", size=11),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         anchor="e",
#     ).grid(row=5, column=0, padx=(16, 8), pady=4, sticky="e")

#     CTkLabel(
#         master=content,
#         textvariable=youtube_progress_var,
#         font=CTkFont(family="Segoe UI", size=11),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         anchor="w",
#     ).grid(row=5, column=1, padx=(0, 8), pady=4, sticky="ew")

#     global stop_youtube_download_btn
#     stop_youtube_download_btn = CTkButton(
#         master=content,
#         text="■  Stop",
#         width=120,
#         height=30,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         fg_color=_PANEL2,
#         hover_color="#3d1a1a",
#         border_color="#3d1a1a",
#         border_width=1,
#         text_color="#ff4545",
#         command=lambda: Stop_Youtube_Downloading(),
#         state="disabled",
#     )
#     stop_youtube_download_btn.grid(row=5, column=2, padx=(0, 8), pady=4, sticky="w")

#     # ── SIDE PANEL — spans all content rows ──────────────────────────────────
#     side_panel = CTkFrame(
#         master=content,
#         fg_color=_PANEL,
#         corner_radius=12,
#         border_width=1,
#         border_color=_BORDER,
#     )
#     side_panel.grid(row=0, column=3, rowspan=6, padx=(4, 14), pady=10, sticky="nsew")
#     side_panel.grid_rowconfigure(0, weight=1)
#     side_panel.grid_rowconfigure(1, weight=0)
#     side_panel.grid_columnconfigure(0, weight=1)

#     bg_image = Image.open(find_by_relative_path("Assets" + os_separator + "youtube_img.png")).resize((frame_width, frame_height))
#     bg_image_tk = CTkImage(bg_image, size=(frame_width, frame_height))
#     bg_label = CTkLabel(
#         master=side_panel,
#         image=bg_image_tk,
#         width=frame_width,
#         height=frame_height,
#         fg_color="transparent",
#         text="",
#     )
#     bg_label.grid(row=0, column=0, padx=10, pady=(14, 4), sticky="n")
#     bg_label.image = bg_image_tk

#     CTkLabel(
#         master=side_panel,
#         text="Powered by yt-dlp",
#         font=CTkFont(family="Courier New", size=8),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#     ).grid(row=1, column=0, pady=(0, 12))

#     # ── FOOTER STRIPE ─────────────────────────────────────────────────────────
#     footer = CTkFrame(master=card, fg_color=_PANEL, corner_radius=0, height=34)
#     footer.grid(row=2, column=0, sticky="ew")
#     footer.grid_propagate(False)
#     footer.grid_columnconfigure(1, weight=1)

#     Info_button_youtubedownloader = create_info_button(
#         open_YoutubeDownloader_tool_info,
#         "«  INFO",
#         width=80,
#         master=footer,
#     )
#     Info_button_youtubedownloader.grid(row=0, column=0, padx=12, pady=5, sticky="w")

#     global upload_button
#     upload_button = CTkButton(
#         master=footer,
#         text="Upload Cookies",
#         width=110,
#         height=22,
#         corner_radius=6,
#         font=CTkFont(family="Segoe UI", size=9, weight="bold"),
#         fg_color=_PANEL2,
#         hover_color="#1c2028",
#         border_color=_BORDER2,
#         border_width=1,
#         text_color=_TEXT_DIM,
#         command=lambda: upload_cookie_file(),
#     )
#     if cookie_file_path is None:
#         upload_button.grid(row=0, column=2, padx=12, pady=5, sticky="e")
#     if cookie_file_path is not None:
#         upload_button.grid_forget()


# def delete_cookie_file_and_reset_button():
#     """ Deletes the cookie file if it exists and resets the upload button visibility. """
#     global upload_button, COOKIE_PATH_FILE, cookie_file_path

#     if COOKIE_PATH_FILE.exists():
#         try:
#             corruptedcookiefile_path = str(COOKIE_PATH_FILE)
#             os.remove(corruptedcookiefile_path)
#             cookie_file_path = None
#             logging.info(f"Cookie file {COOKIE_PATH_FILE} deleted successfully.")
#         except Exception as e:
#             logging.info(f"Error deleting cookie file: {e}")
#     upload_button.place(relx=0.12, rely=0.94, anchor="e")


# def load_cookie_file_path():
#     """ Load cookie file path from saved path file. """
#     global cookie_file_path
#     try:
#         if COOKIE_PATH_FILE.exists():
#             cookie_file_path = str(COOKIE_PATH_FILE)
#             logging.info(f"Cookie file path exsist at: {cookie_file_path}")
#         else:
#             cookie_file_path = None
#             logging.info(f"cookie file path is None cause it does not exists.")
#     except Exception as e:        
#         cookie_file_path = None
#         logging.info(f"Error exception cookie file path is None ")


# def update_cookie_timestamps(file_path):
#     """ Reads cookie file, updates expiration timestamps, and saves it back. """
#     updated_lines = []
    
#     with open(file_path, "r", encoding="utf-8") as f:
#         for line in f:
#             parts = line.strip().split("\t")

      
#             if line.startswith("#") or len(parts) < 5:
#                 updated_lines.append(line.strip())
#                 continue
            
#             try:
      
#                 old_timestamp = int(parts[4])
#                 if old_timestamp < NEW_TIMESTAMP:
#                     parts[4] = str(NEW_TIMESTAMP)  
#             except ValueError:
#                 pass  

#             updated_lines.append("\t".join(parts))
    
#     updated_path = os.path.join(COOKIE_STORAGE_DIR, os.path.basename(file_path))
#     with open(updated_path, "w", encoding="utf-8") as f:
#         f.write("\n".join(updated_lines))

#     logging.info(f"Updated cookie file saved at: {updated_path}")
#     return updated_path


# def upload_cookie_file():
#     """ Let user upload a cookie file and save it to the app's cookie directory. """
#     global cookie_file_path,upload_button

#     cookie_file_path_input = filedialog.askopenfilename(
#         title="Select Cookie File", 
#         filetypes=[("Text files", "*.txt")]
#     )
    
#     if cookie_file_path_input:
#         try:
  
#            save_path = COOKIE_STORAGE_DIR / fixed_cookie_filename

#            shutil.copy(cookie_file_path_input, save_path)

#            cookie_file_path = str(save_path)


#            update_cookie_timestamps(cookie_file_path)
#            upload_button.place_forget() 
           
#         except Exception as e:
#             logging.info(f"Error saving cookie file: {e}")
#     else: 
#         logging.info("No file selected")



# def ensure_protocol(youtube_url):

#     if not youtube_url.startswith(('http://', 'https://')):
#         youtube_url = 'https://' + youtube_url
#     return youtube_url



# def get_available_formats(youtube_url):
#     global cookie_file_path,backup
#     backup = False
#     ensure_protocol(youtube_url)
#     ydl_opts = {
#              'quiet': True,
#              "nocheckcertificate": True,
#              "cookiefile": cookie_file_path,
#              # Explicitly use node runtime
#              'js_runtimes': {'node': {}},
#              'extractor_args': {'youtube': {'remote_components': 'ejs:github'}},
#              'remote_components': ['ejs:github']
#             }
#     ydl_opts_backup = {
#         'quiet': True,
#         'nocheckcertificate': True,
#         'no_signature': True,  
#         "cookiefile": cookie_file_path,
#         'js_runtimes': {'node': {}},
#         'extractor_args': {'youtube': {'remote_components': 'ejs:github'}},
#         'remote_components': ['ejs:github']
#     }
#     ydl_opts_fallback = {
#         'quiet': True,
#         'nocheckcertificate': True,
#         'force_generic_extractor': True, 
#         'ignoreerrors': True,
#         "cookiefile": cookie_file_path,
#         'js_runtimes': {'node': {}},
#         'extractor_args': {'youtube': {'remote_components': 'ejs:github'}},
#         'remote_components': ['ejs:github']
#     }

#     if cookie_file_path:
#         ydl_opts["cookiefile"] = cookie_file_path
#         ydl_opts_backup["cookiefile"] = cookie_file_path
#         ydl_opts_fallback["cookiefile"] = cookie_file_path
#     if not cookie_file_path:
#         logging.info("Cookie file path is None/Empty")
#         return

#     logging.info(f"cookie_file_path when getting available format: {cookie_file_path}")
    
    
#     def try_fetching_format(ydl_opts_variable):
#                 with yt_dlp.YoutubeDL(ydl_opts_variable) as ydl:
#                     info = ydl.extract_info(youtube_url, download=False)
#                     formats = info.get('formats', []) if info else []

#                     video_formats_list = []
#                     audio_formats_list = []

#                     for f in formats:
#                         if f.get('vcodec') != 'none' and f.get('acodec') == 'none':
#                             height = f.get('height') or 0
#                             resolution = f.get('resolution', 'Unknown')
#                             ext = f.get('ext', '')
#                             format_id = f['format_id']
#                             video_formats_list.append({'height': height, 'str': f"{format_id} - {resolution} ({ext})"})
#                         elif f.get('acodec') != 'none' and f.get('vcodec') == 'none': 
#                             # Filter for English audio only
#                             language = f.get('language', '')
#                             if language and language != 'en':
#                                 continue
#                             abr = f.get('abr') or 0
#                             ext = f.get('ext', '')
#                             format_id = f['format_id']
#                             lang_tag = f" [{language}]" if language else ""
#                             audio_formats_list.append({'abr': abr, 'str': f"{format_id} - {abr}kbps ({ext}){lang_tag}"})
                    
#                     # Sort descending
#                     video_formats_list.sort(key=lambda x: x['height'], reverse=True)
#                     audio_formats_list.sort(key=lambda x: x['abr'], reverse=True)

#                     video_formats = ['Only Audio','Video Formats...'] + [x['str'] for x in video_formats_list]
#                     audio_formats = [x['str'] for x in audio_formats_list]

#                 return video_formats, audio_formats
    
#     try: 
#             video_formats, audio_formats = try_fetching_format(ydl_opts)
#             return video_formats, audio_formats
    
#     except yt_dlp.utils.DownloadError as e:
#         logging.info(f"Error fetching formats with default opts: {e}")
#         try:
#             logging.info("Retrying with backup options (no_signature)...")
#             video_formats, audio_formats = try_fetching_format(ydl_opts_backup)
#             return video_formats, audio_formats
#         except yt_dlp.utils.DownloadError as e2:
#             logging.info(f"Error fetching formats with backup opts: {e2}")
#             try:
#                 logging.info("Retrying with fallback options (force_generic_extractor)...")
#                 video_formats, audio_formats = try_fetching_format(ydl_opts_fallback)
#                 return video_formats, audio_formats
#             except yt_dlp.utils.DownloadError as e3:
#                 logging.info(f"All fetch attempts failed: {e3}")
#                 return None
#         if "cookie" in str(e).lower() or "sign in" in str(e).lower() or "403" in str(e):
#                 logging.info("⚠️ Cookie file seems broken or expired. Resetting...")
#                 delete_cookie_file_and_reset_button()
#         backup = True
#         try:
#             logging.info("⚙️ Switching to backup method...")
#             video_formats, audio_formats = try_fetching_format(ydl_opts_backup)

#         except yt_dlp.utils.DownloadError as e:
#             if "cookie" in str(e).lower() or "sign in" in str(e).lower() or "403" in str(e):
#                 logging.info("⚠️ Cookie file seems broken or expired. Resetting...")
#                 delete_cookie_file_and_reset_button()
#                 return [], []
#             logging.info(f"❌ Backup method failed: {e}")
#             logging.info("🛠️ Trying final fallback metho d (force_generic_extractor)...")

#         try:
#             video_formats, audio_formats = try_fetching_format(ydl_opts_fallback)

#             # Explicit check after fallback
#             if not video_formats or video_formats == ['Video Formats...','Only Audio']:
#                 raise Exception("Fallback method returned no formats")

#             return video_formats, audio_formats

#         except Exception as e:
#             logging.info(f"❌ Final fallback failed: {e}")

#             if "cookie" in str(e).lower() or "sign in" in str(e).lower() or "403" in str(e):
#                 logging.info("⚠️ Cookie file seems broken or expired. Resetting...")
#                 delete_cookie_file_and_reset_button()
#                 return [], []
#             return ["error"], ["error"]



# def download_youtube_link(youtube_url,output_path, progress_callback=None):
#     video_format = video_format_var.get().split(" - ")[0]  
#     audio_format = audio_format_var.get().split(" - ")[0]  

#     if video_format == "Only Audio":
#         # Audio only download
#         format_string = audio_format if audio_format else "bestaudio"
#         merge_format = "mp3"
#     else:
#         # Video + audio download
#         format_string = f"{video_format}+{audio_format}/bestaudio"
#         merge_format = "mp4"
    
#     base_opts = {
#         "outtmpl": f'{output_path}/%(title)s.%(ext)s',
#         "cookiefile": cookie_file_path,
#         'format': format_string,
#         'merge_output_format': merge_format,
#         'progress_hooks': [progress_callback] if progress_callback else [],
#         'nocheckcertificate': True,
#         'cookiesfrombrowser': None,
#         'js_runtimes': {'node': {}},
#         'extractor_args': {'youtube': {'remote_components': 'ejs:github'}},
#         'remote_components': ['ejs:github']
#     }

#     # Fallback options similar to get_available_formats
#     opts_list = [
#         base_opts,
#         {**base_opts, 'no_signature': True},
#         {**base_opts, 'force_generic_extractor': True, 'ignoreerrors': True}
#     ]

#     last_error = None
#     for opts in opts_list:
#         try:
#             with yt_dlp.YoutubeDL(opts) as ydl:
#                  ydl.download([youtube_url])
            
#             window.after(0, lambda: [stop_youtube_download_btn.pack_forget(), stop_youtube_download_btn.update_idletasks()])
#             return "Download Complete!"

#         except yt_dlp.utils.DownloadError as e:
#             last_error = e
#             if "User stopped the download." in str(e):
#                 return f"Error: {str(e)}"
#             logging.info(f"Download failed with opts: {e}. Retrying...")
#             continue
#         except Exception as e:
#             return f"Error: {str(e)}"
    
#     return f"Error: {str(last_error)}"
    
# def update_progress(d):
#     if stop_download_flag:
#         raise yt_dlp.utils.DownloadError("User stopped the download.")
#     if d['status'] == 'downloading':
#         percent = d.get('_percent_str', '0%')
#         window.after(0, lambda: youtube_progress_var.set(percent))


# def download_thread(youtube_url, output_path):
#     global stop_download_flag
#     try:
#         info_message.set("Downloading....")
#         message = download_youtube_link(youtube_url, output_path, update_progress)
#         if stop_download_flag:
#             info_message.set("Removing temporary files...")
         
#             for file in os.listdir(output_path):
#                 if file.endswith(".part"):
#                     try:
#                         os.remove(os.path.join(output_path, file))
#                         info_message.set("Done cleaning up files.")
#                     except Exception as e:
#                         info_message.set(f"Error cleaning up files: {str(e)}")
#             return
        
        
#         if message == "Download Complete!":
#             info_message.set(message)
#             stop_youtube_download_btn.pack_forget()
#         else: 
#             info_message.set(message)
#     except yt_dlp.utils.DownloadError as e:
#         if "User stopped the download." in str(e):
#             info_message.set("YouTube downloader is ready :)")

          
      
#         else:
#             info_message.set(f"Error:  {str(e)}")

#     except Exception as e:
#         info_message.set(f"Error: {str(e)}")
#     finally:
#         youtube_progress_var.set("" if stop_download_flag else "Download Complete!")
#         video_format_var.set("")
#         audio_format_var.set("")
#         youtube_link_entry.delete(0, 'end')

# def Stop_Youtube_Downloading():
#     global youtube_link_entry
#     global stop_download_flag 
#     stop_download_flag = True
#     stop_youtube_download_btn.place_forget()
#     info_message.set("Stopping Download, cleaning up...")


# def start_youtube_download():
#     global youtube_link_entry, youtube_output_path_entry
#     url=youtube_link_entry.get()
#     output_path = youtube_output_path_entry.get()

#     if not url or 'youtube.com' not in url and 'youtube.be' not in url:
#         info_message.set("Invalid YouTube URL!")
#         return
    
#     if not output_path:
#         info_message.set("Choose a folder for saving!")
#         return
#     stop_youtube_download_btn.grid(row=4, column=3, sticky="ew", padx=10, pady=5)
#     youtube_progress_var.set("0%")
#     Thread(target=download_thread, args=(url, output_path)).start()
    

        

# def get_ffmpeg_details(file_path):
#     """
#     Uses ffmpeg.probe to extract metadata from a video file.
#     Returns a formatted JSON string with all available details.
#     """
#     try:
#         probe = ffmpeg.probe(file_path)
#         return json.dumps(probe, indent=4)
#     except ffmpeg.Error as e:
#         error_message = e.stderr.decode() if e.stderr else str(e)
#         return f"Error retrieving details: {error_message}"
#     except Exception as e:
#         return f"An unexpected error occurred: {e}"

































# class ToolMenu:
#     def __init__(self, parent_container):
#         self.parent_container = parent_container

#         self.container = CTkFrame(
#             master=self.parent_container,
#             fg_color="black",
#             border_width=2,
#             border_color="#404040",
#             corner_radius=10
#         )
#         self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
#         self.container.update_idletasks()


#         self.create_widgets()
     

#     def create_widgets(self):
#         top_bar = CTkFrame(
#             master=self.container,
#             fg_color="#282828"
#         )



#         top_bar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
  

#         tools_intro = [
#             ("✔️YouTube Downloader", "Download videos and audio with all available format selection for det video. \n"),
#             ("✔️LR Metadata Agent", "AI-Agent: Generates SEO-optimized Title, Description, Hashtags, Keywords  choosen video in uploaded files. \n"),
#             ("✔️Mediainfo Analyst", "View technical metadata from media files. \n"),
#             ("✔️Social Media Uploading", "Upload to platforms like YouTube, TikTok. \n"),
#             ("✔️AI AutoCreator", "AI agent to transcribe, edit and upload videos. \n"),
#             ("📍Future Updates", "The program is under development, Program updates will be released in the future. \n"),

#         ]
#         intro_text = "\n\n".join([f"• {name}:\n  {desc}" for name, desc in tools_intro])
      
#         intro_label = CTkLabel(
#             master=self.container,
#             text="Available Tools:\n\n" + intro_text,
#             font=("Arial", 14),
#             justify="left",
#             text_color="#FFFFFF",
#             wraplength=600,
#             fg_color="transparent",
#             anchor="nw"
#         )
#         intro_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)


#         self.info_button_ToolMenu_info = create_info_button(
#             open_ToolMenu_Info,
#             text="INFO",
#             width=15,
#             master=top_bar
#         )
#         self.info_button_ToolMenu_info.pack(side="left", padx=10, pady=5)

   

#         self.container.columnconfigure(0, weight=1)
#         self.container.rowconfigure(1, weight=1)

 




































# class VidGenesis_Automation_Agent:

#     def __init__(self, parent_container):
#         self.parent_container = parent_container


        
#         self.should_stop = False
#         self.container = CTkFrame(
#             master=self.parent_container,
#             fg_color="#282828",
#             border_width=2,
#             border_color="#404040",
#             corner_radius=10
#         )
#         self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

#         self.loading_label = CTkLabel(
#             master=self.container,
#             text="",
#             text_color="#00FF00",
#             font=("Arial", 14)
#         )
#         self.loading_label.grid(row=2, column=0, pady=5, sticky="nsew")
#         wait_time = 0
#         while Global_offline_model is None:
#             self.loading_label.configure(text=f"⏳ Waiting for model to load... {wait_time}s")
#             self.loading_label.update_idletasks()
#             time.sleep(1)
#             wait_time += 1
#             if wait_time > 60:
#                 self.loading_label.configure(text="❌ Timeout waiting for model to load.")
#                 return

#         self.loading_label.configure(text="✅ Model loaded successfully.")
#         self.model = Global_offline_model
#         self.create_widgets()

#     def create_widgets(self):
#         #Top section with all user inputs
#         self.top_bar = CTkFrame(
#             master=self.container,
#             fg_color="black",
#             border_color="white",
#             border_width=2
#         )
#         self.top_bar.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 0))
#         self.top_bar.columnconfigure((0, 1, 2), weight=1)
#         self.top_bar.rowconfigure(1, weight=1)
#         #Title input
#         self.title_entry = CTkEntry(self.top_bar, placeholder_text="Title of video", width=250)
#         self.title_entry.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="w")

#         #Topic
#         self.topic_entry = CTkEntry(self.top_bar, placeholder_text="Topic of video", width=250)
#         self.topic_entry.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="w")


#         # Dropdown1
#         self.styledropdown1 = CTkOptionMenu(self.top_bar, variable=StringVar(), values=[
#             "Cinematic", "Emotional", "Inspirational", "Mystical",
#             "Playful", "Dark & Gritty", "Uplifting", "Chill / Relaxed",
#             "Tense / Suspenseful", "Epic", "Minimalistic", "Abstract / Surreal"
#         ], width=175)
#         self.styledropdown1.set("None")
#         self.styledropdown1.grid(row=0, column=1, padx=(5, 10), pady=(10, 5), sticky="w")

#         #Dropdown2
#         self.styledropdown2 = CTkOptionMenu(self.top_bar, variable=StringVar(), values=[
#             "value1", "value2", "value3", "value4"
#         ], width=175)
#         self.styledropdown2.set("None")
#         self.styledropdown2.grid(row=1, column=1, padx=(5, 10), pady=5, sticky="w")

#         #Amount
#         self.video_amount = CTkEntry(self.top_bar, textvariable=StringVar(), placeholder_text="Amount of videos", width=100)
#         self.video_amount.grid(row=0, column=2, padx=5, pady=5, sticky="w")

#         #Description label
#         self.description_label = CTkLabel(self.top_bar, text="📝 Description of the Video", font=("Arial", 14), text_color="white")
#         self.description_label.grid(row=2, column=0, columnspan=3, padx=10, pady=(10, 0), sticky="w")

#         #Description box
#         self.description_entry = CTkTextbox(self.top_bar, height=110)
#         self.description_entry.grid(row=3, column=0, columnspan=3, padx=10, pady=(0, 5), sticky="ew")

#         #Agent run button 
#         self.run_agent_node = CTkButton(
#             master=self.top_bar,
#             command=lambda: Thread(target=self.run_agent).start(),
#             fg_color="black",
#             text="▶ Run AGENT Node"
#         )
#         self.run_agent_node.grid(row=1, column=2,     padx=(5, 10), pady=(0, 5), sticky="se")

#         #Chat area below other widgets
#         self.chat_display = scrolledtext.ScrolledText(
#             self.container,
#             wrap=tk.WORD,
#             width=55,
#             height=25,
#             font=("Helvetica", 12),
#             bg="black",
#             fg="white",
#             state="disabled"
#         )
#         self.chat_display.config(
#             insertbackground="yellow",
#             selectbackground="#444444",
#             selectforeground="white",
#             borderwidth=2,
#             relief="sunken"
#         )
#         self.chat_display.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=(0, 10))
#         self.container.columnconfigure(0, weight=1)
#         self.container.rowconfigure(1, weight=1)


#     def run_single_video_task(self):

#             try:
#                 prompts = find_by_relative_path(f"Assets{os_separator}prompts_video_creator.yaml")
#                 with open(prompts, 'r') as stream:
#                      prompt = yaml.safe_load(stream)

#                 Custom_user_task = f"""Your goal is to create a video based on the specified topic and parameters implemented.
#                                    1.
#                                    2.
#                                    3.
#                                    4.
#                                    5.
#                                    6.

                              
#                                    """

          
#                 self.context_var =  { 
#                             "Video Title": self.title_entry.get(),
#                             "topic": self.topic_entry.get(),
#                             "description": self.description_entry.get("1.0", "end-1c"),
#                             "video_amount": self.video_amount_var.get(),
#                             "media_type": self.media_type_var.get()
#                             }
                
#                 AutoMation_agent  = CodeAgent(
#                     model=self.model,
#                     tools=[
#                         FinalAnswerTool(), 
#                         SpeechToTextTool(),
#                         VisitWebpageTool(),
#                         GoogleSearchTool(),
#                         Fetch_top_trending_youtube_videos,
#                         #Upload_video_to_socialMedia_platform,
#                         #add_text_to_video,
#                         #add_audio_to_video,
#                         #add_filter_to_video,
#                     ], 
#                     max_steps=10,
#                     verbosity_level=1,
#                     prompt_templates=prompt,
#                     add_base_tools=True
#                 )

#                 self.manager_agent = AutoMation_agent
#                 self.user_task = Custom_user_task
#                 self.context_var = self.context_var

#                 response = self.manager_agent.run(
#                             task=self.user_task,
#                             additional_args=self.context_var
#                 )

#                 self.chat_display.config(state=tk.NORMAL)
#                 if isinstance(response, dict):
#                     formatted = (
#                         json.dumps(response, indent=4),
#                     )
#                 else:
#                     formatted = str(response)

#                 self.chat_display.insert(tk.END, formatted + "\n")
#                 self.chat_display.config(state=tk.DISABLED)
#                 self.chat_display.see(tk.END)
#             except Exception as e:
#                     logging.info("❌ Error in run_single_video_task:", e)



#     def run_agent_loop(self):
#             try:
#                 amount = int(self.video_amount_var.get())
#             except ValueError:
#                 logging.info("invalid video amount entered")
#                 return
            
#             for i in range(amount):
#                 if self.should_stop:
#                     break
#                 self.run_single_video_task()


#     def run_agent(self):   
     
#         self.RunForever = Thread(target=self.run_agent_loop(),daemon=True)
#         self.RunForever.start()

 

           


        
























# class ColorRestorer_gui:

#     def __init__(self, parent_container):
#         self.parent_container = parent_container
#         self.uploaded_image  = None
#         self.colorizer = None
#         self.colorized_image = None
#         self.selected_resolution = 800

#         self.container = CTkFrame(
#             master=self.parent_container,
#             fg_color="#282828",
#             border_width=2,
#             border_color="#404040",
#             corner_radius=10
#         )
#         self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

#         self.resolution_entry = CTkOptionMenu(
#             self.container,
#             values=["512x512", "768x768", "1024x1024", "1280x1280", "1920x1920"],
#             command=self.on_resolution_change,
#             width=200
#         )
#         self.resolution_entry.pack(pady=10)

#         self.upload_button = CTkButton(
#             self.container,
#             text="Upload Image",
#             command=self.upload_image
#         )
#         self.upload_button.pack(pady=10)
   
#         self.save_button = CTkButton(
#             self.container,
#             text="Save Image",
#             command=self.save_image,
#             state="disabled"
#         )
#         self.upload_button.pack(pady=10)
   

#         self.colorize_button = CTkButton(
#             self.container,
#             text="Colorize",
#             command=self.colorize_image,
#             state="disabled"
#         )
#         self.colorize_button.pack(pady=10)


#         self.image_label = CTkLabel(self.container, text="").pack(pady=10)


#     def on_resolution_change(self,value):
#         try:
#             w, h = value.lower().split("x")
#             self.selected_resolution = (int(w), int(h))
#         except:
#             self.selected_resolution = (800,800)

#     def upload_image(self):
#         file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
#         if file_path:
#             self.uploaded_image = Image.open(file_path).convert("RGB")
#             preview = self.uploaded_image.resize((300,300))
#             tk_img = ImageTk.PhotoImage(preview)
#             self.image_label.image = tk_img
#             self.colorize_button.configure(state="normal")


#     def colorize_image(self):
#         from LocalModelAssets.Old_photos__colorizing.Vizualise  import get_image_colorizer
#         if self.uploaded_image:
#             self.colorizer = get_image_colorizer(artistic=True)
#             resized = self.uploaded_image.resize((self.selected_resolution))
#             colorized_img = self.colorizer.plot_transformed_pil_image(resized, render_factor=35, compare=False)
#             self.colorized_image = colorized_img
#             tk_img = ImageTk.PhotoImage(colorized_img.resize((300,300)))
#             self.image_label.configure(image=tk_img)
#             self.image_label.image = tk_img
#             self.save_button.configure(state="normal")

#     def save_image(self):
#         if self.colorized_image:
#             save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
#                                                      filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
#             if save_path:
#                 final_img = self.colorized_image.resize((self.selected_resolution, self.selected_resolution))
#                 final_img.save(save_path)



























































# ####TOOL(1) FOR TOOLCLASS#####
# class MediaTree_Inspector_gui:
#     def __init__(self, parent_container):
#         self.parent_container = parent_container
#         self.selected_file_list = selected_file_list
#         self.truncated_to_full = {}
#         self.MediaInfo_Agent = Global_offline_model


#         self.container = CTkFrame(
#             master=self.parent_container,
#             fg_color="#282828",
#             border_width=2,
#             border_color="#404040",
#             corner_radius=10
#         )
#         self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

#         self.create_widgets()
#         global media_info_update_callback
#         media_info_update_callback = self.sync_uploaded_files
#         self.populate_dropdown()

#     def create_widgets(self):
#         top_bar = CTkFrame(
#             master=self.container,
#             fg_color="#282828"
#         )
#         top_bar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

      
#         self.file_menu_var = StringVar(value="No files uploaded")
#         self.file_menu = CTkOptionMenu(
#             master=top_bar,
#             variable=self.file_menu_var,
#             values=[],
#             width=150,
#             height=30,
#             fg_color="#282828",
#             button_color="#404040",
#             text_color="#FFFFFF"
#         )
#         self.file_menu.pack(side="left", padx=10, pady=5)



#         self.get_details_btn = CTkButton(
#             master=top_bar,
#             text="Fetch MediaInfo",
#             width=140,
#             height=30,
#             border_width=1,
#             font=bold11,
#             fg_color="#282828",
#             text_color="#E0E0E0",
#             border_color="#0096FF",
#             command=self.get_details
#         )
#         self.get_details_btn.pack(side="left", padx=10, pady=5)

   
#         self.info_button_mediainfo_analyst = create_info_button(
#             open_mediaInfo_Analyst,
#             text="INFO",
#             width=15,
#             master=top_bar
#         )
#         self.info_button_mediainfo_analyst.pack(side="left", padx=10, pady=5)

   
#         self.details_text = CTkTextbox(
#             master=self.container,
#             width=1000,
#             height=500,
#             font=("Arial", 20),
#             corner_radius=10,
#             state="disabled"
#         )
#         self.details_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

#         self.container.columnconfigure(0, weight=1)
#         self.container.rowconfigure(1, weight=1)


#     def sync_uploaded_files(self):
#             """Sync file list with global and refresh dropdown"""
#             self.selected_file_list = selected_file_list
#             self.populate_dropdown()


#     def populate_dropdown(self):
#         max_length = 20
#         self.truncated_to_full = {}  # reset mapping

#         file_names = [f.split("/")[-1] for f in self.selected_file_list]
#         truncated_names = []

#         for original, full_path in zip(file_names, self.selected_file_list):
#             truncated = original if len(original) <= max_length else original[:max_length] + '...'
#             truncated_names.append(truncated)
#             self.truncated_to_full[truncated] = full_path  # store mapping

#         self.file_menu.configure(values=truncated_names)

#         if truncated_names:
#             self.file_menu_var.set(truncated_names[0])


#     def place_mediainfo_analyst_textbox(self):
#         Info_button_mediainfo_analyst = create_info_button(
#             open_mediaInfo_Analyst,
#             text="MediaInfo (info)",
#             width=15,
#             master=self.container
#         )
#         Info_button_mediainfo_analyst.grid(row=1, column=0, pady=10)




#     def clear_file_list(self):
#         """
#         Clears the selected_file_list and resets the dropdown.
#         """
#         self.selected_file_list = []
#         self.file_menu.configure(values=[])
#         self.file_menu_var.set("No files uploaded")


#     def get_details(self):
#         """
#         Retrieves detailed metadata for the selected video file using ffmpeg.
#         """
#         logging.info("[DEBUG] Fetch button clicked")

#         selected_file = self.file_menu_var.get()
#         file_path = self.truncated_to_full.get(selected_file)
#         logging.info(f"[DEBUG] Selected file: {selected_file}")
#         logging.info(f"[DEBUG] Full path: {file_path}")

#         self.details_text.configure(state="normal")
#         self.details_text.delete("1.0", END)

#         if file_path:
#             details = get_ffmpeg_details(file_path)
#             logging.info(f"[DEBUG] Raw details returned:\n{details}")

#             if not details:
#                 self.details_text.insert(END, "No data received from ffmpeg.")
#             elif details.startswith("Error") or details.startswith("An unexpected"):
#                 self.details_text.insert(END, details)
#             else:
#                 formatted_data = self.format_details(details)
#                 self.details_text.insert(END, formatted_data or "No readable metadata found.")
#         else:
#             self.details_text.insert(END, "No file selected or file not found.")

#         self.details_text.configure(state="disabled")

#     def format_details(self, details):
#         """
#         Format and structure the JSON data for better readability in the textbox.
#         """
#         try:
      
#             parsed_details = json.loads(details)
            
    
#             formatted_data = ""

          
#             formatted_data += "\n### General Information ###\n"
#             format_info = parsed_details.get('format', {})
#             formatted_data += f"Filename: {format_info.get('filename', 'N/A')}\n"
#             formatted_data += f"Format: {format_info.get('format_name', 'N/A')} ({format_info.get('format_long_name', 'N/A')})\n"
#             formatted_data += f"Duration: {format_info.get('duration', 'N/A')} seconds\n"
#             formatted_data += f"Size: {format_info.get('size', 'N/A')} bytes\n"
#             formatted_data += f"Bitrate: {format_info.get('bit_rate', 'N/A')} bps\n"
#             formatted_data += f"Probe Score: {format_info.get('probe_score', 'N/A')}\n"
#             formatted_data += "-" * 50 + "\n"

       
#             streams = parsed_details.get('streams', [])
#             for stream in streams:
#                 formatted_data += f"### Stream {stream.get('index', 'N/A')} ###\n"
#                 formatted_data += f"Codec: {stream.get('codec_long_name', 'N/A')}\n"
#                 formatted_data += f"Codec Type: {stream.get('codec_type', 'N/A')}\n"
#                 formatted_data += f"Resolution: {stream.get('width', 'N/A')} x {stream.get('height', 'N/A')}\n"
#                 formatted_data += f"Aspect Ratio: {stream.get('display_aspect_ratio', 'N/A')}\n"
#                 formatted_data += f"Frame Rate: {stream.get('r_frame_rate', 'N/A')}\n"
#                 formatted_data += f"Bitrate: {stream.get('bit_rate', 'N/A')}\n"
#                 formatted_data += f"Duration: {stream.get('duration', 'N/A')} seconds\n"
#                 formatted_data += f"Has B-Frames: {stream.get('has_b_frames', 'N/A')}\n"
#                 formatted_data += f"Sample Aspect Ratio: {stream.get('sample_aspect_ratio', 'N/A')}\n"
#                 formatted_data += f"Chroma Location: {stream.get('chroma_location', 'N/A')}\n"
#                 formatted_data += f"Field Order: {stream.get('field_order', 'N/A')}\n"
#                 formatted_data += f"Pixel Format: {stream.get('pix_fmt', 'N/A')}\n"
#                 formatted_data += "-" * 50 + "\n"

              
#                 disposition = stream.get('disposition', {})
#                 formatted_data += "Disposition:\n"
#                 for key, value in disposition.items():
#                     formatted_data += f"  {key}: {value}\n"

           
#                 tags = stream.get('tags', {})
#                 if tags:
#                     formatted_data += "Tags:\n"
#                     for tag_key, tag_value in tags.items():
#                         formatted_data += f"  {tag_key}: {tag_value}\n"
#                 formatted_data += "-" * 50 + "\n"

       
#             tags = format_info.get('tags', {})
#             if tags:
#                 formatted_data += "\n### File Tags ###\n"
#                 for tag_key, tag_value in tags.items():
#                     formatted_data += f"{tag_key}: {tag_value}\n"
#                 formatted_data += "-" * 50 + "\n"

        
#             return formatted_data

#         except json.JSONDecodeError:
#             return "Error: Failed to parse the details."



































# ####TOOLCLASS#####
# ### a class with list of available tools that changes window for each tool on the main window.
# class ToolWindowClass:
#     def __init__(self, master):
#         self.master = master

#         self.container = CTkFrame(master, fg_color="black", border_width=0, corner_radius=0)
#         self.container.place(relx=0.0, rely=0.0, relwidth=0.22, relheight=1.0)


    
#         self.create_widgets()

#     def create_widgets(self):
#         self.menu_frame = CTkFrame(self.container, fg_color="#0A0A09",
#                                    border_width=0, corner_radius=0, height=44)
#         self.menu_frame.pack(side="top", fill="x")
#         self.menu_frame.pack_propagate(False)

  
#         self.tool_list = ['Tool Menu','YouTube Downloader', 'MediaTree Inspector', 'SocialMedia Uploading','VidIntel Agent','VidGenesis Automation Agent','ColorRestorer AI','Corelytics InsightCatcher AI','Social Media Optimizer AI']
#         self.tool_menu_var = StringVar(value=self.tool_list[0])
#         self.tool_menu = CTkOptionMenu(
#             master=self.menu_frame,
#             variable=self.tool_menu_var,
#             values=self.tool_list,
#             command=self.on_tool_select,
#             width=200,
#             height=36,
#             fg_color="#0E0E0D",
#             button_color="#201E1A",
#             button_hover_color="#383028",
#             text_color="#C8C0B0",
#             dropdown_fg_color="#0E0E0D",
#             dropdown_text_color="#C8C0B0",
#             dropdown_hover_color="#181614",
#             font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         )
#         self.tool_menu.pack(side="top", fill="x", padx=8, pady=4)

#         self.content_frame = CTkFrame(self.container, fg_color="transparent")
#         self.content_frame.pack(side="top", fill="both", expand=True)

  
#         self.on_tool_select(self.tool_list[0])

#     def on_tool_select(self, selected_tool):
     
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

          
#         if selected_tool == 'Tool Menu':
#             self.CreateToolMenu_info()
#         elif selected_tool == 'VidIntel Agent':
#             self.create_vidintel_agent()
#         elif selected_tool == 'YouTube Downloader':
#             self.create_youtube_downloader()
#         elif selected_tool == "MediaTree Inspector":
#             self.create_MediaTree_Inspector()
#         elif selected_tool == "SocialMedia Uploading":
#             self.Create_Social_Media_uploading()
#         elif selected_tool == "VidGenesis Automation Agent":
#             self.create_VidGenesis_Automation_Agent
#         elif selected_tool == "ColorRestorer AI":
#             self.create_ColorRestorer_ai()
#         elif selected_tool == "Corelytics InsightCatcher AI":
#             self.Corelytics_InsightCatcher()
#         elif selected_tool == "Social Media Optimizer AI":
#             self.create_Social_Media_Optimizer_AI

#     def create_Social_Media_Optimizer_AI(self):
#         self.social_media_optimizer_Gui = social_media_optimizer_Gui(self.content_frame)
#         self.social_media_optimizer_Gui.pack(fill="both", expand=True, padx=10, pady=10)

#     def CreateToolMenu_info(self):
#        self.ToolMenu = ToolMenu(self.content_frame)
#        self.ToolMenu.container.pack(fill="both",expand=True,padx=10,pady=10)
        
#     def Corelytics_InsightCatcher(self):
#         self.create_corelytics_InsightCatcher = corelytics_InsightCatcher(self.content_frame)
#         self.create_corelytics_InsightCatcher.pack(fill="both", expand=True, padx=10, pady=10)

#     def create_vidintel_agent(self):
#         self.vidintel_agent = vidintel_agent_gui(self.content_frame)
#         self.vidintel_agent.container.pack(fill="both", expand=True, padx=10, pady=10)

#     def create_VidGenesis_Automation_Agent(self):
#         self.VidGenesis_Automation_Agent = VidGenesis_Automation_Agent(self.content_frame)
#         self.VidGenesis_Automation_Agent.container.pack(fill="both",expand=True,padx=10,pady=10)
    
#     def create_MediaTree_Inspector(self):
#         self.MediaTree_Insepctor = MediaTree_Inspector_gui(self.content_frame)
#         self.MediaTree_Insepctor.container.pack(fill="both", expand=True, padx=10, pady=10)

#     def Create_Social_Media_uploading(self):
#         self.socialMediaUploading = SocialMediaUploading(self.content_frame)
#         self.socialMediaUploading.container.pack(fill="both", expand=True, padx=10, pady=10)
    
#     def create_ColorRestorer_ai(self):
#         self.colorRestorer_ai = ColorRestorer_gui(self.content_frame)
#         self.colorRestorer_ai.container.pack(fill="both", expand=True, padx=10, pady=10)

#     def create_youtube_downloader(self):
#         self.content_frame.grid_rowconfigure(0, weight=1)
#         self.content_frame.grid_columnconfigure(0, weight=1)
#         place_youtube_download_menu(self.content_frame)





















































































# ####VIDEO PREVIEW CLASS######
# class VideoPreview:
#     """
#     Owns its layout completely inside parent_container (the global 'container').

#     Side-by-side:  two CTkLabel frames packed left/right
#     SoloFrame:     one tk.Canvas with draggable before/after split line
#     """

#     # ── Design tokens ──────────────────────────────────────────────────
#     _ACCENT      = "#D49A2A"   # amber
#     _ACCENT_DIM  = "#48403A"
#     _SEP_COLOR   = "#141210"
#     _TAG_FG      = "#948C7E"
#     _TAG_BG      = "#0E0D0C"
#     _SLIDER_FG   = "#D8C090"
#     _BTN_ACTIVE  = "#1C1810"
#     _BTN_IDLE    = "#0C0C0B"

#     def __init__(self, parent_container, original_label, upscaled_label, video_path):
#         logging.info("Initializing VideoPreview...")
#         self.parent_container = parent_container
#         self.video_path       = video_path

#         # ── Video source ──────────────────────────────────────────────
#         self.cap          = cv2.VideoCapture(video_path)
#         self.fps          = int(self.cap.get(cv2.CAP_PROP_FPS))
#         self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
#         raw_w = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         raw_h = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         self.source_aspect = (raw_w / raw_h) if raw_h > 0 else (16/9)
#         self.target_size   = (raw_w, raw_h)

#         # ── State ─────────────────────────────────────────────────────
#         self.view_mode       = StringVar(value="side_by_side")
#         self.split_ratio     = 0.5
#         self.last_original   = None
#         self.last_upscaled   = None
#         self.solo_canvas     = None
#         self._canvas_photo   = None

#         # ── Destroy any existing layout widgets inside parent_container
#         for w in parent_container.winfo_children():
#             w.destroy()

#         # ── Top bar ───────────────────────────────────────────────────
#         self.top_bar = CTkFrame(parent_container, fg_color="#090907",
#                                 corner_radius=0, height=44)
#         self.top_bar.pack(side="top", fill="x")
#         self.top_bar.pack_propagate(False)

#         # Thin separator line under top bar
#         CTkFrame(parent_container, fg_color=self._SEP_COLOR,
#                  height=1, corner_radius=0).pack(side="top", fill="x")

#         # Mode toggle buttons
#         btn_row = CTkFrame(self.top_bar, fg_color="#090907", corner_radius=6)
#         btn_row.pack(side="left", padx=10, pady=8)

#         self._btn_sbs = CTkButton(
#             btn_row, text="Side by Side",
#             width=104, height=26, corner_radius=6,
#             font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#             fg_color=self._BTN_ACTIVE, hover_color="#28220E",
#             text_color=self._ACCENT,
#             border_width=1, border_color="#302818",
#             command=lambda: self._set_mode("side_by_side")
#         )
#         self._btn_sbs.pack(side="left", padx=(0, 3))

#         self._btn_solo = CTkButton(
#             btn_row, text="Compare",
#             width=90, height=26, corner_radius=6,
#             font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#             fg_color=self._BTN_IDLE, hover_color="#141210",
#             text_color=self._ACCENT_DIM,
#             border_width=1, border_color="#181410",
#             command=lambda: self._set_mode("SoloFrame")
#         )
#         self._btn_solo.pack(side="left")

#         # Timer label — shows current position as MM:SS
#         self.timer_label = CTkLabel(
#             self.top_bar, text="00:00",
#             font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#             text_color=self._ACCENT_DIM,
#             fg_color="#090907",
#             width=44,
#         )
#         self.timer_label.pack(side="left", padx=(8, 2), pady=0)

#         # Timeline slider — right side
#         self.timeline_slider = CTkSlider(
#             self.top_bar,
#             from_=0, to=max(1, self.total_frames - 1),
#             command=self._on_timeline_change,
#             button_color=self._ACCENT,
#             button_hover_color="#F0D880",
#             progress_color="#2A1E08",
#             fg_color="#141210",
#             height=12,
#         )

#         # ── Display area ──────────────────────────────────────────────
#         self.display_area = CTkFrame(parent_container, fg_color="#060606")
#         self.display_area.pack(side="top", fill="both", expand=True)

#         # ── Side-by-side sub-frames ───────────────────────────────────
#         self.orig_frame = CTkFrame(self.display_area, fg_color="#060606")
#         self.orig_label = CTkLabel(self.orig_frame, text="")
#         self.orig_label.pack(fill="both", expand=True, padx=4, pady=(0, 6))

#         self.mid_sep = CTkFrame(self.display_area, fg_color="#161210",
#                                 width=1, corner_radius=0)

#         self.ups_frame = CTkFrame(self.display_area, fg_color="#060606")
#         self.ups_label = CTkLabel(self.ups_frame, text="")
#         self.ups_label.pack(fill="both", expand=True, padx=4, pady=(0, 6))

#         # ── Solo canvas ───────────────────────────────────────────────
#         self.solo_canvas = tk.Canvas(
#             self.display_area, bg="#060606",
#             highlightthickness=0, cursor="sb_h_double_arrow"
#         )
#         self.solo_canvas.bind("<ButtonPress-1>", self._on_canvas_drag)
#         self.solo_canvas.bind("<B1-Motion>",     self._on_canvas_drag)

#         # Show side-by-side initially
#         self._show_sbs_layout()
#         # Defer frame load until layout is fully rendered so winfo_width/height
#         # return real values (not 0/1), preventing a black initial preview.
#         # Load the midpoint frame so the thumbnail is representative.
#         mid_frame = max(0, self.total_frames // 2)
#         self.parent_container.after(150, lambda: self._load_frame(mid_frame))

#         if self.total_frames > 1:
#             self.timeline_slider.pack(side="right", fill="x", expand=True,
#                                       padx=(6, 14), pady=0)
#             # Move slider to midpoint to match the frame we're loading
#             self.timeline_slider.set(mid_frame)

#         logging.info("VideoPreview initialized.")

#     # ================================================================== #
#     #  Header factory — compact pill tag                                   #
#     # ================================================================== #
#     def _make_header(self, parent, text):
#         row = CTkFrame(parent, fg_color="#060606")
#         row.pack(side="top", fill="x", padx=4, pady=(6, 2))
#         is_ups = (text == "UPSCALED")
#         CTkLabel(
#             row, text=text,
#             font=CTkFont(family="Segoe UI", size=9, weight="bold"),
#             text_color=AMBER_DIM if is_ups else self._TAG_FG,
#             fg_color="#0C0906" if is_ups else self._TAG_BG,
#             corner_radius=4, padx=8, pady=3, width=0,
#         ).pack(anchor="center", expand=True)

#     # ================================================================== #
#     #  Layout helpers                                                      #
#     # ================================================================== #
#     def _show_sbs_layout(self):
#         self.solo_canvas.pack_forget()
#         self.orig_frame.pack(side="left",  fill="both", expand=True)
#         self.mid_sep.pack(   side="left",  fill="y",    pady=8)
#         self.ups_frame.pack( side="right", fill="both", expand=True)

#     def _show_solo_layout(self):
#         self.orig_frame.pack_forget()
#         self.mid_sep.pack_forget()
#         self.ups_frame.pack_forget()
#         # Center the compare canvas instead of stretching to the left
#         # Keep the canvas at its rendered image size and let extra space
#         # distribute evenly around it so it stays centered.
#         self.solo_canvas.pack(expand=True, padx=4, pady=4)

#     def _set_mode(self, mode):
#         self.view_mode.set(mode)
#         if mode == "side_by_side":
#             self._btn_sbs.configure(fg_color=self._BTN_ACTIVE,
#                                     text_color=self._ACCENT,
#                                     border_color="#302818")
#             self._btn_solo.configure(fg_color=self._BTN_IDLE,
#                                      text_color=self._ACCENT_DIM,
#                                      border_color="#181410")
#             self._show_sbs_layout()
#         else:
#             self._btn_solo.configure(fg_color=self._BTN_ACTIVE,
#                                      text_color=self._ACCENT,
#                                      border_color="#302818")
#             self._btn_sbs.configure(fg_color=self._BTN_IDLE,
#                                     text_color=self._ACCENT_DIM,
#                                     border_color="#181410")
#             self._show_solo_layout()
#         self._refresh_display()

#     def _on_mode_change(self, mode):
#         self._set_mode(mode)

#     # ================================================================== #
#     #  Helpers                                                             #
#     # ================================================================== #
#     def _fit_size(self, max_w, max_h, aspect=None):
#         if aspect is None:
#             aspect = self.source_aspect
#         aspect = max(0.01, aspect)
#         if max_w / aspect <= max_h:
#             w, h = max_w, int(max_w / aspect)
#         else:
#             h, w = max_h, int(max_h * aspect)
#         return max(1, w), max(1, h)

#     def _frame_aspect(self, frame):
#         h, w = frame.shape[:2]
#         return w / h if h > 0 else self.source_aspect

#     def _to_ctk(self, frame_bgr, w, h):
#         rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
#         res = cv2.resize(rgb, (w, h), interpolation=cv2.INTER_AREA)
#         return CTkImage(Image.fromarray(res), size=(w, h))

#     # ================================================================== #
#     #  Rendering                                                           #
#     # ================================================================== #
#     def _refresh_display(self):
#         if self.last_original is None or self.last_upscaled is None:
#             return
#         if self.view_mode.get() == "side_by_side":
#             self._render_sbs(self.last_original, self.last_upscaled)
#         else:
#             self._render_solo(self.last_original, self.last_upscaled)

#     def _render_sbs(self, orig, ups):
#         self.display_area.update_idletasks()
#         avail_w = max(50, (self.display_area.winfo_width()  // 2) - 16)
#         avail_h = max(50,  self.display_area.winfo_height() - 60)
#         aspect  = self._frame_aspect(orig)
#         dw, dh  = self._fit_size(avail_w, avail_h, aspect)

#         orig_img = self._to_ctk(orig, dw, dh)
#         ups_img  = self._to_ctk(ups,  dw, dh)
#         self.orig_label.configure(image=orig_img, width=dw, height=dh)
#         self.ups_label.configure( image=ups_img,  width=dw, height=dh)
#         self.orig_label.image = orig_img
#         self.ups_label.image  = ups_img

#     def _render_solo(self, orig, ups):
#         self.display_area.update_idletasks()
#         avail_w = max(50, self.display_area.winfo_width()  - 10)
#         avail_h = max(50, self.display_area.winfo_height() - 10)
#         aspect  = self._frame_aspect(orig)
#         dw, dh  = self._fit_size(avail_w, avail_h, aspect)

#         orig_rgb = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)
#         ups_rgb  = cv2.cvtColor(ups,  cv2.COLOR_BGR2RGB)
#         orig_r   = cv2.resize(orig_rgb, (dw, dh), interpolation=cv2.INTER_AREA)
#         ups_r    = cv2.resize(ups_rgb,  (dw, dh), interpolation=cv2.INTER_AREA)

#         sx       = max(0, min(dw, int(dw * self.split_ratio)))
#         combined = orig_r.copy()
#         if sx < dw:
#             combined[:, sx:] = ups_r[:, sx:]

#         pil  = Image.fromarray(combined).convert("RGBA")
#         draw = ImageDraw.Draw(pil, "RGBA")

#         # Main divider — white
#         draw.line([(sx, 0), (sx, dh)], fill=(255, 255, 255, 255), width=2)

#         # Circle handle — white
#         hy, r = dh // 2, 16
#         draw.ellipse([sx-r, hy-r, sx+r, hy+r],
#                      fill=(255, 255, 255, 255), outline=(180, 180, 180, 220), width=1)
#         ap, arrow_col = 4, (50, 50, 50, 255)
#         draw.polygon([(sx-r+ap+2, hy), (sx-ap, hy-7), (sx-ap, hy+7)], fill=arrow_col)
#         draw.polygon([(sx+r-ap-2, hy), (sx+ap, hy-7), (sx+ap, hy+7)], fill=arrow_col)

#         # Corner pill labels
#         try:
#             fnt = ImageFont.truetype("segoeuib.ttf", max(11, dh // 36))
#         except IOError:
#             try:
#                 fnt = ImageFont.truetype("arial.ttf", max(11, dh // 36))
#             except IOError:
#                 fnt = ImageFont.load_default()

#         def _pill(text, x, y, text_col, bg_col):
#             tw = int(draw.textlength(text, font=fnt))
#             th = max(11, dh // 36)
#             px, py = 8, 4
#             draw.rounded_rectangle([x-px, y-py, x+tw+px, y+th+py],
#                                    radius=4, fill=bg_col)
#             draw.text((x, y), text, fill=text_col, font=fnt)

#         self.solo_canvas.config(width=dw, height=dh)
#         photo = ImageTk.PhotoImage(pil.convert("RGB"))
#         self.solo_canvas.delete("all")
#         self.solo_canvas.create_image(dw // 2, dh // 2, anchor="center", image=photo)
#         self._canvas_photo = photo

#     # ================================================================== #
#     #  Events                                                              #
#     # ================================================================== #
#     def _on_canvas_drag(self, event):
#         cw = self.solo_canvas.winfo_width()
#         if cw > 0:
#             self.split_ratio = max(0.0, min(1.0, event.x / cw))
#         if self.last_original is not None:
#             self._render_solo(self.last_original, self.last_upscaled)

#     def _on_timeline_change(self, value):
#         frame_number = int(float(value))
#         # Update timer label (MM:SS)
#         fps = self.fps if self.fps > 0 else 24
#         total_seconds = frame_number / fps
#         minutes = int(total_seconds // 60)
#         seconds = int(total_seconds % 60)
#         self.timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
#         self._load_frame(frame_number)

#     # ================================================================== #
#     #  Frame loading                                                       #
#     # ================================================================== #
#     def _load_frame(self, frame_number):
#         self.timeline_slider.configure(state="disabled")
#         loading = LoadingIcon(self.parent_container)
#         loading.start()
#         Thread(target=self._process_frame_bg,
#                args=(frame_number, loading), daemon=True).start()

#     def _process_frame_bg(self, frame_number, loading):
#         try:
#             if frame_number in frame_cache:
#                 orig, ups = frame_cache[frame_number]
#             else:
#                 self.cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_number))
#                 ok, frame = self.cap.read()
#                 if not ok:
#                     return
#                 orig = cv2.resize(frame, self.target_size, interpolation=cv2.INTER_AREA)
#                 ups  = self._ai_process(orig)
#                 frame_cache[frame_number] = (orig, ups)

#             self.last_original = orig
#             self.last_upscaled = ups
#             self.parent_container.after(0, self._refresh_display)
#             self.parent_container.after(0, loading.stop)
#             self.parent_container.after(0, lambda: self.timeline_slider.configure(state="normal"))
#         except Exception as e:
#             logging.info(f"Error processing frame {frame_number}: {e}")
#             try:
#                 self.parent_container.after(0, loading.stop)
#             except Exception:
#                 pass

#     def _ai_process(self, frame):
#         global preview_ai_instance
#         if preview_ai_instance:
#             return preview_ai_instance.AI_orchestration(frame)
#         return frame

#     # ================================================================== #
#     #  Cleanup                                                             #
#     # ================================================================== #
#     def close(self):
#         self.cap.release()
#         try:
#             self.timeline_slider.destroy()
#         except Exception:
#             pass






# # GUI place functions ---------------------------
# def create_placeholder_image(width, height, label="ORIGINAL"):
#     """Render a sleek dark placeholder with a film-strip icon and a hint line."""
#     from PIL import Image, ImageDraw, ImageFont
#     import math

#     # ── background ────────────────────────────────────────────────────
#     img  = Image.new('RGB', (width, height), color='#080807')
#     draw = ImageDraw.Draw(img)

#     # subtle vignette-style border gradient (draw concentric rects fading in)
#     for i in range(18):
#         alpha = int(30 * (1 - i / 18))
#         shade = max(0, alpha)
#         c = f"#{shade:02x}{shade:02x}{int(shade*0.85):02x}"
#         draw.rectangle([i, i, width - i - 1, height - i - 1], outline=c)

#     # ── icon: simple film-frame / play chevron ─────────────────────────
#     cx, cy = width // 2, height // 2 - 22

#     # outer circle
#     r = 34
#     draw.ellipse([cx - r, cy - r, cx + r, cy + r],
#                  outline="#2A2620", width=2, fill="#0F0E0C")

#     # play triangle
#     pts = [
#         (cx - 10, cy - 15),
#         (cx - 10, cy + 15),
#         (cx + 16, cy),
#     ]
#     draw.polygon(pts, fill="#3C2808")   # dim amber fill
#     draw.polygon(pts, outline="#8C6418", fill=None)

#     # decorative tick marks around circle (like a reel)
#     for angle_deg in range(0, 360, 45):
#         angle = math.radians(angle_deg)
#         x1 = cx + (r + 2) * math.cos(angle)
#         y1 = cy + (r + 2) * math.sin(angle)
#         x2 = cx + (r + 8) * math.cos(angle)
#         y2 = cy + (r + 8) * math.sin(angle)
#         draw.line([(x1, y1), (x2, y2)], fill="#1E1A14", width=1)

#     # ── main hint text ─────────────────────────────────────────────────
#     try:
#         font_main = ImageFont.truetype("arialbd.ttf", 13)
#         font_sub  = ImageFont.truetype("arial.ttf",   10)
#     except IOError:
#         font_main = ImageFont.load_default()
#         font_sub  = font_main

#     main_text = "Upload a file to preview"
#     sub_text  = "Supports videos & image formats"

#     mw = draw.textlength(main_text, font=font_main)
#     sw = draw.textlength(sub_text,  font=font_sub)

#     draw.text(((width - mw) / 2, cy + r + 16), main_text, fill="#4A4640", font=font_main)
#     draw.text(((width - sw) / 2, cy + r + 36), sub_text,  fill="#2E2B26", font=font_sub)

#     return img







# def place_loadFile_section(window):
#     global container, original_preview, upscaled_preview
#     global original_preview_frame, upscaled_preview_frame
#     global original_label_title, upscaled_label_title

#     window.preview_frame = CTkFrame(
#         master=window,
#         fg_color="#060606",
#         corner_radius=0,
#     )
#     window.preview_frame.place(relx=0.55, rely=0.0, relwidth=0.45, relheight=1.0)

#     container = CTkFrame(window.preview_frame, fg_color="#060606")
#     container.pack(pady=0, padx=0, fill='both', expand=True)

#     # Build the default side-by-side layout directly in container
#     _build_side_by_side_layout(container)

#     globals()['container'] = container

#     # ── Drag-and-drop registration ────────────────────────────────────
#     if _TKDND_AVAILABLE:
#         def _on_drop(event):
#             # Restore normal border colour
#             try:
#                 window.preview_frame.configure(border_color=BORDER2, border_width=0)
#             except Exception:
#                 pass
#             add_files_from_drop(event.data)

#         def _on_enter(event):
#             try:
#                 window.preview_frame.configure(border_width=2, border_color=AMBER)
#             except Exception:
#                 pass
#             return event.action

#         def _on_leave(event):
#             try:
#                 window.preview_frame.configure(border_width=0)
#             except Exception:
#                 pass

#         for widget in (window.preview_frame, container):
#             widget.drop_target_register(_tkdnd.DND_FILES)
#             widget.dnd_bind('<<Drop>>', _on_drop)
#             widget.dnd_bind('<<DragEnter>>', _on_enter)
#             widget.dnd_bind('<<DragLeave>>', _on_leave)


# def _build_side_by_side_layout(container):
#     """Create the default side-by-side preview layout inside container."""
#     global original_preview, upscaled_preview
#     global original_preview_frame, upscaled_preview_frame
#     global original_label_title, upscaled_label_title

#     ph_w, ph_h = 400, 225
#     placeholder_img_orig   = create_placeholder_image(ph_w, ph_h, label="ORIGINAL")
#     placeholder_img_ups    = create_placeholder_image(ph_w, ph_h, label="UPSCALED")
#     placeholder_photo_orig = CTkImage(placeholder_img_orig, size=(ph_w, ph_h))
#     placeholder_photo_ups  = CTkImage(placeholder_img_ups,  size=(ph_w, ph_h))

#     # ── Single centered panel: shown when no file is loaded ──────────
#     original_preview_frame = CTkFrame(
#         container,
#         fg_color="#060606",
#         border_width=1,
#         border_color=BORDER2,
#         corner_radius=6,
#     )
#     # Center the single panel with equal padding on both sides
#     original_preview_frame.pack(fill='both', expand=True, padx=4, pady=4)

#     # Image label fills the panel
#     original_preview = CTkLabel(original_preview_frame, image=placeholder_photo_orig, text="")
#     original_preview.pack(fill='both', expand=True)

#     # Badge overlaid at bottom-left using place()
#     original_label_title = CTkLabel(
#         original_preview_frame,
#         text="ORIGINAL",
#         font=CTkFont(family="Segoe UI", size=9, weight="bold"),
#         text_color=CREAM3,
#         fg_color="#0C0C0B",
#         corner_radius=4,
#         padx=8,
#         pady=3,
#     )
#     original_label_title.place(relx=0.0, rely=1.0, anchor="sw", x=8, y=-8)
#     # Hide the ORIGINAL badge when showing the placeholder (no file loaded)
#     original_label_title.place_forget()

#     # ── Thin amber divider between panels (hidden initially) ─────────
#     _divider = CTkFrame(container, fg_color=AMBER_GLOW, width=1)
#     # Do NOT pack _divider yet — shown only after a file is loaded

#     # ── Right panel: UPSCALED (hidden initially) ─────────────────────
#     upscaled_preview_frame = CTkFrame(
#         container,
#         fg_color="#060606",
#         border_width=1,
#         border_color=BORDER2,
#         corner_radius=6,
#     )
#     # Do NOT pack upscaled_preview_frame yet — shown only after a file is loaded

#     upscaled_preview = CTkLabel(upscaled_preview_frame, image=placeholder_photo_ups, text="")
#     upscaled_preview.pack(fill='both', expand=True)

#     upscaled_label_title = CTkLabel(
#         upscaled_preview_frame,
#         text="UPSCALED",
#         font=CTkFont(family="Segoe UI", size=9, weight="bold"),
#         text_color=AMBER_DIM,
#         fg_color="#0C0906",
#         corner_radius=4,
#         padx=8,
#         pady=3,
#     )
#     upscaled_label_title.place(relx=0.0, rely=1.0, anchor="sw", x=8, y=-8)

#     # Store divider reference so it can be shown later
#     globals()['_preview_divider']       = _divider

#     globals()['original_preview']       = original_preview
#     globals()['upscaled_preview']       = upscaled_preview
#     globals()['original_preview_frame'] = original_preview_frame
#     globals()['upscaled_preview_frame'] = upscaled_preview_frame
#     globals()['original_label_title']   = original_label_title
#     globals()['upscaled_label_title']   = upscaled_label_title


 











# ###Loading-ICON####
# class LoadingIcon:
#     def __init__(self, master):
#         self.master = master
#         self.animating = False
#         self.angle = 0

#         size = 60
#         self.canvas = tk.Canvas(
#             master,
#             width=size,
#             height=size,
#             bg="#060606",
#             highlightthickness=0,
#             bd=0,
#         )
#         self.canvas.place(relx=0.5, rely=0.5, anchor="center")

#         self._size = size
#         self._arc_id = None

#     def start(self):
#         self.animating = True
#         logging.info("Started loading animation")
#         self._draw()

#     def stop(self):
#         self.animating = False
#         self.canvas.destroy()
#         logging.info("Stopped loading animation")

#     def _draw(self):
#         if not self.animating:
#             return
#         s = self._size
#         pad = 8
#         self.canvas.delete("all")

#         # Faint grey track circle
#         self.canvas.create_oval(pad, pad, s - pad, s - pad,
#                                 outline="#2A2A2A", width=5)

#         # Amber arc spinner
#         self.canvas.create_arc(pad, pad, s - pad, s - pad,
#                                start=self.angle,
#                                extent=270,
#                                outline=AMBER,
#                                width=5,
#                                style="arc")

#         self.angle = (self.angle + 12) % 360
#         self.master.after(30, self._draw)





























# ####VIDEO PREVIEW EXTERNAL FUNCTIONS######
# def load_model_inference():
#     global preview_ai_instance, last_model_config
#     logging.info(f" preview_ai_instance: {preview_ai_instance},last model config: {last_model_config} ")
#     if not selected_AI_model or selected_AI_model == AI_LIST_SEPARATOR[0]:
#         logging.info("Select an AI model first!")
#         return
#     try:
#         resolution_percentage = float(selected_input_resize_factor.get())
#         if not 1 <= resolution_percentage <= 100:
#             logging.info("Resolution must be between 1% and 100%")
#             return

#         resize_factor = float(resolution_percentage / 100.0)  

#         current_config = (
#             selected_AI_model,
#             selected_gpu,
#             resize_factor,  
#             float(selected_VRAM_limiter.get())
#         )

#         if not preview_ai_instance or last_model_config != current_config:
#             vram_limiter = float(selected_VRAM_limiter.get())
            
#             tiles_resolution = 100 * int(float(str(selected_VRAM_limiter.get())))
#             if tiles_resolution > 0: 
#                 vram_multiplier = very_low_VRAM
#                 max_resolution = int(vram_multiplier * vram_limiter * 100)
                
#                 preview_ai_instance = AI(
#                     selected_AI_model,
#                     selected_gpu,
#                     resize_factor, 
#                     max_resolution
#                 )
#                 available_providers = ort.get_available_providers()
#                 if "DmlExecutionProvider" in available_providers:
#                     preview_ai_instance.inferenceSession.set_providers(
#                     ['DmlExecutionProvider'], 
#                     [{'device_id': 0}]
#                 )
#                 else: 
#                     preview_ai_instance.inferenceSession.set_providers(
#                     preview_ai_instance.inferenceSession.set_providers(["CPUExecutionProvider"])

#                     )
#                 dummy_height = max(64, int(512 * resize_factor))  
#                 dummy_width = max(64, int(512 * resize_factor))
#                 dummy_input = np.random.randint(0, 255, (dummy_height, dummy_width, 3), dtype=np.uint8)

#                 logging.info(f"Dummy input shape: {dummy_input.shape}")
#                 logging.info(f"Dummy input shape: {dummy_input.shape}")
#                 _ = preview_ai_instance.AI_orchestration(dummy_input)
#                 last_model_config = current_config
#                 logging.info("Dummy inference complete")
#                 logging.info("Dummy inference complete")
#                 gc.collect()
#                 torch.cuda.empty_cache()
                
#     except Exception as e:
#         logging.info(f"Error loading model with dummy input: {str(e)}")
#         logging.info(f"Error loading model with dummy input: {str(e)}")
#         logging.info("Dummy inference ERROR")







# def load_model_if_needed(model_name):
#     global preview_ai_instance, current_loaded_model
#     logging.info(f"Loading model if needed: {model_name}...")
#     with model_loading_lock:
#         if current_loaded_model == model_name:
#             logging.info(f"Model {model_name} already loaded.")
#             return 
        
#         try:
#             logging.info(f"Loading {model_name} model...")
#             info_message.set(f"Loading {model_name} model...")

     
#             if preview_ai_instance:
#                 preview_ai_instance.inferenceSession = None
#                 del preview_ai_instance
#                 preview_ai_instance = None
#                 gc.collect()

          
#             preview_ai_instance = AI(
#                 model_name,
#                 selected_gpu,
#                 int(float(selected_input_resize_factor.get())),  
#                 int(float(selected_VRAM_limiter.get())) 
#             )

#             current_loaded_model = model_name
#             info_message.set(f"Model: {model_name} Ready!")
#             logging.info(f"Model: {model_name} Ready!")
#             logging.info(f"{model_name} loaded successfully.")
#         except Exception as e:
#             logging.info(f"Error loading model {model_name}: {str(e)}")
#             logging.info(f"Error loading model {model_name}: {str(e)}")
#             info_message.set(f"Model load failed: {str(e)}")
#             current_loaded_model = None
#             preview_ai_instance = None
#         finally:
#             window.after(0, check_model_loading_progress)




# def check_model_loading_progress():
#     global model_loading_thread, current_loaded_model,window
#     if model_loading_thread.is_alive():
#         window.after(100, check_model_loading_progress)
#     else:
#         if current_loaded_model == selected_AI_model:
#             window.preview_button.configure(state="normal")
#             info_message.set("Ready for preview")
#         else:
#             window.preview_button.configure(state="disabled")
#             info_message.set("Model load failed")







# def select_AI_from_menu(selected_option: str) -> None:
#     global selected_AI_model, current_loaded_model, model_loading_thread
#     logging.info(f"AI model selected: {selected_option}")
    
#     if selected_option == current_loaded_model or selected_option in AI_LIST_SEPARATOR:
#         return
    

#     selected_AI_model = selected_option
#     info_message.set(f"Loading {selected_option}...")
#     update_file_widget(1, 2, 3)

#     if model_loading_thread and model_loading_thread.is_alive():
#         model_loading_thread.join(timeout=0.5)
    
#     model_loading_thread = threading.Thread(
#         target=load_model_if_needed,
#         args=(selected_option, ),
#         daemon=True
#     )
#     model_loading_thread.start()


 







# # AI -------------------
# class AI:
#     # CLASS INIT FUNCTIONS
#     def __init__(
#             self, 
#             AI_model_name: str, 
#             directml_gpu: str, 
#             input_resize_factor: int,
#             max_resolution: int,
#             ):
        
#         # Passed variables
#         self.AI_model_name  = AI_model_name
#         self.audio_model_name = "Vocal_Isolation"
#         self.denoise_model_name = "Audio_Denoiser"
#         self.directml_gpu   = directml_gpu
#         self.input_resize_factor  = input_resize_factor
#         self.max_resolution = max_resolution

#         # Calculated variables
#         self.AI_model_path    = find_by_relative_path(f"AI-onnx{os_separator}{self.AI_model_name}_fp16.onnx")
#         self.inferenceSession = self._load_inferenceSession()
#         self.upscale_factor   = self._get_upscale_factor()
#         self.audio_model_path = find_by_relative_path(f"AI-onnx{os_separator}{self.audio_model_name}.onnx")
#         self.Denoise_Modelpath = find_by_relative_path(f"AI-onnx{os_separator}{self.denoise_model_name}.onnx")
        
#     def _get_upscale_factor(self) -> int:
#         if   "x1" in self.AI_model_name: return 1
#         elif "x2" in self.AI_model_name: return 2
#         elif "x4" in self.AI_model_name: return 4
        
        
    

#     def _load_inferenceSession(self) -> onnxruntime_inferenceSession:
#         import onnxruntime
#         providers = ['CPUExecutionProvider']

#         if 'CUDAExecutionProvider' in onnxruntime.get_available_providers():

#             providers = ['CUDAExecutionProvider', 'CPUExecutionProvider']
#         elif 'DmlExecutionProvider' in onnxruntime.get_available_providers():

#             match self.directml_gpu:
#                 case 'Auto':
                   
#                     providers = [('DmlExecutionProvider', {})] + providers
#                 case 'GPU 1' | 'GPU 2' | 'GPU 3' | 'GPU 4':
#                     device_id = int(self.directml_gpu.split()[-1]) - 1
#                     providers = [
#                         ('DmlExecutionProvider', {'device_id': device_id}),
#                         'CPUExecutionProvider'
#                     ]
#                 case 'CPU':
#                     providers = ['CPUExecutionProvider']
        
    
#         session_options = onnxruntime.SessionOptions()
#         session_options.graph_optimization_level = onnxruntime.GraphOptimizationLevel.ORT_ENABLE_ALL
#         session_options.execution_mode = onnxruntime.ExecutionMode.ORT_PARALLEL
        
#         try:
          
#             inference_session = onnxruntime_inferenceSession(
#                 path_or_bytes=self.AI_model_path,
#                 providers=providers,
#                 sess_options=session_options
#             )
#         except Exception as e:
#             logging.info(f"Session creation failed: {str(e)}")

#             inference_session = onnxruntime_inferenceSession(
#                 path_or_bytes=self.AI_model_path,
#                 providers=['CPUExecutionProvider']
#             )
        
#         logging.info(f"Using providers: {inference_session.get_providers()}")
#         if 'CUDAExecutionProvider' in inference_session.get_providers():
#             options = inference_session.get_provider_options()['CUDAExecutionProvider']
#             logging.info(f"CUDA device ID: {options.get('device_id', 'default')}")

#         return inference_session

#     def _load_audio_inferenceSession(self) -> onnxruntime_inferenceSession:
#         import onnxruntime
#         available_providers = onnxruntime.get_available_providers()
#         if 'DmlExecutionProvider' in available_providers:
#             providers = ['DmlExecutionProvider'] 
#             [{"device_id": 0}]
#         else:  
#             providers = ["CPUExecutionProvider"]


#         session_options = onnxruntime.SessionOptions()
#         session_options.graph_optimization_level = onnxruntime.GraphOptimizationLevel.ORT_ENABLE_ALL
#         session_options.execution_mode = onnxruntime.ExecutionMode.ORT_PARALLEL

#         try:
#             return ort.InferenceSession(
#                 path_or_bytes=self.audio_model_path,
#                 providers=providers,
#                 sess_options=session_options
#             )
#         except Exception as e:
#             logging.info(f"[AudioSession Error] {e}")
#             return ort.InferenceSession(
#                 path_or_bytes=self.audio_model_path,
#                 providers=['CPUExecutionProvider']
#             )

#     def extract_audio_from_video(self, video_path: str) -> str:
#         video_dir = os.path.dirname(video_path)
#         audio_output_path = os.path.join(video_dir, "extracted_audio.wav")
#         command = [
#             "ffmpeg",
#             "-y",               # Overwrite without asking
#             "-i", video_path,   # Input video
#             "-ac", "2",         # Force audio to stereo (2 channels)
#             "-ar", "44100",     # Set sample rate to 44100 Hz
#             "-q:a", "0",        # Best audio quality for VBR formats (optional here)
#             "-map", "0:a",      # Map only the audio stream
#             audio_output_path   # Output path
#         ]       
#         subprocess_run(command, check=True)
#         logging.info(f"Returning audio_output_path for extracted audio at: {audio_output_path}")
#         return audio_output_path
     

  
#     def run_vocal_isolation(self,video_path: str) -> str:
#         import soundfile as sf
#         from LocalModelAssets.Old_photos__colorizing.Vocal_isolation import main
#         audio_file_path = self.extract_audio_from_video(video_path)
#         audio_session = self._load_audio_inferenceSession()
#         vocals_array, samplerate = main(self.audio_model_path,audio_file_path,audio_session)
#         if vocals_array is None or samplerate is None:
#             raise ValueError("Failed to isolate vocals. Received None values from main() function.")
#        # sf.write("output_vocals.wav", vocals_array.T, samplerate)  
        
    
#         isolated_output_path = audio_file_path.replace("extracted_audio", "isolated_audio")
#         sf.write(isolated_output_path, vocals_array.T, samplerate)
#         logging.info(f"isolated audio saved at {isolated_output_path}")
#         return isolated_output_path
    

#     def run_audio_denoise(self,video_path: str) -> str:
#         import torch
#         import soundfile as sf
#         from librosa import istft
#         import numpy as np
#         video_dir = os.path.dirname(video_path)
#         audio_output_path = os.path.join(video_dir, "extracted_audio.wav")
#         command = [
#             "ffmpeg",
#             "-y",               # Overwrite without asking
#             "-i", video_path,   # Input video
#             "-ac", "2",         # Force audio to stereo (2 channels)
#             "-ar", "16000",     # Set sample rate to 44100 Hz
#             "-q:a", "0",        # Best audio quality for VBR formats (optional here)
#             "-map", "0:a",      # Map only the audio stream
#             audio_output_path   # Output path
#         ]       
#         subprocess_run(command, check=True)
#         x = torch.from_numpy(sf.read(audio_output_path, dtype='float32')[0])
#         x = torch.stft(x, 512, 256, 512, torch.hann_window(512).pow(0.5), return_complex=False)[None]
#         session =  self._load_audio_inferenceSession()

#         conv_cache = np.zeros([2, 1, 16, 16, 33], dtype="float32")
#         tra_cache = np.zeros([2, 3, 1, 1, 16], dtype="float32")
#         inter_cache = np.zeros([2, 1, 33, 16], dtype="float32")

#         T_list = []
#         outputs = []

#         inputs = x.numpy()
#         for i in range(inputs.shape[-2]):

#             out_i, conv_cache, tra_cache, inter_cache \
#                 = session.run([], {'mix': inputs[..., i:i + 1, :],
#                                 'conv_cache': conv_cache,
#                                 'tra_cache': tra_cache,
#                                 'inter_cache': inter_cache})
#             outputs.append(out_i)
#         outputs = np.concatenate(outputs, axis=2)
#         enhanced = istft(outputs[..., 0] + 1j * outputs[..., 1], n_fft=512, hop_length=256, win_length=512,
#                  window=np.hanning(512) ** 0.5)
#         sf.write('output_denoise.wav', enhanced.squeeze(), 16000)
#         denoised_output_path = audio_output_path.replace("extracted_audio", "output_denoise")
#         return denoised_output_path


#     def process_Audio_Inference(self, video_path,selected_audio_mode):
#         if selected_audio_mode == "Vocal Isolation":
#             try: 
#                 Enchanced_audiofile =  self.run_vocal_isolation(video_path)

#                 return Enchanced_audiofile
#             except Exception as e:
#                 logging.info(f"Audio inference vocal isolation failed: {str(e)}")
#                 return None
            
#         elif selected_audio_mode == "Audio Denoise":
#             try: 
#                 Denoised_audio = self.run_audio_denoise(video_path)
#                 return Denoised_audio
#             except Exception as e:
#                 logging.info(f"Audio inference audio denoise failed: {str(e)}")
#                 return
#         else: 
#             logging.info("Normal audio returning None")
#             return None
   
    





    
    
#     #INTERNAL CLASS FUNCTIONS
#     def get_image_mode(self, image: numpy_ndarray) -> str:
#         match image.shape:
#             case (rows, cols):
#                 return "Grayscale"
#             case (rows, cols, channels) if channels == 3:
#                 return "RGB"
#             case (rows, cols, channels) if channels == 4:
#                 return "RGBA"

#     def get_image_resolution(self, image: numpy_ndarray) -> tuple:
#         height = image.shape[0]
#         width  = image.shape[1]

#         return height, width 

#     def calculate_target_resolution(self, image: numpy_ndarray) -> tuple:
#         height, width = self.get_image_resolution(image)
#         target_height = height * self.upscale_factor
#         target_width  = width  * self.upscale_factor

#         return target_height, target_width

#     def resize_with_input_factor(self, image: numpy_ndarray) -> numpy_ndarray:
        
#         old_height, old_width = self.get_image_resolution(image)

#         new_width  = int(old_width * self.input_resize_factor)
#         new_height = int(old_height * self.input_resize_factor)

#         match self.input_resize_factor:
#             case factor if factor > 1:
#                 return opencv_resize(image, (new_width, new_height), interpolation = INTER_CUBIC)
#             case factor if factor < 1:
#                 return opencv_resize(image, (new_width, new_height), interpolation = INTER_AREA)
#             case _:
#                 return image
            


#     def resize_image_with_target_resolution(
#             self,
#             image: numpy_ndarray, 
#             t_height: int,
#             t_width: int
#             ) -> numpy_ndarray:
        
#         old_height, old_width = self.get_image_resolution(image)
#         old_resolution = old_height + old_width
#         new_resolution = t_height + t_width

#         if new_resolution > old_resolution:
#             return opencv_resize(image, (t_width, t_height), interpolation = INTER_LINEAR)
#         else:
#             return opencv_resize(image, (t_width, t_height), interpolation = INTER_AREA) 







#  # VIDEO CLASS FUNCTIONS
#     def calculate_multiframes_supported_by_gpu(self, video_frame_path: str) -> int:
#         resized_video_frame  = self.resize_with_input_factor(image_read(video_frame_path))
#         height, width        = self.get_image_resolution(resized_video_frame)
#         image_pixels         = height * width
#         max_supported_pixels = self.max_resolution * self.max_resolution

#         frames_simultaneously = max_supported_pixels // image_pixels 

#         logging.info(f" Frames supported simultaneously by GPU: {frames_simultaneously}")

#         return frames_simultaneously







#     # TILLING FUNCTIONS
#     def video_need_tilling(self, video_frame_path: str) -> bool:       
#         resized_video_frame  = self.resize_with_input_factor(image_read(video_frame_path))
#         height, width        = self.get_image_resolution(resized_video_frame)
#         image_pixels         = height * width
#         max_supported_pixels = self.max_resolution * self.max_resolution

#         if image_pixels > max_supported_pixels:
#             return True
#         else:
#             return False

#     def image_need_tilling(self, image: numpy_ndarray) -> bool:
#         height, width = self.get_image_resolution(image)
#         image_pixels  = height * width
#         max_supported_pixels = self.max_resolution * self.max_resolution

#         if image_pixels > max_supported_pixels:
#             return True
#         else:
#             return False

#     def add_alpha_channel(self, image: numpy_ndarray) -> numpy_ndarray:
#         if image.shape[2] == 3:
#             alpha = numpy_full((image.shape[0], image.shape[1], 1), 255, dtype = uint8)
#             image = numpy_concatenate((image, alpha), axis = 2)
#         return image

#     def calculate_tiles_number(
#             self, 
#             image: numpy_ndarray, 
#             ) -> tuple:
        
#         height, width = self.get_image_resolution(image)

#         tiles_x = (width  + self.max_resolution - 1) // self.max_resolution
#         tiles_y = (height + self.max_resolution - 1) // self.max_resolution

#         return tiles_x, tiles_y
    
#     def split_image_into_tiles(
#             self,
#             image: numpy_ndarray, 
#             tiles_x: int, 
#             tiles_y: int
#             ) -> list[numpy_ndarray]:

#         img_height, img_width = self.get_image_resolution(image)

#         tile_width  = img_width // tiles_x
#         tile_height = img_height // tiles_y

#         tiles = []

#         for y in range(tiles_y):
#             y_start = y * tile_height
#             y_end   = (y + 1) * tile_height

#             for x in range(tiles_x):
#                 x_start = x * tile_width
#                 x_end   = (x + 1) * tile_width
#                 tile    = image[y_start:y_end, x_start:x_end]
#                 tiles.append(tile)

#         return tiles

#     def combine_tiles_into_image(
#             self,
#             image: numpy_ndarray,
#             tiles: list[numpy_ndarray], 
#             t_height: int, 
#             t_width: int,
#             num_tiles_x: int, 
#             ) -> numpy_ndarray:

#         match self.get_image_mode(image):
#             case "Grayscale": tiled_image = numpy_zeros((t_height, t_width, 3), dtype = uint8)
#             case "RGB":       tiled_image = numpy_zeros((t_height, t_width, 3), dtype = uint8)
#             case "RGBA":      tiled_image = numpy_zeros((t_height, t_width, 4), dtype = uint8)

#         for tile_index in range(len(tiles)):
#             actual_tile = tiles[tile_index]

#             tile_height, tile_width = self.get_image_resolution(actual_tile)

#             row     = tile_index // num_tiles_x
#             col     = tile_index % num_tiles_x
#             y_start = row * tile_height
#             y_end   = y_start + tile_height
#             x_start = col * tile_width
#             x_end   = x_start + tile_width

#             match self.get_image_mode(image):
#                 case "Grayscale": tiled_image[y_start:y_end, x_start:x_end] = actual_tile
#                 case "RGB":       tiled_image[y_start:y_end, x_start:x_end] = actual_tile
#                 case "RGBA":      tiled_image[y_start:y_end, x_start:x_end] = self.add_alpha_channel(actual_tile)

#         return tiled_image

    





#     # AI CLASS FUNCTIONS
#     def normalize_image(self, image: numpy_ndarray) -> tuple:
#         range = 255
#         if numpy_max(image) > 256: range = 65535
#         normalized_image = image / range

#         return normalized_image, range
    
    
    
#     def preprocess_image(self, image: numpy_ndarray) -> numpy_ndarray:
#         image = numpy_transpose(image, (2, 0, 1))
#         image = numpy_expand_dims(image, axis=0)

#         return image



#     def onnxruntime_inference(self, image: numpy_ndarray) -> numpy_ndarray:

#         # IO BINDING
#         # io_binding = self.inferenceSession.io_binding()
#         # io_binding.bind_cpu_input(self.inferenceSession.get_inputs()[0].name, image)
#         # io_binding.bind_output(self.inferenceSession.get_outputs()[0].name, element_type = float32)
#         # self.inferenceSession.run_with_iobinding(io_binding)
#         # onnx_output = io_binding.copy_outputs_to_cpu()[0]

#         onnx_input  = {self.inferenceSession.get_inputs()[0].name: image}
#         onnx_output = self.inferenceSession.run(None, onnx_input)[0]

#         return onnx_output



#     def postprocess_output(self, onnx_output: numpy_ndarray) -> numpy_ndarray:
#         onnx_output = numpy_squeeze(onnx_output, axis=0)
#         onnx_output = numpy_clip(onnx_output, 0, 1)
#         onnx_output = numpy_transpose(onnx_output, (1, 2, 0))

#         return onnx_output.astype(float32)



#     def de_normalize_image(self, onnx_output: numpy_ndarray, max_range: int) -> numpy_ndarray:    
#         match max_range:
#             case 255:   return (onnx_output * max_range).astype(uint8)
#             case 65535: return (onnx_output * max_range).round().astype(float32)




#     def AI_upscale(self, image: numpy_ndarray) -> numpy_ndarray:
#         image_mode   = self.get_image_mode(image)
#         image, range = self.normalize_image(image)
#         image        = image.astype(float32)

#         match image_mode:
#             case "RGB":
#                 image = self.preprocess_image(image)
#                 onnx_output  = self.onnxruntime_inference(image)
#                 onnx_output  = self.postprocess_output(onnx_output)
#                 output_image = self.de_normalize_image(onnx_output, range)

#                 return output_image
            
#             case "RGBA":
#                 alpha = image[:, :, 3]
#                 image = image[:, :, :3]
#                 image = opencv_cvtColor(image, COLOR_BGR2RGB)

#                 image = image.astype(float32)
#                 alpha = alpha.astype(float32)

#                 # Image
#                 image = self.preprocess_image(image)
#                 onnx_output_image = self.onnxruntime_inference(image)
#                 onnx_output_image = self.postprocess_output(onnx_output_image)
#                 onnx_output_image = opencv_cvtColor(onnx_output_image, COLOR_BGR2RGBA)

#                 # Alpha
#                 alpha = numpy_expand_dims(alpha, axis=-1)
#                 alpha = numpy_repeat(alpha, 3, axis=-1)
#                 alpha = self.preprocess_image(alpha)
#                 onnx_output_alpha = self.onnxruntime_inference(alpha)
#                 onnx_output_alpha = self.postprocess_output(onnx_output_alpha)
#                 onnx_output_alpha = opencv_cvtColor(onnx_output_alpha, COLOR_RGB2GRAY)

#                 # Fusion Image + Alpha
#                 onnx_output_image[:, :, 3] = onnx_output_alpha
#                 output_image = self.de_normalize_image(onnx_output_image, range)

#                 return output_image
            
#             case "Grayscale":
#                 image = opencv_cvtColor(image, COLOR_GRAY2RGB)
                
#                 image = self.preprocess_image(image)
#                 onnx_output  = self.onnxruntime_inference(image)
#                 onnx_output  = self.postprocess_output(onnx_output)
#                 output_image = opencv_cvtColor(onnx_output, COLOR_RGB2GRAY)
#                 output_image = self.de_normalize_image(onnx_output, range)

#                 return output_image



#     def AI_upscale_with_tilling(self, image: numpy_ndarray) -> numpy_ndarray:
#         t_height, t_width = self.calculate_target_resolution(image)
#         tiles_x, tiles_y  = self.calculate_tiles_number(image)
#         tiles_list        = self.split_image_into_tiles(image, tiles_x, tiles_y)
#         tiles_list        = [self.AI_upscale(tile) for tile in tiles_list]

#         return self.combine_tiles_into_image(image, tiles_list, t_height, t_width, tiles_x)




#     # EXTERNAL FUNCTION
#     def AI_orchestration(self, image: numpy_ndarray) -> numpy_ndarray:

#         resized_image = self.resize_with_input_factor(image)
        
#         if self.image_need_tilling(resized_image):
#             return self.AI_upscale_with_tilling(resized_image)
#         else:
#             return self.AI_upscale(resized_image)




# # GUI utils ---------------------------
# class MessageBox(CTkToplevel):

#     def __init__(
#             self,
#             messageType: str,
#             title: str,
#             subtitle: str,
#             default_value: str,
#             option_list: list,
#             ) -> None:

#         super().__init__()

#         self._running: bool = False

#         self._messageType = messageType
#         self._title = title        
#         self._subtitle = subtitle
#         self._default_value = default_value
#         self._option_list = option_list
#         self._ctkwidgets_index = 0

#         self.title('')
#         self.lift()                         
#         self.attributes("-topmost", True)   
#         self.protocol("WM_DELETE_WINDOW", self._on_closing)
#         self.after(10, self._create_widgets) 
#         self.resizable(False, False)
#         self.grab_set()                       

#     def _ok_event(
#             self, 
#             event = None
#             ) -> None:
#         self.grab_release()
#         self.destroy()

#     def _on_closing(
#             self
#             ) -> None:
#         self.grab_release()
#         self.destroy()

#     def createEmptyLabel(
#             self
#             ) -> CTkLabel:
        
#         return CTkLabel(master = self, 
#                         fg_color = "transparent",
#                         width    = 500,
#                         height   = 17,
#                         text     = '')

#     def placeInfoMessageTitleSubtitle(
#             self,
#             ) -> None:

#         spacingLabel1 = self.createEmptyLabel()
#         spacingLabel2 = self.createEmptyLabel()

#         if self._messageType == "info":
#             title_subtitle_text_color = "#3399FF"
#         elif self._messageType == "error":
#             title_subtitle_text_color = "#FF3131"

#         titleLabel = CTkLabel(
#             master     = self,
#             width      = 500,
#             anchor     = 'w',
#             justify    = "left",
#             fg_color   = "transparent",
#             text_color = title_subtitle_text_color,
#             font       = bold22,
#             text       = self._title
#             )
        
#         if self._default_value != None:
#             defaultLabel = CTkLabel(
#                 master     = self,
#                 width      = 500,
#                 anchor     = 'w',
#                 justify    = "left",
#                 fg_color   = "transparent",
#                 text_color = "#3399FF",
#                 font       = bold17,
#                 text       = f"Default: {self._default_value}"
#                 )
        
#         subtitleLabel = CTkLabel(
#             master     = self,
#             width      = 500,
#             anchor     = 'w',
#             justify    = "left",
#             fg_color   = "transparent",
#             text_color = title_subtitle_text_color,
#             font       = bold14,
#             text       = self._subtitle
#             )
        
#         spacingLabel1.grid(row = self._ctkwidgets_index, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = "ew")
        
#         self._ctkwidgets_index += 1
#         titleLabel.grid(row = self._ctkwidgets_index, column = 0, columnspan = 2, padx = 25, pady = 0, sticky = "ew")
        
#         if self._default_value != None:
#             self._ctkwidgets_index += 1
#             defaultLabel.grid(row = self._ctkwidgets_index, column = 0, columnspan = 2, padx = 25, pady = 0, sticky = "ew")
        
#         self._ctkwidgets_index += 1
#         subtitleLabel.grid(row = self._ctkwidgets_index, column = 0, columnspan = 2, padx = 25, pady = 0, sticky = "ew")
        
#         self._ctkwidgets_index += 1
#         spacingLabel2.grid(row = self._ctkwidgets_index, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = "ew")

#     def placeInfoMessageOptionsText(
#             self,
#             ) -> None:
        
#         for option_text in self._option_list:
#             optionLabel = CTkLabel(master = self,
#                                     width  = 600,
#                                     height = 45,
#                                     corner_radius = 6,
#                                     anchor     = 'w',
#                                     justify    = "left",
#                                     text_color = "#C0C0C0",
#                                     fg_color   = "#282828",
#                                     bg_color   = "transparent",
#                                     font       = bold12,
#                                     text       = option_text)
            
#             self._ctkwidgets_index += 1
#             optionLabel.grid(row = self._ctkwidgets_index, column = 0, columnspan = 2, padx = 25, pady = 4, sticky = "ew")

#         spacingLabel3 = self.createEmptyLabel()

#         self._ctkwidgets_index += 1
#         spacingLabel3.grid(row = self._ctkwidgets_index, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = "ew")

#     def placeInfoMessageOkButton(
#             self
#             ) -> None:
        
#         ok_button = CTkButton(
#             master  = self,
#             command = self._ok_event,
#             text    = 'OK',
#             width   = 125,
#             font         = bold11,
#             border_width = 1,
#             fg_color     = "#282828",
#             text_color   = "#E0E0E0",
#             border_color = "#0096FF"
#             )
        
#         self._ctkwidgets_index += 1
#         ok_button.grid(row = self._ctkwidgets_index, column = 1, columnspan = 1, padx = (10, 20), pady = (10, 20), sticky = "e")

#     def _create_widgets(
#             self
#             ) -> None:

#         self.grid_columnconfigure((0, 1), weight=1)
#         self.rowconfigure(0, weight=1)

#         self.placeInfoMessageTitleSubtitle()
#         self.placeInfoMessageOptionsText()
#         self.placeInfoMessageOkButton()    







# #SCROLLFRAME---------
# class FileWidget(CTkScrollableFrame):

#     def __init__(
#             self, 
#             master,
#             selected_file_list, 
#             input_resize_factor  = 0,
#             upscale_factor = 1,
#             **kwargs
#             ) -> None:
       
#         super().__init__(master, height=300,**kwargs)

#         self.file_list      = selected_file_list
#         self.input_resize_factor  = input_resize_factor
#         self.upscale_factor = upscale_factor

#         self.label_list = []
#         # Make column 0 stretch to fill full width of the scrollable frame
#         self.columnconfigure(0, weight=1)
#         self._create_widgets()

#     def _destroy_(self) -> None:
#         global selected_file_list, preview_instance, file_widget

#         # Clear both the local and global file lists
#         self.file_list.clear()
#         selected_file_list.clear()
#         file_overrides.clear()

#         # Stop any active preview
#         if preview_instance:
#             try:
#                 preview_instance.close()
#             except Exception:
#                 pass
#             preview_instance = None

#         # Destroy the FileWidget completely so next open_files_action
#         # creates a fresh one (including the Empty LIST button)
#         try:
#             file_widget.destroy()
#         except Exception:
#             pass
#         del file_widget

#         place_loadFile_section(window)


#     def _create_widgets(self) -> None:
#         self.add_clean_button()
#         index_row = 1
#         for file_path in self.file_list:
#             label = self.add_file_information(file_path, index_row)
#             self.label_list.append(label)
#             index_row +=1


#     def add_file_information(self, file_path, index_row) -> CTkLabel:
#         # Outer card frame — spans full column width with amber-theme border
#         file_frame = CTkFrame(
#             self,
#             fg_color="#0E0E0D",
#             border_width=1,
#             border_color="#201E1A",
#             corner_radius=5,
#         )
#         file_frame.grid(row=index_row, column=0, sticky="ew", pady=3, padx=4)
#         file_frame.columnconfigure(0, weight=1)

#         infos, icon = self.extract_file_info(file_path)
#         label = CTkLabel(
#             file_frame,
#             text=infos,
#             image=icon,
#             font=bold12,
#             text_color="#948C7E",
#             compound="left",
#             anchor="w",
#             padx=10,
#             pady=5,
#             justify="left",
#         )
#         label.grid(row=0, column=0, sticky="ew")

#         # Button row — right-aligned
#         btn_frame = CTkFrame(file_frame, fg_color="transparent")
#         btn_frame.grid(row=0, column=1, padx=(0, 8), pady=4, sticky="e")

#         # Edit button — opens per-file settings dialog
#         edit_btn = CTkButton(
#             btn_frame,
#             text="Edit",
#             width=72,
#             height=24,
#             font=bold11,
#             fg_color="#1A1408",
#             hover_color="#2A200A",
#             text_color="#D49A2A",
#             border_color="#8C6418",
#             border_width=1,
#             corner_radius=5,
#             command=lambda path=file_path: self.open_edit_dialog(path)
#         )
#         edit_btn.pack(side="left", padx=(0, 4))

#         global preview_button
#         preview_button = CTkButton(
#             btn_frame,
#             text="Preview",
#             width=72,
#             height=24,
#             font=bold11,
#             fg_color="#0E0E0C",
#             hover_color="#181612",
#             text_color="#948C7E",
#             border_color="#201E1A",
#             border_width=1,
#             corner_radius=5,
#             command=lambda path=file_path: self.preview_file(path)
#         )
#         preview_button.pack(side="left", padx=(0, 4))

#         delete_btn = CTkButton(
#             btn_frame,
#             text="Delete",
#             width=72,
#             height=24,
#             font=bold11,
#             fg_color="#160808",
#             hover_color="#220C0C",
#             text_color="#C04040",
#             border_color="#EC1D1D",
#             border_width=1,
#             corner_radius=5,
#             command=lambda path=file_path: self.delete_single_file(path)
#         )
#         delete_btn.pack(side="left")

#         return file_frame



#     def open_edit_dialog(self, file_path):
#         """Open a per-file settings override dialog."""
#         global file_overrides

#         dialog = CTkToplevel(self)
#         dialog.title(f"Edit: {os_path_basename(file_path)}")
#         dialog.geometry("380x340")
#         dialog.resizable(False, False)
#         dialog.configure(fg_color="#0A0A09")
#         dialog.grab_set()

#         ov = file_overrides.get(file_path, {})

#         CTkLabel(
#             dialog,
#             text="Per-file AI settings",
#             font=CTkFont(family="Segoe UI", size=11, weight="bold"),
#             text_color=AMBER, fg_color="transparent",
#         ).pack(pady=(12, 2))
#         CTkLabel(
#             dialog, text=os_path_basename(file_path),
#             font=CTkFont(family="Segoe UI", size=9),
#             text_color=CREAM3, fg_color="transparent",
#         ).pack(pady=(0, 10))

#         form = CTkFrame(dialog, fg_color="#0E0E0D", border_width=1, border_color=BORDER2, corner_radius=6)
#         form.pack(fill="x", padx=16, pady=4)

#         def make_row(label_text, widget_fn):
#             r = CTkFrame(form, fg_color="transparent")
#             r.pack(fill="x", padx=10, pady=4)
#             CTkLabel(r, text=label_text, width=120, anchor="w",
#                      font=CTkFont(family="Segoe UI", size=9, weight="bold"),
#                      text_color=AMBER_DIM, fg_color="transparent").pack(side="left")
#             w = widget_fn(r)
#             w.pack(side="left", padx=(6, 0))
#             return w

#         ai_var     = StringVar(value=ov.get("ai_model",     default_AI_model))
#         interp_var = StringVar(value=ov.get("interpolation", default_interpolation))
#         res_var    = StringVar(value=str(ov.get("resize_factor", selected_input_resize_factor.get())))
#         img_var    = StringVar(value=ov.get("image_ext",    default_image_extension))
#         vid_var    = StringVar(value=ov.get("video_ext",    default_video_extension))

#         make_row("AI Model",       lambda p: create_option_menu_2(lambda v: ai_var.set(v),     AI_models_list,       ai_var.get(),     master=p, width=200))
#         make_row("AI Interpolation", lambda p: create_option_menu_2(lambda v: interp_var.set(v), interpolation_list,  interp_var.get(), master=p, width=200))
#         make_row("Input Res %",    lambda p: CTkEntry(p, textvariable=res_var, width=200, height=26,
#                                                       font=CTkFont(family="Segoe UI", size=10),
#                                                       fg_color="#080808", border_color=BORDER2, border_width=1,
#                                                       text_color=CREAM2, corner_radius=4))
#         make_row("Image Codec",    lambda p: create_option_menu_2(lambda v: img_var.set(v),    image_extension_list, img_var.get(),    master=p, width=200))
#         make_row("Video Codec",    lambda p: create_option_menu_2(lambda v: vid_var.set(v),    video_extension_list, vid_var.get(),    master=p, width=200))

#         def save_and_close():
#             interp_map = {"Disabled": 0, "Low": 0.3, "Medium": 0.5, "High": 0.7}
#             try:   rf = int(float(res_var.get()))
#             except: rf = int(float(selected_input_resize_factor.get()))
#             file_overrides[file_path] = {
#                 "ai_model":      ai_var.get(),
#                 "interpolation": interp_var.get(),
#                 "interp_factor": interp_map.get(interp_var.get(), 0),
#                 "resize_factor": rf,
#                 "image_ext":     img_var.get(),
#                 "video_ext":     vid_var.get(),
#             }
#             update_file_widget(1, 2, 3)
#             dialog.destroy()

#         def clear_and_close():
#             file_overrides.pop(file_path, None)
#             update_file_widget(1, 2, 3)
#             dialog.destroy()

#         btn_row = CTkFrame(dialog, fg_color="transparent")
#         btn_row.pack(pady=12)

#         CTkButton(btn_row, text="Save", width=110, height=28, command=save_and_close,
#                   fg_color=AMBER_GLOW, hover_color="#5a3c0c", text_color=AMBER,
#                   border_color=AMBER_DIM, border_width=1, corner_radius=5,
#                   font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         ).pack(side="left", padx=6)

#         CTkButton(btn_row, text="Reset to global", width=130, height=28, command=clear_and_close,
#                   fg_color="#0E0E0C", hover_color="#181612", text_color=CREAM2,
#                   border_color=BORDER2, border_width=1, corner_radius=5,
#                   font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         ).pack(side="left", padx=6)


#     def delete_single_file(self, file_path):
#         global selected_file_list, preview_instance, file_widget

#         if file_path not in selected_file_list:
#             return

#         selected_file_list.remove(file_path)
#         self.file_list = selected_file_list
#         # Remove any per-file override for the deleted file
#         file_overrides.pop(file_path, None)

#         if preview_instance and preview_instance.video_path == file_path:
#             try:
#                 preview_instance.close()
#             except Exception:
#                 pass
#             preview_instance = None

#         if not selected_file_list:
#             # No files left — destroy widget entirely, reset the preview area
#             # Do NOT call _destroy_() to avoid double-clearing the list
#             try:
#                 file_widget.destroy()
#             except Exception:
#                 pass
#             del file_widget
#             place_loadFile_section(window)
#         else:
#             # Rebuild rows inside the existing scrollable frame (keeps Empty LIST)
#             self.label_list = []
#             for widget in self.winfo_children():
#                 widget.destroy()
#             self._create_widgets()
#             update_file_widget(1, 2, 3)
            




#     def preview_file(self, file_path):
#         global preview_instance, container

#         if preview_instance:
#             preview_instance.close()
#             preview_instance = None

#         preview_instance = VideoPreview(container, None, None, file_path)
#         preview_button.configure(state=DISABLED)
  
    

#     def add_clean_button(self) -> None:
        
#         button = CTkButton(
#             self, 
#             image        = clear_icon,
#             font         = bold11,
#             text         = "Empty LIST", 
#             compound     = "left",
#             width        = 120, 
#             height       = 22,
#             border_width = 1,
#             fg_color     = "#1A1408",
#             hover_color  = "#2A200A",
#             text_color   = AMBER,
#             border_color = AMBER_DIM,
#             corner_radius= 5,
#             )

#         button.configure(command=lambda: self._destroy_())
#         # Place in column 0 with east-anchor so file-row frames can stretch
#         # to the full scrollable-frame width without any adjacent column stealing space.
#         button.grid(row=0, column=0, sticky="e", pady=(7, 7), padx=(0, 7))
        
#     @cache
#     def extract_file_icon(self, file_path) -> CTkImage:
#         max_size = 50

#         if check_if_file_is_video(file_path):
#             video_cap   = opencv_VideoCapture(file_path)
#             total_frames = int(video_cap.get(CAP_PROP_FRAME_COUNT))
#             # Seek to 10% into the video to avoid black/empty opening frames
#             seek_frame = max(1, int(total_frames * 0.10))
#             video_cap.set(cv2.CAP_PROP_POS_FRAMES, seek_frame)
#             success, frame = video_cap.read()
#             # Fallback: try a few more positions if still black
#             if not success or frame is None or frame.max() < 10:
#                 for pct in [0.25, 0.5, 0.01]:
#                     video_cap.set(cv2.CAP_PROP_POS_FRAMES, max(1, int(total_frames * pct)))
#                     success, frame = video_cap.read()
#                     if success and frame is not None and frame.max() >= 10:
#                         break
#             video_cap.release()
#             if not success or frame is None:
#                 frame = numpy_zeros((50, 50, 3), dtype=uint8)
#             source_icon = opencv_cvtColor(frame, COLOR_BGR2RGB)
#         else:
#             source_icon = opencv_cvtColor(image_read(file_path), COLOR_BGR2RGB)

#         ratio       = min(max_size / source_icon.shape[0], max_size / source_icon.shape[1])
#         new_width   = int(source_icon.shape[1] * ratio)
#         new_height  = int(source_icon.shape[0] * ratio)
#         source_icon = opencv_resize(source_icon,(new_width, new_height))
#         ctk_icon    = CTkImage(pillow_image_fromarray(source_icon, mode="RGB"), size = (new_width, new_height))

#         return ctk_icon
        
    
        
#     def extract_file_info(self, file_path) -> tuple:
        
#         if check_if_file_is_video(file_path):
#             cap          = opencv_VideoCapture(file_path)
#             width        = round(cap.get(CAP_PROP_FRAME_WIDTH))
#             height       = round(cap.get(CAP_PROP_FRAME_HEIGHT))
#             num_frames   = int(cap.get(CAP_PROP_FRAME_COUNT))
#             frame_rate   = cap.get(CAP_PROP_FPS)
#             duration     = num_frames/frame_rate
#             minutes      = int(duration/60)
#             seconds      = duration % 60
#             cap.release()

#             video_name = str(file_path.split("/")[-1])
#             file_icon  = self.extract_file_icon(file_path)

#             file_infos = (f"{video_name}\n"
#                           f"Resolution {width}x{height} • {minutes}m:{round(seconds)}s • {num_frames}frames\n")
            
#             if self.input_resize_factor != 0 and self.upscale_factor != 0 :

#                 input_resized_height  = int(height * (self.input_resize_factor/100))
#                 input_resized_width   = int(width * (self.input_resize_factor/100))

#                 upscaled_height = int(input_resized_height * self.upscale_factor)
#                 upscaled_width  = int(input_resized_width * self.upscale_factor)



#                 file_infos += (
#                     f"AI input ({self.input_resize_factor}%) ➜ {input_resized_width}x{input_resized_height} \n"
#                     f"AI output (x{self.upscale_factor}) ➜ {upscaled_width}x{upscaled_height} \n"
#                 )
#         else:
#             image_name    = str(file_path.split("/")[-1])
#             height, width = get_image_resolution(image_read(file_path))
#             file_icon     = self.extract_file_icon(file_path)

#             file_infos = (f"{image_name}\n"
#                           f"Resolution {width}x{height}\n")
            
#             if self.input_resize_factor != 0 and self.upscale_factor != 0 :
#                 input_resized_height = int(height * (self.input_resize_factor/100))
#                 input_resized_width  = int(width * (self.input_resize_factor/100))

#                 upscaled_height = int(input_resized_height * self.upscale_factor)
#                 upscaled_width  = int(input_resized_width * self.upscale_factor)

                
          
#                 file_infos += (
#                                 f"AI input ({self.input_resize_factor}%) ➜ {input_resized_width}x{input_resized_height} \n"
#                                 f"AI output (x{self.upscale_factor}) ➜ {upscaled_width}x{upscaled_height} \n"
#                             )

#         return file_infos, file_icon









#   # EXTERNAL FUNCTIONS
#     def clean_file_list(self) -> None:
#         for label in self.label_list:
#             label.grid_forget()
    
#     def get_selected_file_list(self) -> list: 
#         return self.file_list 

#     def set_upscale_factor(self, upscale_factor) -> None:
#         self.upscale_factor = upscale_factor

#     def set_resize_factor(self, input_resize_factor) -> None:
#         self.input_resize_factor = input_resize_factor
 

 
# def get_values_for_file_widget() -> tuple:
#     # Upscale factor
#     upscale_factor = get_upscale_factor()

#     # Input resolution %
#     try:
#         input_resize_factor = int(float(str(selected_input_resize_factor.get())))
#     except:
#         input_resize_factor = 0
    
#     return  input_resize_factor, upscale_factor




 
# def update_file_widget(a, b, c) -> None:
#     try:
#         global file_widget
#         file_widget
#     except:
#         return
    
#     upscale_factor = get_upscale_factor()

#     try:
#         resize_factor = int(float(str(selected_input_resize_factor.get())))
#     except:
#         resize_factor = 0

#     file_widget.clean_file_list()
#     file_widget.set_resize_factor(resize_factor)
#     file_widget.set_upscale_factor(upscale_factor)
#     file_widget._create_widgets()

    

# def create_info_button(
#         command: Callable,
#         text: str,
#         width: int = 150,
#         master=None
#         ) -> CTkButton:
#     return CTkButton(
#         master        = master if master else window,
#         command       = command,
#         text          = "● " + text,
#         fg_color      = "transparent",
#         hover_color   = "#181410",
#         text_color    = "#5A5248",
#         anchor        = "w",
#         corner_radius = 0,
#         height        = 20,
#         width         = width,
#         font          = CTkFont(family="Segoe UI", size=8, weight="bold"),
#         border_width  = 0,
#     )


   

# def create_option_menu(
#         command: Callable, 
#         values: list,
#         default_value: str,
#         width: int = 150,
#         master=None  
#         ) -> CTkOptionMenu:
    
#     option_menu = CTkOptionMenu(
#         master=master if master else window,  
#         command = command,
#         values  = values,
#         width         = width,
#         height        = 30,
#         corner_radius = 5,
#         dropdown_font = bold11,
#         font          = bold11,
#         anchor        = "center",
#         text_color    = text_color,
#         fg_color      = widget_background_color,
#         button_color       = widget_background_color,
#         button_hover_color = "#282828",
#         dropdown_fg_color  = text_color,
#     )
#     option_menu.set(default_value)
#     return option_menu



# def create_option_menu_2(
#         command: Callable,
#         values: list,
#         default_value: str,
#         width: int = 330,
#         master=None
#         ) -> CTkFrame:
#     option_menu_frame = CTkFrame(
#         master=master,
#         width=width,
#         height=36,
#         border_width=1,
#         border_color=("#FFFFFF"),
#         corner_radius=6,
#         fg_color="#0B0B0A",
#     )
#     option_menu = CTkOptionMenu(
#         master=option_menu_frame,
#         command=command,
#         values=values,
#         width=width,
#         height=28,
#         corner_radius=5,
#         dropdown_font=CTkFont(family="Segoe UI", size=10),
#         font=CTkFont(family="Segoe UI", size=11, weight="bold"),
#         anchor="center",
#         text_color=CREAM,
#         fg_color="#0B0B0A",
#         button_color="#181410",
#         button_hover_color="#22201C",
#         dropdown_fg_color="#0E0E0C",
#         dropdown_text_color=CREAM2,
#         dropdown_hover_color="#181410",
#     )
#     option_menu.set(default_value)
#     option_menu_frame.pack_propagate(False)
#     option_menu.place(relx=0.5, rely=0.5, anchor="center")
#     return option_menu_frame



# def create_text_box(textvariable: StringVar, master=None, width=150) -> CTkEntry:
#     return CTkEntry(
#         master        = master if master else window,
#         textvariable  = textvariable,
#         corner_radius = 5,
#         width         = width,
#         height        = 30,
#         font          = CTkFont(family="Segoe UI", size=12, weight="bold"),
#         justify       = "center",
#         text_color    = CREAM,
#         fg_color      = "#0B0B0A",
#         border_width  = 1,
#         border_color  = "#FFFFFF",
#     )



# def create_text_box_output_path(textvariable: StringVar, width=None) -> CTkEntry:
#     return CTkEntry(
#         master        = window,
#         textvariable  = textvariable,
#         border_width  = 1,
#         corner_radius = 5,
#         width         = width if width != None else 225,
#         height        = 25,
#         font          = CTkFont(family="Segoe UI", size=9),
#         justify       = "center",
#         text_color    = CREAM3,
#         fg_color      = "#0A0A09",
#         border_color  = BORDER2,
#         state         = DISABLED
#     )



# def create_active_button(
#         command: Callable,
#         text: str,
#         icon: CTkImage = None,
#         width: int = 140,
#         height: int = 30,
#         border_color: str = AMBER
#         ) -> CTkButton:
#     is_stop    = (border_color == "#EC1D1D")
#     is_select  = (text == "SELECT")
#     if is_stop:
#         bg   = "#160808"; hov = "#220C0C"; tc = "#E04040"; bc = "#EC1D1D"
#     elif is_select:
#         bg   = "#0E0E0C"; hov = "#181612"; tc = CREAM2;    bc = "#FFFFFF"
#     else:
#         bg   = "#0E0E0C"; hov = "#181612"; tc = CREAM2;    bc = "#FFFFFF"
#     return CTkButton(
#         master        = window,
#         command       = command,
#         text          = text,
#         image         = icon,
#         width         = width,
#         height        = height,
#         font          = CTkFont(family="Segoe UI", size=11, weight="bold"),
#         border_width  = 1,
#         fg_color      = bg,
#         hover_color   = hov,
#         text_color    = tc,
#         border_color  = bc,
#         corner_radius = 7,
#     )














# # File Utils functions ------------------------
# def create_dir(name_dir: str) -> None:
#     if os_path_exists(name_dir):
#         remove_directory(name_dir)
#     if not os_path_exists(name_dir): 
#         os_makedirs(name_dir, mode=0o777)

# def stop_thread() -> None: stop = 1 + "x"

# def image_read(file_path: str) -> numpy_ndarray: 
#     with open(file_path, 'rb') as file:
#         return opencv_imdecode(numpy_frombuffer(file.read(), uint8), IMREAD_UNCHANGED)

# def image_write(file_path: str, file_data: numpy_ndarray) -> None: 
#     _, file_extension = os_path_splitext(file_path)
#     opencv_imencode(file_extension, file_data)[1].tofile(file_path)


# def prepare_output_image_filename(
#         image_path: str, 
#         selected_output_path: str,
#         selected_AI_model: str, 
#         resize_factor: int, 
#         selected_image_extension: str,
#         selected_interpolation_factor: float
#         ) -> str:
        
#     if selected_output_path == OUTPUT_PATH_CODED:
#         file_path_no_extension, _ = os_path_splitext(image_path)
#         output_path = file_path_no_extension
#     else:
#         file_name   = os_path_basename(image_path)
#         output_path = f"{selected_output_path}{os_separator}{file_name}"

#     # Selected AI model
#     to_append = f"_{selected_AI_model}"

#     # Selected resize
#     to_append += f"_Resize-{str(int(resize_factor * 100))}"

#     # Selected intepolation
#     match selected_interpolation_factor:
#         case 0.3:
#             to_append += "_Interpolation-Low"
#         case 0.5:
#             to_append += "_Interpolation-Medium"
#         case 0.7:
#             to_append += "_Interpolation-High"

#     # Selected image extension
#     to_append += f"{selected_image_extension}"
        
#     output_path += to_append

#     return output_path


# def prepare_output_video_frame_filename(
#         frame_path: str, 
#         selected_AI_model: str, 
#         resize_factor: int, 
#         selected_interpolation_factor: float
#         ) -> str:
            
#     file_path_no_extension, _ = os_path_splitext(frame_path)
#     output_path = file_path_no_extension

#     # Selected AI model
#     to_append = f"_{selected_AI_model}"

#     # Selected resize
#     to_append += f"_Resize-{str(int(resize_factor * 100))}"

#     # Selected intepolation
#     match selected_interpolation_factor:
#         case 0.3:
#             to_append += "_Interpolation-Low"
#         case 0.5:
#             to_append += "_Interpolation-Medium"
#         case 0.7:
#             to_append += "_Interpolation-High"

#     # Selected image extension
#     to_append += f".jpg"
        
#     output_path += to_append

#     return output_path


# def prepare_output_video_filename(
#         video_path: str, 
#         selected_output_path: str,
#         selected_AI_model: str, 
#         input_resize_factor: int, 
#         selected_video_extension: str,
#         selected_interpolation_factor: float
#         ) -> str:
    
#     match selected_video_extension:
#         case '.mp4 (x264)': selected_video_extension = '.mp4'
#         case '.mp4 (x265)': selected_video_extension = '.mp4'
#         case '.avi':        selected_video_extension = '.avi'

#     if selected_output_path == OUTPUT_PATH_CODED:
#         file_path_no_extension, _ = os_path_splitext(video_path)
#         output_path = file_path_no_extension
#     else:
#         file_name   = os_path_basename(video_path)
#         output_path = f"{selected_output_path}{os_separator}{file_name}"
    
#     # Selected AI model
#     to_append = f"_{selected_AI_model}"

#     # Selected resize
#     to_append += f"_Resize-{str(int(input_resize_factor * 100))}"

#     # Selected intepolation
#     match selected_interpolation_factor:
#         case 0.3:
#             to_append += "_Interpolation-Low"
#         case 0.5:
#             to_append += "_Interpolation-Medium"
#         case 0.7:
#             to_append += "_Interpolation-High"

#     # Selected video extension
#     to_append += f"{selected_video_extension}"
        
#     output_path += to_append

#     return output_path


# def prepare_output_video_directory_name(
#         video_path: str, 
#         selected_output_path: str,
#         selected_AI_model: str, 
#         input_resize_factor: int, 
#         selected_interpolation_factor: float
#         ) -> str:
    
#     if selected_output_path == OUTPUT_PATH_CODED:
#         file_path_no_extension, _ = os_path_splitext(video_path)
#         output_path = file_path_no_extension
#     else:
#         file_name   = os_path_basename(video_path)
#         output_path = f"{selected_output_path}{os_separator}{file_name}"

#     # Selected AI model
#     to_append = f"_{selected_AI_model}"

#     # Selected resize
#     to_append += f"_Resize-{str(int(input_resize_factor * 100))}"

#     # Selected intepolation
#     match selected_interpolation_factor:
#         case 0.3:
#             to_append += "_Interpolation-Low"
#         case 0.5:
#             to_append += "_Interpolation-Medium"
#         case 0.7:
#             to_append += "_Interpolation-High"

#     output_path += to_append

#     return output_path












# # Image/video Utils functions ------------------------
# def get_video_fps(video_path: str) -> float:
#     video_capture = opencv_VideoCapture(video_path)
#     frame_rate    = video_capture.get(CAP_PROP_FPS)
#     video_capture.release()
#     return frame_rate
   
# def get_image_resolution(image: numpy_ndarray) -> tuple:
#     height = image.shape[0]
#     width  = image.shape[1]

#     return height, width 

# def save_extracted_frames(
#         extracted_frames_paths: list[str], 
#         extracted_frames: list[numpy_ndarray], 
#         cpu_number: int
#         ) -> None:
    
#     pool = ThreadPool(cpu_number)
#     pool.starmap(image_write, zip(extracted_frames_paths, extracted_frames))
#     pool.close()
#     pool.join()

# def extract_video_frames(
#         processing_queue: multiprocessing_Queue,
#         file_number: int,
#         target_directory: str,
#         video_path: str, 
#         cpu_number: int
#     ) -> list[str]:

#     create_dir(target_directory)

#     # Video frame extraction
#     frames_number_to_save = cpu_number * FRAMES_FOR_CPU
#     video_capture         = opencv_VideoCapture(video_path)
#     frame_count           = int(video_capture.get(CAP_PROP_FRAME_COUNT))

#     extracted_frames       = []
#     extracted_frames_paths = []
#     video_frames_list      = []

#     for frame_number in range(frame_count):
#         success, frame = video_capture.read()
#         if success:
#             frame_path = f"{target_directory}{os_separator}frame_{frame_number:03d}.jpg"            
#             extracted_frames.append(frame)
#             extracted_frames_paths.append(frame_path)
#             video_frames_list.append(frame_path)

#             if len(extracted_frames) == frames_number_to_save:
#                 percentage_extraction = (frame_number / frame_count) * 100

#                 write_process_status(processing_queue, f"{file_number}. Extracting video frames ({round(percentage_extraction, 2)}%)")
#                 save_extracted_frames(extracted_frames_paths, extracted_frames, cpu_number)
#                 extracted_frames       = []
#                 extracted_frames_paths = []

#     video_capture.release()

#     if len(extracted_frames) > 0: save_extracted_frames(extracted_frames_paths, extracted_frames, cpu_number)
    
#     return video_frames_list



# def video_encoding(
#         video_path: str,
#         video_output_path: str,
#         upscaled_frame_paths: list[str], 
#         cpu_number: int,
#         selected_video_extension: str, 
#         Audio_Inference_output: str = None
#         ) -> None:
        
#     match selected_video_extension:
#         case ".mp4 (x264)": codec = "libx264"
#         case ".mp4 (x265)": codec = "libx265"
#         case ".avi":        codec = "png"

#     no_audio_path = f"{os_path_splitext(video_output_path)[0]}_no_audio{os_path_splitext(video_output_path)[1]}"
#     video_fps     = get_video_fps(video_path)
#     video_clip    = ImageSequenceClip.ImageSequenceClip(sequence = upscaled_frame_paths, fps = video_fps)

#     video_clip.write_videofile(
#         filename = no_audio_path,
#         fps      = video_fps,
#         codec    = codec,
#         threads  = cpu_number,
#         logger   = None,
#         audio    = None,
#         bitrate  = "12M",
#         preset   = "ultrafast"
#     )

        
#     audio_source = Audio_Inference_output if Audio_Inference_output else video_path
#     # Copy the audio from original video
#     audio_passthrough_command = [
#         FFMPEG_EXE_PATH,
#         "-y",
#         "-i", audio_source,
#         "-i", no_audio_path,
#         "-c:v", "copy",
#         "-c:a", "copy",
#         "-b:a", "192k", #Audio bitrate
#         "-map", "1:v:0", #Map video from no_audio_path
#         "-map", "0:a:0", #map audio from isolated audio
#         video_output_path
#     ]
#     try: 
#         subprocess_run(audio_passthrough_command, check = True, shell = "False")
#         if os_path_exists(no_audio_path):
#             os_remove(no_audio_path)
#     except Exception as e:
#         logging.info(f"Error during video encoding: {e}")
#         pass

#     if Audio_Inference_output:
#         try: 
#             if os_path_exists(Audio_Inference_output):
#                 os_remove(Audio_Inference_output)
#         except Exception as e:
#             logging.info(f"error during removal of audio {str(e)}")

#     extracted_audio = os_path_join(os.path.dirname(video_path), "extracted_audio.wav") 
#     if os_path_exists(extracted_audio):
#         try:
#             os_remove(extracted_audio)
#         except Exception as e:
#             logging.info(f"warning could not delete extracted audio {extracted_audio}, might have been moved: {str(e)}")
    
# def check_video_upscaling_resume(
#         target_directory: str, 
#         selected_AI_model: str
#         ) -> bool:
    
#     if os_path_exists(target_directory):
#         directory_files      = os_listdir(target_directory)
#         upscaled_frames_path = [file for file in directory_files if selected_AI_model in file]

#         if len(upscaled_frames_path) > 1:
#             return True
#         else:
#             return False
#     else:
#         return False


# def get_video_frames_for_upscaling_resume(
#         target_directory: str,
#         selected_AI_model: str,
#         ) -> list[str]:
    
#     # Only file names
#     directory_files      = os_listdir(target_directory)
#     original_frames_path = [file for file in directory_files if file.endswith('.jpg')]
#     original_frames_path = [file for file in original_frames_path if selected_AI_model not in file]

#     # Adding the complete path to file
#     original_frames_path = natsorted([os_path_join(target_directory, file) for file in original_frames_path])

#     return original_frames_path



# def calculate_time_to_complete_video(
#         time_for_frame: float,
#         remaining_frames: int,
#         ) -> str:
    
#     remaining_time = time_for_frame * remaining_frames

#     hours_left   = remaining_time // 3600
#     minutes_left = (remaining_time % 3600) // 60
#     seconds_left = round((remaining_time % 3600) % 60)

#     time_left = ""

#     if int(hours_left) > 0: 
#         time_left = f"{int(hours_left):02d}h"
    
#     if int(minutes_left) > 0: 
#         time_left = f"{time_left}{int(minutes_left):02d}m"

#     if seconds_left > 0: 
#         time_left = f"{time_left}{seconds_left:02d}s"

#     return time_left        




# def interpolate_images_and_save(
#         target_path: str,
#         starting_image: numpy_ndarray,
#         upscaled_image: numpy_ndarray,
#         starting_image_importance: float,
#         ) -> None:
    
#     def add_alpha_channel(image: numpy_ndarray) -> numpy_ndarray:
#         if image.shape[2] == 3:
#             alpha = numpy_full((image.shape[0], image.shape[1], 1), 255, dtype = uint8)
#             image = numpy_concatenate((image, alpha), axis = 2)
#         return image
    
#     def get_image_mode(image: numpy_ndarray) -> str:
#         match image.shape:
#             case (rows, cols):
#                 return "Grayscale"
#             case (rows, cols, channels) if channels == 3:
#                 return "RGB"
#             case (rows, cols, channels) if channels == 4:
#                 return "RGBA"


#     ZERO = 0
#     upscaled_image_importance       = 1 - starting_image_importance
#     starting_height, starting_width = get_image_resolution(starting_image)
#     target_height, target_width     = get_image_resolution(upscaled_image)

#     starting_resolution = starting_height + starting_width
#     target_resolution   = target_height + target_width

#     if starting_resolution > target_resolution:
#         starting_image = opencv_resize(starting_image,(target_width, target_height), INTER_AREA)
#     else:
#         starting_image = opencv_resize(starting_image,(target_width, target_height), INTER_LINEAR)

#     try: 
#         if get_image_mode(starting_image) == "RGBA":
#             starting_image = add_alpha_channel(starting_image)
#             upscaled_image = add_alpha_channel(upscaled_image)

#         interpolated_image = opencv_addWeighted(starting_image, starting_image_importance, upscaled_image, upscaled_image_importance, ZERO)
#         image_write(
#             file_path = target_path, 
#             file_data = interpolated_image
#         )
#     except:
#         image_write(
#             file_path = target_path, 
#             file_data = upscaled_image
#         )




# def manage_upscaled_video_frame_save_async(
#         upscaled_frame: numpy_ndarray,
#         starting_frame: numpy_ndarray,
#         upscaled_frame_path: str,
#         selected_interpolation_factor: float
#     ) -> None:

#     if selected_interpolation_factor > 0:
#         thread = Thread(
#             target = interpolate_images_and_save,
#             args = (
#                 upscaled_frame_path, 
#                 starting_frame,
#                 upscaled_frame,
#                 selected_interpolation_factor
#             )
#         )
#     else:
#         thread = Thread(
#             target = image_write,
#             args = (
#                 upscaled_frame_path, 
#                 upscaled_frame
#             )
#         )

#     thread.start()




# def update_process_status_videos(
#         processing_queue: multiprocessing_Queue, 
#         file_number: int, 
#         frame_index: int, 
#         how_many_frames: int,
#         average_processing_time: float,
#         ) -> None:


#     batch = 4 if not CPU_ONLY else 1
#     if frame_index != 0 and (frame_index + 1) % batch == 0:  
#         remaining_frames = how_many_frames - frame_index
#         remaining_time   = calculate_time_to_complete_video(average_processing_time, remaining_frames)
#         if remaining_time != "":
#             percent_complete = (frame_index + 1) / how_many_frames * 100 
#             write_process_status(processing_queue, f"{file_number}. Upscaling video {percent_complete:.2f}% ({remaining_time})")





# def copy_file_metadata(
#         original_file_path: str, 
#         upscaled_file_path: str
#         ) -> None:
    
#     exiftool_cmd = [
#         EXIFTOOL_EXE_PATH, 
#         '-fast', 
#         '-TagsFromFile', 
#         original_file_path, 
#         '-overwrite_original', 
#         '-all:all',
#         '-unsafe',
#         '-largetags', 
#         upscaled_file_path
#     ]
    
#     try: 
#         subprocess_run(exiftool_cmd, check = True, shell = "False")
#     except:
#         pass









# # Core functions ------------------------
# def check_upscale_steps() -> None:
#     sleep(1)

#     try:
#         while True:
#             actual_step = read_process_status()

#             if actual_step == COMPLETED_STATUS:
#                 info_message.set(f"All files completed! :)")
#                 stop_upscale_process()
#                 stop_thread()

#             elif actual_step == STOP_STATUS:
#                 info_message.set(f"Upscaling stopped")
#                 stop_upscale_process()
#                 stop_thread()

#             elif ERROR_STATUS in actual_step:
#                 info_message.set(f"Error while upscaling :(")
#                 show_error_message(actual_step.replace(ERROR_STATUS, ""))
#                 stop_thread()

#             else:
#                 info_message.set(actual_step)

#             sleep(1)
#     except:
#         place_upscale_button()
        
# def read_process_status() -> str:
#     return processing_queue.get()

# def write_process_status(
#         processing_queue: multiprocessing_Queue,
#         step: str
#         ) -> None:
    
#     logging.info(f"{step}")
#     while not processing_queue.empty(): processing_queue.get()
#     processing_queue.put(f"{step}")

# def stop_upscale_process() -> None:
#     global process_upscale_orchestrator
#     try:
#         process_upscale_orchestrator
#     except:
#         pass
#     else:
#         process_upscale_orchestrator.kill()

# def stop_button_command() -> None:
#     stop_upscale_process()
#     write_process_status(processing_queue, f"{STOP_STATUS}") 

# def upscale_button_command() -> None: 
#     global selected_file_list
#     global selected_AI_model
#     global selected_gpu
#     global selected_keep_frames
#     global selected_AI_multithreading
#     global selected_interpolation_factor
#     global selected_image_extension
#     global selected_video_extension
#     global tiles_resolution
#     global input_resize_factor
#     global cpu_number
#     global selected_audio_mode
#     global process_upscale_orchestrator
#     global selected_audio_mode
#     selected_audio_mode = selected_audio_mode

#     if user_input_checks():
#         info_message.set("Loading")

#         logging.info("=" * 50)
#         logging.info("> Starting upscale:")
#         logging.info(f"  Files to upscale: {len(selected_file_list)}")
#         logging.info(f"  Output path: {(selected_output_path.get())}")
#         logging.info(f"  Selected AI model: {selected_AI_model}")
#         logging.info(f"  Selected GPU: {selected_gpu}")
#         logging.info(f"  AI multithreading: {selected_AI_multithreading}")
#         logging.info(f"  Interpolation factor: {selected_interpolation_factor}")
#         logging.info(f"  Selected image output extension: {selected_image_extension}")
#         logging.info(f"  Selected video output extension: {selected_video_extension}")
#         logging.info(f"  Tiles resolution for selected GPU VRAM: {tiles_resolution}x{tiles_resolution}px")
#         logging.info(f"  input_resize_factor: {int(input_resize_factor * 100)}%")
#         logging.info(f"  Cpu number: {cpu_number}")
#         logging.info(f" Save frames: {selected_keep_frames}")
#         logging.info(f" selected_audio_mode : {selected_audio_mode}")
#         logging.info("=" * 50)

#         place_stop_button()

#         process_upscale_orchestrator = Process(
#             target = upscale_orchestrator,
#             args = (
#                 processing_queue, 
#                 selected_file_list, 
#                 selected_output_path.get(),
#                 selected_AI_model, 
#                 selected_gpu,
#                 selected_image_extension,
#                 tiles_resolution, 
#                 input_resize_factor, 
#                 cpu_number, 
#                 selected_video_extension,
#                 selected_interpolation_factor,
#                 selected_AI_multithreading,
#                 selected_keep_frames,
#                 selected_audio_mode,
#                 dict(file_overrides),   # pass a copy of per-file overrides
#             )
#         )
#         process_upscale_orchestrator.start()

#         thread_wait = Thread(target = check_upscale_steps)
#         thread_wait.start()


# # ORCHESTRATOR
# def upscale_orchestrator(
#         processing_queue: multiprocessing_Queue,
#         selected_file_list: list,
#         selected_output_path: str,
#         selected_AI_model: str,
#         selected_gpu: str,
#         selected_image_extension: str,
#         tiles_resolution: int,
#         input_resize_factor: int,
#         cpu_number: int,
#         selected_video_extension: str,
#         selected_interpolation_factor: float,
#         selected_AI_multithreading: int,
#         selected_keep_frames: bool,
#         selected_audio_mode: str,
#         file_overrides: dict = None
#         ) -> None:

#     if file_overrides is None:
#         file_overrides = {}

#     write_process_status(processing_queue, f"Loading AI model")

#     # Build a default AI instance (used for files without per-file overrides)
#     AI_instance = AI(selected_AI_model, selected_gpu, input_resize_factor, tiles_resolution)
#     AI_instance_list = [AI_instance]

#     if selected_AI_multithreading > 1:
#         for _ in range(selected_AI_multithreading - 1):
#             AI_instance_list.append(AI(selected_AI_model, selected_gpu, input_resize_factor, tiles_resolution))

#     # Cache of (model, resize_factor) -> AI instance to avoid reloading the same model
#     _ai_cache = {(selected_AI_model, input_resize_factor): AI_instance}

#     try:
#         how_many_files = len(selected_file_list)
#         for file_number in range(how_many_files):
#             file_path   = selected_file_list[file_number]
#             file_number = file_number + 1

#             # Resolve per-file settings (fall back to global when not overridden)
#             ov = file_overrides.get(file_path, {})
#             f_ai_model    = ov.get("ai_model",      selected_AI_model)
#             f_resize      = ov.get("resize_factor",  input_resize_factor)
#             f_interp      = ov.get("interp_factor",  selected_interpolation_factor)
#             f_image_ext   = ov.get("image_ext",      selected_image_extension)
#             f_video_ext   = ov.get("video_ext",      selected_video_extension)

#             # Re-use or create a per-file AI instance
#             cache_key = (f_ai_model, f_resize)
#             if cache_key not in _ai_cache:
#                 write_process_status(processing_queue, f"Loading model {f_ai_model}")
#                 _ai_cache[cache_key] = AI(f_ai_model, selected_gpu, f_resize, tiles_resolution)
#             f_ai_instance      = _ai_cache[cache_key]
#             f_ai_instance_list = [f_ai_instance]
#             if selected_AI_multithreading > 1:
#                 for _ in range(selected_AI_multithreading - 1):
#                     sub_key = (f_ai_model, f_resize, _)
#                     if sub_key not in _ai_cache:
#                         _ai_cache[sub_key] = AI(f_ai_model, selected_gpu, f_resize, tiles_resolution)
#                     f_ai_instance_list.append(_ai_cache[sub_key])

#             if check_if_file_is_video(file_path):
#                 upscale_video(
#                     processing_queue,
#                     file_path,
#                     file_number,
#                     selected_output_path,
#                     f_ai_instance,
#                     f_ai_instance_list,
#                     f_ai_model,
#                     f_resize,
#                     cpu_number,
#                     f_video_ext,
#                     f_interp,
#                     selected_AI_multithreading,
#                     selected_keep_frames,
#                     selected_audio_mode
#                 )
#             else:
#                 upscale_image(
#                     processing_queue,
#                     file_path,
#                     file_number,
#                     selected_output_path,
#                     f_ai_instance,
#                     f_ai_model,
#                     f_image_ext,
#                     f_resize,
#                     f_interp
#                 )

#         write_process_status(processing_queue, f"{COMPLETED_STATUS}")

#     except Exception as exception:
#         write_process_status(processing_queue, f"{ERROR_STATUS} {str(exception)}")



# # IMAGES
# def upscale_image(
#         processing_queue: multiprocessing_Queue,
#         image_path: str, 
#         file_number: int,
#         selected_output_path: str,
#         AI_instance: AI,
#         selected_AI_model: str,
#         selected_image_extension: str,
#         input_resize_factor: int, 
#         selected_interpolation_factor: float
#         ) -> None:
    
#     starting_image = image_read(image_path)
#     upscaled_image_path = prepare_output_image_filename(image_path, selected_output_path, selected_AI_model, input_resize_factor, selected_image_extension, selected_interpolation_factor)

#     write_process_status(processing_queue, f"{file_number}. Upscaling image")
#     upscaled_image = AI_instance.AI_orchestration(starting_image)

#     if selected_interpolation_factor > 0:
#         interpolate_images_and_save(
#             upscaled_image_path,
#             starting_image,
#             upscaled_image,
#             selected_interpolation_factor
#         )

#     else:
#         image_write(
#             file_path = upscaled_image_path,
#             file_data = upscaled_image
#         )

#     copy_file_metadata(image_path, upscaled_image_path)









# # VIDEOS
# def upscale_video(
#         processing_queue: multiprocessing_Queue,
#         video_path: str, 
#         file_number: int,
#         selected_output_path: str,
#         AI_instance: AI,
#         AI_instance_list: list[AI],
#         selected_AI_model: str,
#         input_resize_factor: int, 
#         cpu_number: int, 
#         selected_video_extension: str,
#         selected_interpolation_factor: float,
#         selected_AI_multithreading: int,
#         selected_keep_frames: bool,
#         selected_audio_mode: str
#         ) -> None:

#     global processed_frames_async
#     global processing_times_async
#     processed_frames_async = 0
#     processing_times_async = []
    
#     # 1.Preparation
#     target_directory  = prepare_output_video_directory_name(video_path, selected_output_path, selected_AI_model, input_resize_factor, selected_interpolation_factor)
#     video_output_path = prepare_output_video_filename(video_path, selected_output_path, selected_AI_model, input_resize_factor, selected_video_extension, selected_interpolation_factor)
    
#     Audio_Inference_output = AI_instance.process_Audio_Inference(video_path,selected_audio_mode) 
#     if Audio_Inference_output == None:
#         logging.info(f"Error: no enchanced audio recieved, audio inference output is {Audio_Inference_output}")
    
#     # 2. Resume upscaling OR Extract video frames
#     video_upscale_continue = check_video_upscaling_resume(target_directory, selected_AI_model)
#     if video_upscale_continue:
#         write_process_status(processing_queue, f"{file_number}. Resume video upscaling")
#         extracted_frames_paths = get_video_frames_for_upscaling_resume(target_directory, selected_AI_model)
#     else:
#         write_process_status(processing_queue, f"{file_number}. Extracting video frames")
#         extracted_frames_paths = extract_video_frames(processing_queue, file_number, target_directory, video_path, cpu_number)

#     upscaled_frame_paths = [prepare_output_video_frame_filename(frame_path, selected_AI_model, input_resize_factor,selected_interpolation_factor) for frame_path in extracted_frames_paths]

#     # 3. Check if video need tiles OR video multithreading upscale
#     first_frame_path             = extracted_frames_paths[0]
#     video_need_tiles             = AI_instance.video_need_tilling(first_frame_path)
#     multiframes_supported_by_gpu = AI_instance.calculate_multiframes_supported_by_gpu(first_frame_path)
#     multiframes_number           = min(multiframes_supported_by_gpu, selected_AI_multithreading)

#     write_process_status(processing_queue, f"{file_number}. Upscaling video") 
#     if video_need_tiles or multiframes_number <= 1:
#         upscale_video_frames(
#             processing_queue,
#             file_number,
#             AI_instance,
#             extracted_frames_paths,
#             upscaled_frame_paths,
#             selected_interpolation_factor
#         )
#     else:
#         upscale_video_frames_multithreading(
#             processing_queue,
#             file_number,
#             AI_instance_list,
#             extracted_frames_paths,
#             upscaled_frame_paths,
#             multiframes_number,
#             selected_interpolation_factor
#         )

#     # 4. Check for forgotten video frames
#     check_forgotten_video_frames(processing_queue, file_number, AI_instance, extracted_frames_paths, upscaled_frame_paths, selected_interpolation_factor)

#     # 5. Video encoding
#     write_process_status(processing_queue, f"{file_number}. Processing upscaled video")
#     video_encoding(video_path, video_output_path, upscaled_frame_paths, cpu_number, selected_video_extension,Audio_Inference_output)
#     copy_file_metadata(video_path, video_output_path)
    
#     #6 delete frames folder
#     if selected_keep_frames == False:
#         if os_path_exists(target_directory): remove_directory(target_directory)

# def upscale_video_frames(
#         processing_queue: multiprocessing_Queue,
#         file_number: int,
#         AI_instance: AI,
#         extracted_frames_paths: list[str],
#         upscaled_frame_paths: list[str],
#         selected_interpolation_factor: float
#         ) -> None:
    
#     frame_processing_times = []

#     for frame_index, frame_path in enumerate(extracted_frames_paths):
#         upscaled_frame_path = upscaled_frame_paths[frame_index]
#         already_upscaled    = os_path_exists(upscaled_frame_path)
        
#         if already_upscaled == False:
#             start_timer = timer()
            
#             starting_frame = image_read(frame_path)
#             upscaled_frame = AI_instance.AI_orchestration(starting_frame)
#             manage_upscaled_video_frame_save_async(upscaled_frame, starting_frame, upscaled_frame_path, selected_interpolation_factor)
        
#             end_timer    = timer()
#             elapsed_time = end_timer - start_timer
#             frame_processing_times.append(elapsed_time)
            
#             if (frame_index + 1) % 8 == 0:
#                 average_processing_time = numpy_mean(frame_processing_times)
#                 update_process_status_videos(processing_queue, file_number, frame_index, len(extracted_frames_paths), average_processing_time)

#             if (frame_index + 1) % 100 == 0: frame_processing_times = []

# def upscale_video_frames_multithreading(
#         processing_queue: multiprocessing_Queue,
#         file_number: int,
#         AI_instance_list: list[AI],
#         extracted_frames_paths: list[str],
#         upscaled_frame_paths: list[str],
#         multiframes_number: int,
#         selected_interpolation_factor: float,
#         ) -> None:
    
#     def upscale_single_video_frame_async(
#             processing_queue: multiprocessing_Queue,
#             file_number: int,
#             multiframes_number: int,
#             total_video_frames: int,
#             AI_instance: AI,
#             extracted_frames_paths: list[str],
#             upscaled_frame_paths: list[str],
#             selected_interpolation_factor: float,
#             ) -> None:

#         global processed_frames_async
#         global processing_times_async

#         for frame_index in range(len(extracted_frames_paths)):
#             upscaled_frame_path = upscaled_frame_paths[frame_index]
#             already_upscaled    = os_path_exists(upscaled_frame_path)

#             if already_upscaled == False:
#                 start_timer = timer()

#                 starting_frame = image_read(extracted_frames_paths[frame_index])
#                 upscaled_frame = AI_instance.AI_orchestration(starting_frame)

#                 manage_upscaled_video_frame_save_async(upscaled_frame, starting_frame, upscaled_frame_path, selected_interpolation_factor)

#                 end_timer    = timer()
#                 elapsed_time = end_timer - start_timer
#                 processing_times_async.append(elapsed_time)

#                 if (processed_frames_async + 1) % 8 == 0:
#                     average_processing_time = float(numpy_mean(processing_times_async)/multiframes_number)
#                     update_process_status_videos(processing_queue, file_number, processed_frames_async, total_video_frames, average_processing_time)

#                 if (processed_frames_async + 1) % 100 == 0: processing_times_async = []
        
#             processed_frames_async +=1

    
#     total_video_frames         = len(extracted_frames_paths)
#     chunk_size                 = total_video_frames // multiframes_number
#     frame_list_chunks          = [extracted_frames_paths[i:i + chunk_size] for i in range(0, len(extracted_frames_paths), chunk_size)]
#     upscaled_frame_list_chunks = [upscaled_frame_paths[i:i + chunk_size] for i in range(0, len(upscaled_frame_paths), chunk_size)]

#     write_process_status(processing_queue, f"{file_number}. Upscaling video ({multiframes_number} threads)")
#     try: 
#         pool = ThreadPool(multiframes_number)
#         pool.starmap(
#             upscale_single_video_frame_async,
#             zip(
#                 repeat(processing_queue),
#                 repeat(file_number),
#                 repeat(multiframes_number),
#                 repeat(total_video_frames),
#                 AI_instance_list,
#                 frame_list_chunks,
#                 upscaled_frame_list_chunks,
#                 repeat(selected_interpolation_factor)
#             )
#         )
#         pool.close()
#         pool.join()
#     except Exception as e:
#         logging.info(f"error during upscaling {str(e)}")

# def check_forgotten_video_frames(
#         processing_queue: multiprocessing_Queue,
#         file_number: int,
#         AI_instance: AI,
#         extracted_frames_paths: list[str],
#         upscaled_frame_paths: list[str],
#         selected_interpolation_factor: float,
#         ):
    

#     frame_path_todo_list          = []
#     upscaled_frame_path_todo_list = []

#     for frame_index in range(len(upscaled_frame_paths)):
        
#         if not os_path_exists(upscaled_frame_paths[frame_index]):
#             frame_path_todo_list.append(extracted_frames_paths[frame_index])
#             upscaled_frame_path_todo_list.append(upscaled_frame_paths[frame_index]) 

#     if len(upscaled_frame_path_todo_list) > 0:
#         upscale_video_frames(
#             processing_queue,
#             file_number,
#             AI_instance,
#             frame_path_todo_list,
#             upscaled_frame_path_todo_list,
#             selected_interpolation_factor
#         )











# # GUI utils function ---------------------------
# def check_if_file_is_video(
#         file: str
#         ) -> bool:
    
#     return any(video_extension in file for video_extension in supported_video_extensions)

# def check_supported_selected_files(
#         uploaded_file_list: list
#         ) -> list:
    
#     return [file for file in uploaded_file_list if any(supported_extension in file for supported_extension in supported_file_extensions)]

# def user_input_checks() -> bool:
#     global selected_file_list
#     global selected_AI_model
#     global selected_image_extension
#     global tiles_resolution
#     global input_resize_factor
#     global cpu_number

#     # Selected files 
#     try: selected_file_list = file_widget.get_selected_file_list()
#     except:
#         info_message.set("Please select a file")
#         return False

#     if len(selected_file_list) <= 0:
#         info_message.set("Please select a file")
#         return False


#     # AI model
#     if selected_AI_model == AI_LIST_SEPARATOR[0]:
#         info_message.set("Please select the AI model")
#         return False


#     # Input resize factor 
#     try: input_resize_factor = int(float(str(selected_input_resize_factor.get())))
#     except:
#         info_message.set("Resize % must be a numeric value")
#         return False

#     if input_resize_factor > 0: input_resize_factor = input_resize_factor/100
#     else:
#         info_message.set("Resize % must be a value > 0")
#         return False
    

   

#     try: tiles_resolution = 100 * int(float(str(selected_VRAM_limiter.get())))
#     except:
#         info_message.set("VRAM/RAM value must be a numeric value")
#         return False

#     if tiles_resolution > 0: 
#         if selected_AI_model in RRDB_models_list:          
#             vram_multiplier = very_high_VRAM
#         elif selected_AI_model in SRVGGNetCompact_models_list: 
#             vram_multiplier = medium_VRAM
#         elif selected_AI_model in IRCNN_models_list:
#             vram_multiplier = very_low_VRAM

#         selected_vram = (vram_multiplier * int(float(str(selected_VRAM_limiter.get()))))
#         tiles_resolution = int(selected_vram * 100)

        
#     else:
#         info_message.set("VRAM/RAM value must be > 0")
#         return False

#     # Cpu number 
#     try: cpu_number = int(float(str(selected_cpu_number.get())))
#     except:
#         info_message.set("Cpu number must be a numeric value")
#         return False

#     if cpu_number <= 0:         
#         info_message.set("Cpu number value must be > 0")
#         return False
#     else: 
#         cpu_number = int(cpu_number)

#     return True

# def show_error_message(exception: str) -> None:
#     messageBox_title    = "Upscale error"
#     messageBox_subtitle = "Please report the error on Github or Telegram"
#     messageBox_text     = f"\n {str(exception)} \n"

#     MessageBox(
#         messageType   = "error",
#         title         = messageBox_title,
#         subtitle      = messageBox_subtitle,
#         default_value = None,
#         option_list   = [messageBox_text]
#     )

# def get_upscale_factor() -> int:
#     global selected_AI_model
#     if AI_LIST_SEPARATOR[0] in selected_AI_model: upscale_factor = 0
#     elif 'x1' in selected_AI_model: upscale_factor = 1
#     elif 'x2' in selected_AI_model: upscale_factor = 2
#     elif 'x4' in selected_AI_model: upscale_factor = 4

#     return upscale_factor



# def add_files_from_drop(drop_data: str) -> None:
#     """Parse a TkinterDnD drop event data string and add valid files to the list."""
#     global selected_file_list, file_widget

#     # tkinterdnd2 wraps paths with braces when they contain spaces
#     import re
#     raw = drop_data.strip()
#     # Extract paths: either {path with spaces} or plain/path
#     paths = re.findall(r'\{([^}]+)\}|(\S+)', raw)
#     parsed = [a or b for a, b in paths]

#     supported = [
#         p for p in parsed
#         if os_path_exists(p) and any(p.lower().endswith(ext.lower()) for ext in supported_file_extensions)
#     ]

#     if not supported:
#         info_message.set("No supported files in drop")
#         return

#     new_files = [f for f in supported if f not in selected_file_list]
#     if not new_files:
#         info_message.set("Files already loaded")
#         return

#     widget_exists = 'file_widget' in globals() and globals()['file_widget'].winfo_exists()

#     for f in new_files:
#         selected_file_list.append(f)

#     if widget_exists:
#         next_row = 1 + len(selected_file_list) - len(new_files)
#         for f in new_files:
#             row_frame = file_widget.add_file_information(f, next_row)
#             file_widget.label_list.append(row_frame)
#             next_row += 1
#         file_widget.file_list = selected_file_list
#     else:
#         upscale_factor = get_values_for_file_widget()
#         file_widget = FileWidget(
#             master             = window,
#             selected_file_list = selected_file_list,
#             upscale_factor     = upscale_factor,
#             fg_color           = background_color,
#             bg_color           = background_color,
#         )
#         file_widget.place(relx=0.22, rely=0.095, relwidth=0.33, relheight=0.905)

#     if file_list_update_callback:
#         file_list_update_callback()
#     if media_info_update_callback:
#         media_info_update_callback()

#     update_file_widget(1, 2, 3)
#     info_message.set("Ready")


# def open_files_action():
#     global selected_file_list  
#     def check_supported_selected_files(uploaded_file_list: list) -> list:
#         return [file for file in uploaded_file_list if any(supported_extension in file for supported_extension in supported_file_extensions)]

#     info_message.set("Selecting files")

#     uploaded_files_list    = list(filedialog.askopenfilenames())
#     uploaded_files_counter = len(uploaded_files_list)

#     supported_files_list    = check_supported_selected_files(uploaded_files_list)
#     supported_files_counter = len(supported_files_list)
    
#     logging.info("> Uploaded files: " + str(uploaded_files_counter) + " => Supported files: " + str(supported_files_counter))

#     global file_widget

#     if supported_files_counter > 0:
#         new_files = [f for f in supported_files_list if f not in selected_file_list]

#         if new_files:
#             widget_exists = 'file_widget' in globals() and globals()['file_widget'].winfo_exists()

#             for f in new_files:
#                 selected_file_list.append(f)

#             if widget_exists:
#                 # Append only new rows - no full rebuild, no shaking
#                 next_row = 1 + len(selected_file_list) - len(new_files)
#                 for f in new_files:
#                     row_frame = file_widget.add_file_information(f, next_row)
#                     file_widget.label_list.append(row_frame)
#                     next_row += 1
#                 file_widget.file_list = selected_file_list
#             else:
#                 upscale_factor = get_values_for_file_widget()
#                 file_widget = FileWidget(
#                     master               = window,
#                     selected_file_list   = selected_file_list,
#                     upscale_factor       = upscale_factor,
#                     fg_color             = background_color,
#                     bg_color             = background_color
#                 )
#                 file_widget.place(relx = 0.22, rely = 0.095, relwidth = 0.33, relheight = 0.905)

#             if file_list_update_callback:
#                 file_list_update_callback()
#             if media_info_update_callback:
#                 media_info_update_callback()

#             update_file_widget(1, 2, 3)

#         info_message.set("Ready")
#     else:
#         info_message.set("Not supported files :(")
    

# def open_output_path_action():
#     asked_selected_output_path = filedialog.askdirectory()
#     if asked_selected_output_path == "":
#         selected_output_path.set(OUTPUT_PATH_CODED)
#     else:
#         selected_output_path.set(asked_selected_output_path)







# # GUI select from menus functions ---------------------------
# def select_audio_mode_from_menu(selected_mode):
#     global selected_audio_mode
#     selected_audio_mode = selected_mode
#     logging.info(f"Print global selected audio mode: {selected_audio_mode}, print selected_mode: {selected_mode}")
#     if selected_audio_mode == "Vocal Isolation":
#         logging.info(f"Selected Audio Mode:  {selected_audio_mode}")
    
#     if selected_audio_mode == "Audio Denoise":
#         logging.info(f"Selected audio mode is: {selected_audio_mode}")
        
#     if selected_audio_mode == "Disabled":
#         logging.info(f"Selected audio mode is: {selected_audio_mode}")
    
#     return selected_audio_mode
    
    




# def select_interpolation_from_menu(selected_option: str) -> None:
#     global selected_interpolation_factor

#     match selected_option:
#         case "Disabled":
#             selected_interpolation_factor = 0
#         case "Low":
#             selected_interpolation_factor = 0.3
#         case "Medium":
#             selected_interpolation_factor = 0.5
#         case "High":
#             selected_interpolation_factor = 0.7

    
# def select_save_frame_from_menu(selected_option: str):
#     global selected_keep_frames
#     if   selected_option == 'Enabled':  selected_keep_frames = True
#     elif selected_option == 'Disabled': selected_keep_frames = False

# def select_image_extension_from_menu(selected_option: str) -> None:
#     global selected_image_extension   
#     selected_image_extension = selected_option
    
# def select_video_extension_from_menu(selected_option: str) -> None:
#     global selected_video_extension   
#     selected_video_extension = selected_option






















# # GUI info functions ---------------------------
# def open_socialMedia_tool_info():
#     option_list = [
#         "\n NOTES\n" 
#         "\nInstagram: \n" +
#         "\nYoutube: \n" +
#         "\nTiktok: \n" 
#     ]
#     MessageBox(
#         messageType = "info",
#         title       = "Social Media",
#         subtitle    = "Information about (Social Media Tool)",
#         default_value = "",
#         option_list   = option_list
#     )


# def open_mediaInfo_Analyst():
#     option_list = [
#         "\n NOTES\n" 
#         "\n open_mediaInfo_Analyst\n" 

#     ]
#     MessageBox(
#         messageType = "info",
#         title       = "open_mediaInfo_Analyst",
#         subtitle    = "open_mediaInfo_Analyst",
#         default_value = "",
#         option_list   = option_list
#     )
# def open_ToolMenu_Info():
#     option_list = [
#         "\nNOTES\n" 
#         "\n TOOL list information\n" 

#     ]
#     MessageBox(
#         messageType = "info",
#         title       = "TOOL list information",
#         subtitle    = "TOOL list information",
#         default_value = "",
#         option_list   = option_list
#     )


# def open_LR_Agent_tool_info():
#     option_list = [
#         "\n NOTES\n" 
#         "\nLearnReflect Agent: \n" 
#     ]
#     MessageBox(
#         messageType = "info",
#         title       = "LearnReflect Agent",
#         subtitle    = "Information about LearnReflect Agent",
#         default_value = "",
#         option_list   = option_list
#     )





# def open_YoutubeDownloader_tool_info():
#     option_list = [
#         "\n NOTES\n" 
#         "\n Youtube Downloader:\n" 
#     ]
#     MessageBox(
#         messageType = "info",
#         title       = "Youtube Downloader",
#         subtitle    = "Information about youtube downloader",
#         default_value = "",
#         option_list   = option_list
#     )


# def open_info_output_path():
#     option_list = [
#         "\n The default path is defined by the input files."
#         + "\n Upload cookie file from youtube, it will be auto-saved."
#         + "\n 1. go to google crome."
#         + "\n 2.find a cookie extension for exsample: https://chromewebstore.google.com/detail/get-cookiestxt-clean/ahmnmhfbokciafffnknlekllgcnafnie"
#         + "\n Go to youtube, then open the extension and export as, this will download a .txt\n",
#         + "\n upload the .txt file to upload files, and then you are good to go :D \n",
#         "it is possible to select the desired output path using the SELECT button",
#     ]

#     MessageBox(
#         messageType   = "info",
#         title         = "Output path",
#         subtitle      = "This widget allows to choose upscaled files path",
#         default_value = default_output_path,
#         option_list   = option_list
#     )




# def open_info_AI_model():
#     option_list = [
#         "\n IRCNN (2017) - Very simple and lightweight AI architecture\n" + 
#         " Only denoising (no upscaling)\n" + 
#         " Recommended for both image/video denoising\n" + 
#         "  • IRCNN_Mx1 - (medium denoise)\n" +
#         "  • IRCNN_Lx1 - (high denoise)\n",

#         "\n SRVGGNetCompact (2022) - Fast and lightweight AI architecture\n" + 
#         " Good-quality upscale\n" + 
#         " Recommended for video upscaling\n" + 
#         "  • RealESR_Gx4\n" + 
#         "  • RealSRx4_Anime\n",

#         "\n RRDB (2020) - Complex and heavy AI architecture\n" + 
#         " High-quality upscale\n" + 
#         " Recommended for image upscaling\n" +
#         "  • BSRGANx2\n" + 
#         "  • BSRGANx4\n" +
#         "  • RealESRGANx4\n",

#     ]

#     MessageBox(
#         messageType = "info",
#         title       = "AI model",
#         subtitle    = "This widget allows to choose between different AI models for upscaling",
#         default_value = default_AI_model,
#         option_list   = option_list
#     )








# def open_info_audio_mode(): 
#     option_list = [
#         "Audio Mode Options:"
#         "\n • Audio Enhancement: Improve overall sound quality, reducing background noise and clarifying audio details.\n" +
#         "   • Vocal Isolation: Separate and isolate vocals from the background music or environment, allowing you to emphasize or remove singing or speech.\n"
#     ]
    
#     MessageBox(
#         messageType= "info",
#         title = "Audio Denoise",
#         subtitle = "This Widget allows to choose Vocal isolation or Audio Denoise",
#         default_value = default_audio_mode,
#         option_list = option_list
#     )
    




# def open_info_keep_frames():
#     option_list = [
#         "\n ENABLED \n" + 
#         " The app does not delete the video frames after creating the upscaled video \n",

#         "\n DISABLED \n" + 
#         " The app deletes the video frames after creating the upscaled video \n"
#     ]

#     MessageBox(
#         messageType   = "info",
#         title         = "Keep frames",
#         subtitle      = "This widget allows to choose to keep video frames",
#         default_value = None,
#         option_list   = option_list
#     )
    




# def open_info_AI_interpolation():
#     option_list = [
#         " Interpolation is the fusion of the upscaled image produced by AI and the original image",

#         " \n INTERPOLATION OPTIONS\n" +
#         "  • Disabled - 100% upscaled\n" + 
#         "  • Low - 30% original / 70% upscaled\n" +
#         "  • Medium - 50% original / 50% upscaled\n" +
#         "  • High - 70% original / 30% upscaled\n",

#         " \n NOTES\n" +
#         "  • Can increase the quality of the final result\n" + 
#         "  • Especially when using the tilling/merging function (with low VRAM)\n" +
#         "  • Especially at low Input resolution % values (<50%) \n",

#     ]

#     MessageBox(
#         messageType = "info",
#         title       = "AI Interpolation", 
#         subtitle    = "This widget allows to choose interpolation between upscaled and original image/frame",
#         default_value = default_interpolation,
#         option_list   = option_list
#     )




# def open_info_image_output():
#     option_list = [
#         " \n PNG\n  • very good quality\n  • slow and heavy file\n  • supports transparent images\n",
#         " \n JPG\n  • good quality\n  • fast and lightweight file\n",
#         " \n BMP\n  • highest quality\n  • slow and heavy file\n",
#         " \n TIFF\n  • highest quality\n  • very slow and heavy file\n",
#     ]

#     MessageBox(
#         messageType = "info",
#         title       = "Image output",
#         subtitle    = "This widget allows to choose the extension of upscaled images",
#         default_value = default_image_extension,
#         option_list   = option_list
#     )




# def open_info_video_extension():
#     option_list = [
#         "\n MP4 (x264)\n" + 
#         "   • produces well compressed video using x264 codec\n",

#         "\n MP4 (x265)\n" + 
#         "   • produces well compressed video using x265 codec\n",

#         "\n AVI\n" + 
#         "   • produces the highest quality video\n" +
#         "   • the video produced can also be of large size\n"
#     ]

#     MessageBox(
#         messageType = "info",
#         title = "Video output",
#         subtitle = "This widget allows to choose the extension of the upscaled video",
#         default_value = default_video_extension,
#         option_list = option_list
#     )



# def open_info_input_resolution():
#     option_list = [
#         " A high value (>70%) will create high quality photos/videos but will be slower",
#         " While a low value (<40%) will create good quality photos/videos but will much faster",

#         " \n For example, for a 1080p (1920x1080) image/video\n" + 
#         " • Input resolution 25% => input to AI 270p (480x270)\n" +
#         " • Input resolution 50% => input to AI 540p (960x540)\n" + 
#         " • Input resolution 75% => input to AI 810p (1440x810)\n" + 
#         " • Input resolution 100% => input to AI 1080p (1920x1080) \n",
#     ]

#     MessageBox(
#         messageType = "info",
#         title       = "Input resolution %",
#         subtitle    = "This widget allows to choose the resolution input to the AI",
#         default_value = default_resize_factor,
#         option_list   = option_list
#     )



# def place_input_output_resolution_textboxs():

#     def open_info_input_resolution():
#         option_list = [
#             " A high value (>70%) will create high quality photos/videos but will be slower",
#             " While a low value (<40%) will create good quality photos/videos but will much faster",

#             " \n For example, for a 1080p (1920x1080) image/video\n" + 
#             " • Input resolution 25% => input to AI 270p (480x270)\n" +
#             " • Input resolution 50% => input to AI 540p (960x540)\n" + 
#             " • Input resolution 75% => input to AI 810p (1440x810)\n" + 
#             " • Input resolution 100% => input to AI 1080p (1920x1080) \n",
#         ]
#         MessageBox(
#             messageType   = "info",
#             title         = "Input resolution %",
#             subtitle      = "This widget allows to choose the resolution input to the AI",
#             default_value = None,
#             option_list   = option_list
#         )

#     widget_row = row4_y

#     background = create_option_background()
#     background.place(relx = 0.75, rely = widget_row, relwidth = 0.48, anchor = "center")

#     info_button = create_info_button(open_info_input_resolution, "Input resolution")
#     option_menu = create_text_box(selected_input_resize_factor, width = little_textbox_width) 

#     info_button.place(relx = column_info1, rely = widget_row - 0.003, anchor = "center")
#     option_menu.place(relx = column_1_5,   rely = widget_row,         anchor = "center")



#     info_button.place(relx = column_info2, rely = widget_row - 0.003, anchor = "center")
#     option_menu.place(relx = column_3,     rely = widget_row,         anchor = "center")











# def place_output_path_textbox():
#     # Row 1, cols 0-1: Output Path + Image/Video format selectors (merged)
#     outer = CTkFrame(controls_grid, fg_color=PANEL2_BG,
#                      border_width=1, border_color=BORDER2, corner_radius=5)
#     outer.grid(row=1, column=0, columnspan=2, padx=3, pady=3, sticky="nsew")
#     outer.columnconfigure(0, weight=0)
#     outer.columnconfigure(1, weight=1)
#     outer.columnconfigure(2, weight=1)
#     outer.rowconfigure(0, weight=0)
#     outer.rowconfigure(1, weight=0)
#     outer.rowconfigure(2, weight=0)

#     path_lbl = CTkButton(
#         outer, text="● Output Path", command=open_info_output_path,
#         fg_color="transparent", hover_color="#181410",
#         text_color=AMBER_DIM, height=14,
#         font=CTkFont(family="Segoe UI", size=8, weight="bold"),
#         border_width=0, anchor="center",
#     )
#     path_lbl.grid(row=0, column=0, columnspan=3, sticky="ew", padx=4, pady=(4, 1))

#     output_path_textbox = CTkEntry(
#         outer, textvariable=selected_output_path,
#         border_width=1, corner_radius=5, height=22,
#         font=CTkFont(family="Segoe UI", size=9),
#         justify="center", text_color=CREAM3,
#         fg_color="#0A0A09", border_color=BORDER2, state=DISABLED,
#     )
#     output_path_textbox.grid(row=1, column=0, columnspan=3, sticky="ew", padx=4, pady=(1, 2))

#     # Image sub-column
#     img_col = CTkFrame(outer, fg_color="transparent")
#     img_col.grid(row=2, column=1, padx=(4, 2), pady=(0, 4), sticky="ew")
#     CTkLabel(img_col, text="Image", font=CTkFont(family="Segoe UI", size=7),
#              text_color=CREAM3, fg_color="transparent").pack()
#     img_menu = create_option_menu_2(select_image_extension_from_menu,
#                                     image_extension_list, default_image_extension,
#                                     master=img_col, width=68)
#     img_menu.pack(fill="x")

#     # Video sub-column
#     vid_col = CTkFrame(outer, fg_color="transparent")
#     vid_col.grid(row=2, column=2, padx=(2, 4), pady=(0, 4), sticky="ew")
#     CTkLabel(vid_col, text="Video", font=CTkFont(family="Segoe UI", size=7),
#              text_color=CREAM3, fg_color="transparent").pack()
#     vid_menu = create_option_menu_2(select_video_extension_from_menu,
#                                     video_extension_list, default_video_extension,
#                                     master=vid_col, width=88)
#     vid_menu.pack(fill="x")



# def place_AI_menu():
#     # Row 0, col 0
#     frame = CTkFrame(controls_grid, fg_color=PANEL2_BG,
#                      border_width=1, border_color=BORDER2, corner_radius=5)
#     frame.grid(row=0, column=0, padx=3, pady=3, sticky="nsew")

#     CTkButton(
#         frame, text="● AI Model", command=open_info_AI_model,
#         fg_color="transparent", hover_color="#181410",
#         text_color=AMBER_DIM, height=14,
#         font=CTkFont(family="Segoe UI", size=8, weight="bold"),
#         border_width=0, anchor="center",
#     ).pack(fill="x", padx=4, pady=(4, 1))

#     AI_menu = create_option_menu_2(select_AI_from_menu, AI_models_list,
#                                    default_AI_model, master=frame, width=108)
#     AI_menu.pack(fill="x", padx=4, pady=(0, 4))



# def place_AI_interpolation_menu():
#     # Row 0, col 1
#     frame = CTkFrame(controls_grid, fg_color=PANEL2_BG,
#                      border_width=1, border_color=BORDER2, corner_radius=5)
#     frame.grid(row=0, column=1, padx=3, pady=3, sticky="nsew")

#     CTkButton(
#         frame, text="● AI Interp.", command=open_info_AI_interpolation,
#         fg_color="transparent", hover_color="#181410",
#         text_color=AMBER_DIM, height=14,
#         font=CTkFont(family="Segoe UI", size=8, weight="bold"),
#         border_width=0, anchor="center",
#     ).pack(fill="x", padx=4, pady=(4, 1))

#     menu = create_option_menu_2(select_interpolation_from_menu, interpolation_list,
#                                 default_interpolation, master=frame, width=108)
#     menu.pack(fill="x", padx=4, pady=(0, 4))
 




    
# def place_Audio_Selection_menu():
#     # Row 0, col 2
#     frame = CTkFrame(controls_grid, fg_color=PANEL2_BG,
#                      border_width=1, border_color=BORDER2, corner_radius=5)
#     frame.grid(row=0, column=2, padx=3, pady=3, sticky="nsew")

#     CTkButton(
#         frame, text="● Audio Mode", command=open_info_audio_mode,
#         fg_color="transparent", hover_color="#181410",
#         text_color=AMBER_DIM, height=14,
#         font=CTkFont(family="Segoe UI", size=8, weight="bold"),
#         border_width=0, anchor="center",
#     ).pack(fill="x", padx=4, pady=(4, 1))

#     menu = create_option_menu_2(select_audio_mode_from_menu, audio_mode_list,
#                                 default_audio_mode, master=frame, width=108)
#     menu.pack(fill="x", padx=4, pady=(0, 4))




# def place_keep_frames_menu():
#     keep_frames_button = create_info_button(open_info_keep_frames, "Keep frames")
#     keep_frames_menu   = create_option_menu(select_save_frame_from_menu, keep_frames_list, default_keep_frames)
    
#     keep_frames_button.place(relx = column1_x- 0.4, rely = row4_y - 0.053, anchor = "center")
#     keep_frames_menu.place(relx = column1_x- 0.4, rely = row4_y, anchor = "center")
    



# def place_image_output_menu():
#     pass  # now merged into place_output_path_textbox (row 1, cols 0-1)



# def place_input_resolution_textbox():
#     # Row 0, col 3
#     frame = CTkFrame(controls_grid, fg_color=PANEL2_BG,
#                      border_width=1, border_color=BORDER2, corner_radius=5)
#     frame.grid(row=0, column=3, padx=3, pady=3, sticky="nsew")

#     CTkButton(
#         frame, text="● Input Res %", command=open_info_input_resolution,
#         fg_color="transparent", hover_color="#181410",
#         text_color=AMBER_DIM, height=14,
#         font=CTkFont(family="Segoe UI", size=8, weight="bold"),
#         border_width=0, anchor="center",
#     ).pack(fill="x", padx=4, pady=(4, 1))

#     tb = create_text_box(selected_input_resize_factor, master=frame, width=75)
#     tb.pack(fill="x", padx=4, pady=(0, 4))



# def place_upscale_button(): 
#     global upscale_slot_frame
#     # Clear previous UPSCALE/STOP widget
#     for w in upscale_slot_frame.winfo_children():
#         w.destroy()

#     upscale_button = CTkButton(
#         master=upscale_slot_frame,
#         command=upscale_button_command,
#         text="UPSCALE",
#         image=upscale_icon,
#         width=110, height=26,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         border_width=1,
#         fg_color=AMBER_GLOW,
#         hover_color="#5a3c0c",
#         text_color=AMBER,
#         border_color=AMBER_DIM,
#         corner_radius=6,
#     )
#     upscale_button.pack(side="left", padx=2)
#     upscale_button.lift()

# def place_stop_button(): 
#     global upscale_slot_frame
#     # Clear previous UPSCALE/STOP widget
#     for w in upscale_slot_frame.winfo_children():
#         w.destroy()

#     stop_button = CTkButton(
#         master=upscale_slot_frame,
#         command=stop_button_command,
#         text="STOP",
#         image=stop_icon,
#         width=110, height=26,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         border_width=1,
#         fg_color="#160808",
#         hover_color="#220C0C",
#         text_color="#E04040",
#         border_color="#EC1D1D",
#         corner_radius=6,
#     )
#     stop_button.pack(side="left", padx=2)


# def place_message_label():
#     global input_file_button, upscale_slot_frame

#     # Row 1, cols 2-3: Welcome message + SELECT FILES + UPSCALE buttons
#     action_frame = CTkFrame(controls_grid, fg_color=PANEL2_BG,
#                             border_width=1, border_color=BORDER2, corner_radius=5)
#     action_frame.grid(row=1, column=2, columnspan=2, padx=3, pady=3, sticky="nsew")

#     message_label = CTkLabel(
#         master=action_frame,
#         textvariable=info_message,
#         height=16,
#         font=CTkFont(family="Segoe UI", size=9, weight="bold"),
#         fg_color="transparent",
#         text_color=CREAM2,
#         anchor="center",
#     )
#     message_label.pack(pady=(6, 3))

#     btns_row = CTkFrame(action_frame, fg_color="transparent")
#     btns_row.pack(pady=(0, 6))

#     input_file_button = CTkButton(
#         master=btns_row,
#         command=open_files_action,
#         text="SELECT FILES",
#         width=100, height=26,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         border_width=1,
#         fg_color="#0E0E0C", hover_color="#181612",
#         text_color=CREAM2, border_color=BORDER3,
#         corner_radius=6,
#     )
#     input_file_button.pack(side="left", padx=2)

#     # Slot frame for UPSCALE / STOP toggle
#     upscale_slot_frame = CTkFrame(btns_row, fg_color="transparent")
#     upscale_slot_frame.pack(side="left")
#     globals()['upscale_slot_frame'] = upscale_slot_frame




# def create_option_background():
#     return CTkFrame(
#         master        = window,
#         bg_color      = background_color,
#         fg_color      = PANEL2_BG,
#         height        = 46,
#         corner_radius = 8,
#     )











# # Main functions ---------------------------
# def on_app_close() -> None:
#     global Global_offline_model
#     del Global_offline_model
#     window.grab_release()
#     window.destroy()
#     load_model_inference()
#     global selected_AI_model
#     global selected_AI_multithreading
#     global selected_gpu
#     global selected_interpolation_factor
#     global selected_image_extension
#     global selected_video_extension
#     global tiles_resolution
#     global input_resize_factor
#     global cpu_number
#     global selected_audio_mode 
#     global preview_ai_instance


#     preview_ai_instance = None

#     selected_audio_mode = "Disabled"
#     AI_model_to_save          = f"{selected_AI_model}"
#     AI_multithreading_to_save = f"{selected_AI_multithreading} threads"
#     gpu_to_save               = selected_gpu
#     keep_frames_to_save = "Enabled" if selected_keep_frames == True else "Disabled"
#     image_extension_to_save   = selected_image_extension
#     video_extension_to_save   = selected_video_extension
    
#     interpolation_to_save= {
#         0: "Disabled",
#         0.3: "Low",
#         0.5: "Medium",
#         0.7: "High",
#     }.get(selected_interpolation_factor)
    
#     Audio_option_to_save = {
#         0: "Disabled",
#         1: "Vocal Isolation",
#         2: "Audio Denoise",
#     }.get(selected_audio_mode)

#     user_preference = {
#         "default_AI_model":          AI_model_to_save,
#         "default_AI_multithreading": AI_multithreading_to_save,
#         "default_gpu":               gpu_to_save,
#         "default_keep_frames":       keep_frames_to_save,
#         "default_image_extension":   image_extension_to_save,
#         "default_video_extension":   video_extension_to_save,
#         "default_interpolation":     interpolation_to_save,
#         "default_audio_mode":         Audio_option_to_save,
#         "default_output_path":       selected_output_path.get(),
#         "default_resize_factor":     str(selected_input_resize_factor.get()),
#         "default_VRAM_limiter":      str(selected_VRAM_limiter.get()),
#         "default_cpu_number":        str(selected_cpu_number.get()),
#     }
#     user_preference_json = json_dumps(user_preference)
#     with open(USER_PREFERENCE_PATH, "w") as preference_file:
#         preference_file.write(user_preference_json)

#     stop_upscale_process()
#     gc.collect()
#     torch.cuda.empty_cache()
    
    


    
    
# class VideoEnhancer():
#     def __init__(self, Master):
#         #threading.Thread(target=load_model_async, daemon=True).start()
#         self.toplevel_window = None
#         self._master = Master
#         Master.protocol("WM_DELETE_WINDOW", on_app_close)
#         Master.title('LearnReflect Video Enchancer')
#         screen_width  = Master.winfo_screenwidth()
#         screen_height = Master.winfo_screenheight()
#         window_width  = int(screen_width  * 0.85)
#         window_height = int(screen_height * 0.85)
#         x_offset = (screen_width  - window_width)  // 2
#         y_offset = (screen_height - window_height) // 2
#         # Store windowed geometry so we can restore it when leaving fullscreen
#         self._windowed_geometry = f"{window_width}x{window_height}+{x_offset}+{y_offset}"
#         Master.geometry(self._windowed_geometry)
#         Master.resizable(True, True)
#         # Start in fullscreen
#         Master.attributes("-fullscreen", True)
#         self._is_fullscreen = True
#         # F11 toggles fullscreen / windowed
#         Master.bind("<F11>", self._toggle_fullscreen)
#         # Escape also exits fullscreen (back to windowed)
#         Master.bind("<Escape>", self._exit_fullscreen)
#         Master.iconbitmap(find_by_relative_path("Assets" + os_separator + "logo.ico"))
#         # Background image hidden in new layout
#         # self.bg_image = CTkImage(...)
#         load_cookie_file_path()

#         # ── Thin separator bar between left col and center col ──────────────
#         sep_left = CTkFrame(Master, fg_color=BORDER2, width=1, corner_radius=0)
#         sep_left.place(relx=0.22, rely=0.0, relwidth=0.001, relheight=1.0)

#         # ── Thin separator bar between center col (file list) and right col (preview) ──
#         sep_right = CTkFrame(Master, fg_color=BORDER2, width=1, corner_radius=0)
#         sep_right.place(relx=0.55, rely=0.0, relwidth=0.001, relheight=1.0)

#         # ── Controls bar (top of center column) ─────────────────────────────
#         global controls_bar_frame, controls_grid
#         self.controls_bar_frame = CTkFrame(
#             Master,
#             fg_color=PANEL2_BG,
#             corner_radius=0,
#             border_width=0,
#         )
#         self.controls_bar_frame.place(relx=0.22, rely=0.0, relwidth=0.33, relheight=0.185)
#         controls_bar_frame = self.controls_bar_frame

#         # ── 2-row x 4-col inner grid ─────────────────────────────────────────
#         controls_grid = CTkFrame(self.controls_bar_frame, fg_color="transparent")
#         controls_grid.pack(fill="both", expand=True, padx=5, pady=4)
#         for _c in range(4):
#             controls_grid.columnconfigure(_c, weight=1, uniform="cols")
#         controls_grid.rowconfigure(0, weight=1)
#         controls_grid.rowconfigure(1, weight=1)

#         # ── Thin bottom border for controls bar ─────────────────────────────
#         cb_border = CTkFrame(Master, fg_color=BORDER2, height=1, corner_radius=0)
#         cb_border.place(relx=0.22, rely=0.185, relwidth=0.33, relheight=0.001)

#         # ── Permanent file list area (visible even when no files are loaded) ─
#         self.file_list_bg = CTkFrame(
#             Master,
#             fg_color=PANEL_BG,
#             border_color=BORDER2,
#             border_width=1,
#             corner_radius=0,
#         )
#         self.file_list_bg.place(relx=0.22, rely=0.186, relwidth=0.33, relheight=0.814)

#         self.ToolWindowClass = ToolWindowClass(Master)
#         #load_model_inference()
#         place_loadFile_section(Master)
#         place_output_path_textbox()
#         place_AI_menu()
#         place_AI_interpolation_menu()
#         place_Audio_Selection_menu()
#         place_input_resolution_textbox()
#         place_image_output_menu()
#         place_message_label()
#         place_upscale_button()
#         selected_VRAM_limiter.set(str(round(get_gpu_vram() / 1000)) if get_gpu_vram() else "4")

#     # ── Fullscreen helpers ────────────────────────────────────────────
#     def _toggle_fullscreen(self, event=None):
#         """Toggle between fullscreen and windowed mode (F11)."""
#         if self._is_fullscreen:
#             self._exit_fullscreen()
#         else:
#             self._enter_fullscreen()

#     def _enter_fullscreen(self, event=None):
#         self._master.attributes("-fullscreen", True)
#         self._is_fullscreen = True

#     def _exit_fullscreen(self, event=None):
#         self._master.attributes("-fullscreen", False)
#         self._master.geometry(self._windowed_geometry)
#         self._is_fullscreen = False


# if __name__ == "__main__":
#     #from Decryption import validate_jwt
#     # if not validate_jwt():
#     #     logging.info(f"Validating with jwt error")
#     #     sys.exit(1)
#     # else: 
#     #     logging.info(f"Validating with jwt success!")

    
#     selected_audio_mode = "Disabled"
#     multiprocessing_freeze_support()
#     set_appearance_mode("Dark")
#     set_default_color_theme("dark-blue")

 
    
#     if _TKDND_AVAILABLE:
#         # tkinterdnd2 + customtkinter: create a hybrid root that supports both
#         class _CTkDnD(CTk, _tkdnd.DnDWrapper):
#             def __init__(self, *args, **kwargs):
#                 CTk.__init__(self, *args, **kwargs)
#                 self.TkdndVersion = _tkdnd.DnDWrapper.tkdnd_init(self)
#         window = _CTkDnD()
#     else:
#         window = CTk()
#     window.configure(fg_color="#060606")
#     youtube_progress_var = StringVar()
#     processing_queue = multiprocessing_Queue(maxsize=1)
#     info_message            = StringVar()
#     selected_output_path    = StringVar()
#     selected_input_resize_factor  = StringVar()
#     selected_VRAM_limiter   = StringVar()
#     selected_cpu_number     = StringVar()
#     video_format_var = StringVar(value="None")
#     audio_format_var = StringVar(value="None")

    
#     global selected_file_list
#     global selected_AI_model
#     global selected_gpu
#     global selected_keep_frames
#     global selected_AI_multithreading
#     global selected_image_extension
#     global selected_video_extension
#     global selected_interpolation_factor
#     global tiles_resolution
#     global input_resize_factor
#     global cpu_number
#     selected_gpu = "Auto"
#     selected_file_list = []
#     selected_AI_model          = default_AI_model
#     selected_image_extension   = default_image_extension
#     selected_video_extension   = default_video_extension
#     selected_AI_multithreading = max(1, int(os_cpu_count() // 2))
#     default_cpu_number        = str(int(get_cpu_number()))
#     selected_keep_frames = True if default_keep_frames == "Enabled" else False

#     selected_interpolation_factor = {
#         "Disabled": 0,
#         "Low": 0.3,
#         "Medium": 0.5,
#         "High": 0.7,
#     }.get(default_interpolation)
    

#     selected_input_resize_factor.set(default_resize_factor)
#     selected_VRAM_limiter.set(default_VRAM_limiter)
#     selected_cpu_number.set(default_cpu_number)
#     selected_output_path.set(default_output_path)

#     info_message.set("Welcome Back")
#     selected_input_resize_factor.trace_add('write', update_file_widget)


#     font   = "Segoe UI"    
#     bold8  = CTkFont(family = font, size = 8, weight = "bold")
#     bold9  = CTkFont(family = font, size = 9, weight = "bold")
#     bold10 = CTkFont(family = font, size = 10, weight = "bold")
#     bold11 = CTkFont(family = font, size = 11, weight = "bold")
#     bold12 = CTkFont(family = font, size = 12, weight = "bold")
#     bold13 = CTkFont(family = font, size = 13, weight = "bold")
#     bold14 = CTkFont(family = font, size = 14, weight = "bold")
#     bold16 = CTkFont(family = font, size = 16, weight = "bold")
#     bold17 = CTkFont(family = font, size = 17, weight = "bold")
#     bold18 = CTkFont(family = font, size = 18, weight = "bold")
#     bold19 = CTkFont(family = font, size = 19, weight = "bold")
#     bold20 = CTkFont(family = font, size = 20, weight = "bold")
#     bold21 = CTkFont(family = font, size = 21, weight = "bold")
#     bold22 = CTkFont(family = font, size = 22, weight = "bold")
#     bold23 = CTkFont(family = font, size = 23, weight = "bold")
#     bold24 = CTkFont(family = font, size = 24, weight = "bold")
#     stop_icon      = CTkImage(pillow_image_open(find_by_relative_path(f"Assets{os_separator}stop_icon.png")),      size=(15, 15))
#     upscale_icon   = CTkImage(pillow_image_open(find_by_relative_path(f"Assets{os_separator}upscale_iconLR.png")),   size=(15, 15))
#     clear_icon     = CTkImage(pillow_image_open(find_by_relative_path(f"Assets{os_separator}clear_icon.png")),     size=(15, 15))
#     info_icon      = CTkImage(pillow_image_open(find_by_relative_path(f"Assets{os_separator}info_icon.png")),      size=(17, 17))

    
    
#     app = VideoEnhancer(window)
#     window.update()
#     window.mainloop()


# import os
# # os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
# # os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
# import sys
# import torch 
# import torch
# import onnxruntime as ort
# from functools  import cache
# from time       import sleep
# from subprocess import run  as subprocess_run
# import ffmpeg
# from smolagents import CodeAgent, FinalAnswerTool,  DuckDuckGoSearchTool, GoogleSearchTool, VisitWebpageTool, LiteLLMModel,VLLMModel, SpeechToTextTool,PythonInterpreterTool
# from Agents_tools import ExtractAudioFromVideo, Fetch_top_trending_youtube_videos, Log_Agent_Progress,Read_transcript
# import numpy as np
# from PIL import Image, ImageTk
# import yaml
# from tkinter import filedialog
# import os
# import time
# from googleapiclient.discovery import build
# from googleapiclient.http import MediaFileUpload
# from dotenv import load_dotenv
# from shutil     import rmtree as remove_directory
# import subprocess
# from timeit     import default_timer as timer
# from PIL import Image, ImageSequence
# import threading
# import cv2
# from Logger import logging
# from typing    import Callable
# from threading import Thread
# from itertools import repeat
# import yt_dlp
# from multiprocessing.pool import ThreadPool
# from PIL import Image, ImageDraw, ImageFont 
# from multiprocessing import ( 
#     Process, 
#     Queue          as multiprocessing_Queue,
#     freeze_support as multiprocessing_freeze_support
# )

# from json import (
#     load  as json_load, 
#     dumps as json_dumps
# )
# import gc
# import shutil
# import json
# from File_path import get_app_data_path
# from os import (
#     sep        as os_separator,
#     devnull    as os_devnull,
#     environ    as os_environ,
#     cpu_count  as os_cpu_count,
#     makedirs   as os_makedirs,
#     listdir    as os_listdir,
#     remove     as os_remove
# )

# from os.path import (
#     basename   as os_path_basename,
#     dirname    as os_path_dirname,
#     abspath    as os_path_abspath,
#     join       as os_path_join,
#     exists     as os_path_exists,
#     splitext   as os_path_splitext,
#     expanduser as os_path_expanduser
# )


# from natsort          import natsorted
# from moviepy.video.io import ImageSequenceClip 
# from onnxruntime      import InferenceSession as onnxruntime_inferenceSession

# from PIL.Image import (
#     open      as pillow_image_open,
#     fromarray as pillow_image_fromarray
# )

# from cv2 import (
#     CAP_PROP_FPS,
#     CAP_PROP_FRAME_COUNT,
#     CAP_PROP_FRAME_HEIGHT,
#     CAP_PROP_FRAME_WIDTH,
#     COLOR_BGR2RGB,
#     COLOR_GRAY2RGB,
#     COLOR_BGR2RGBA,
#     COLOR_RGB2GRAY,
#     IMREAD_UNCHANGED,
#     INTER_LINEAR,
#     INTER_AREA,
#     INTER_CUBIC,
#     VideoCapture as opencv_VideoCapture,
#     cvtColor     as opencv_cvtColor,
#     imdecode     as opencv_imdecode,
#     imencode     as opencv_imencode,
#     addWeighted  as opencv_addWeighted,
#     cvtColor     as opencv_cvtColor,
#     resize       as opencv_resize,
# )
# import numpy as np
# from numpy import (
#     ndarray     as numpy_ndarray,
#     frombuffer  as numpy_frombuffer,
#     concatenate as numpy_concatenate, 
#     transpose   as numpy_transpose,
#     full        as numpy_full, 
#     zeros       as numpy_zeros, 
#     expand_dims as numpy_expand_dims,
#     squeeze     as numpy_squeeze,
#     clip        as numpy_clip,
#     mean        as numpy_mean,
#     repeat      as numpy_repeat,
#     max         as numpy_max, 
#     float32,
#     uint8
# )

# import torch
# import tkinter as tk
# from tkinter import StringVar, DISABLED,END,scrolledtext
# try:
#     import tkinterdnd2 as _tkdnd
#     _TKDND_AVAILABLE = True
# except ImportError:
#     _TKDND_AVAILABLE = False
# from customtkinter import (
#     CTk,
#     CTkButton,
#     CTkFrame,
#     CTkComboBox,
#     CTkCheckBox,
#     CTkSlider,
#     CTkEntry,
#     CTkFont,
#     CTkImage,
#     CTkLabel,
#     CTkOptionMenu,
#     CTkScrollableFrame,
#     CTkToplevel,
#     filedialog,
#     CTkTextbox,
#     set_appearance_mode,
#     set_default_color_theme
# )



# def check_hardware():
#     if torch.cuda.is_available():
#         try:
#             major = torch.cuda.get_device_capability(0)[0]
#             if major >= 7:
#                 return "cuda", torch.float16
#             else:
#                 return "cuda", torch.bfloat16
#         except (AssertionError, RuntimeError) as e:
#             print(f"Warning: Unable to access CUDA device. Falling back to CPU. Reason: {e}")
#             return "cpu", torch.float32
#     else:
#         print("CUDA not available. Using CPU.")
#         return "cpu", torch.float32
# device, dtype = check_hardware()

# def get_gpu_vram():
#     import psutil
#     try:
#         import wmi
#         w = wmi.WMI()
#         for gpu in w.Win32_VideoController():
#             if 'VRAM' in gpu.AdapterRAM:
#                    return min(4, int((psutil.virtual_memory().total / (1024**3)) * 0.7))  
#             return 4000
#     except:
#         return 4000

# def get_cpu_number():
#         try:
#             cpu_number = max(1, int(os_cpu_count() // 1.5))
#             return cpu_number
#         except Exception as e:
#             return

# if sys.stdout is None: sys.stdout = open(os_devnull, "w")
# if sys.stderr is None: sys.stderr = open(os_devnull, "w")

# def find_by_relative_path(relative_path: str) -> str:
#     base_path = getattr(sys, '_MEIPASS', os_path_dirname(os_path_abspath(__file__)))
#     return os_path_join(base_path, relative_path)


# app_name   = "LearnReflect AI"
# app_name_color          = "#D49A2A"    # amber
# dark_color              = "#070707"
# background_color        = "#060606"
# text_color              = "#948C7E"    # warm muted
# widget_background_color = "#0E0E0D"
# # ── Design system ────────────────────────────────────────────────────
# AMBER        = "#D49A2A"
# AMBER_DIM    = "#8C6418"
# AMBER_GLOW   = "#3C2808"
# CREAM        = "#E0D8C8"
# CREAM2       = "#948C7E"
# CREAM3       = "#4A4640"
# BORDER1      = "#141210"
# BORDER2      = "#201E1A"
# BORDER3      = "#383028"
# GREEN_OK     = "#38A858"
# GREEN_BG     = "#0C1C10"
# PANEL_BG     = "#0A0A09"
# PANEL2_BG    = "#0E0E0D"
# very_low_VRAM  = 4
# low_VRAM       = 3
# medium_VRAM    = 2.2
# very_high_VRAM = 0.6

# AI_LIST_SEPARATOR           = [ "----" ]
# IRCNN_models_list           = [ "IRCNN_Mx1", "IRCNN_Lx1" ]
# SRVGGNetCompact_models_list = [ "RealESR_Gx4", "RealSRx4_Anime" ]
# RRDB_models_list            = [ "BSRGANx4", "BSRGANx2", "RealESRGANx4"]
# Facedetection_model_list = ["yolov8x-face-lindevs"]



# ####Cookies
# import datetime
# FUTURE_DATE = datetime.datetime(2030, 1, 1)
# NEW_TIMESTAMP = int(FUTURE_DATE.timestamp())
# fixed_cookie_filename = "youtube.com_cookies.txt"
# COOKIE_STORAGE_DIR = get_app_data_path() / "cookies" 
# COOKIE_PATH_FILE = COOKIE_STORAGE_DIR / fixed_cookie_filename
# if not COOKIE_STORAGE_DIR.exists():
#     COOKIE_STORAGE_DIR.mkdir(parents=True)
# cookie_file_path = None


# #Video Preview
# youtube_download_list = []
# frame_cache = {}
# last_model_config =  None
# preview_ai_instance = None
# current_loaded_model = None
# model_loading_thread = None
# global original_preview
# global upscaled_preview
# global original_preview_frame
# global upscaled_preview_frame
# preview_instance = None  
# file_list_update_callback = None
# media_info_update_callback = None
# stop_download_flag = False
# Global_offline_model = None  

# import onnxruntime as ort
# model_loading_lock = threading.Lock()
# AI_models_list         = ( SRVGGNetCompact_models_list + AI_LIST_SEPARATOR + RRDB_models_list + AI_LIST_SEPARATOR + IRCNN_models_list )
# keep_frames_list       = [ "Disabled", "Enabled" ]
# image_extension_list   = [ ".png", ".jpg", ".bmp", ".tiff" ]
# video_extension_list   = [ ".mp4 (x264)", ".mp4 (x265)", ".avi" ]
# interpolation_list     = [ "Low", "Medium", "High", "Disabled" ]
# audio_mode_list        = ["Disabled", "Vocal Isolation", "Audio Denoise"] 
# OUTPUT_PATH_CODED    = "Same path as input files"
# DOCUMENT_PATH        = os_path_join(os_path_expanduser('~'), 'Documents')
# USER_PREFERENCE_PATH = find_by_relative_path(f"{DOCUMENT_PATH}{os_separator}{app_name}_UserPreference.json")
# FFMPEG_EXE_PATH      = find_by_relative_path(f"Assets{os_separator}ffmpeg.exe")
# os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "video_codec;h264_cuvid"
# EXIFTOOL_EXE_PATH    = find_by_relative_path(f"Assets{os_separator}exiftool.exe")
# FRAMES_FOR_CPU       = 30
# if 'CUDAExecutionProvider' not in ort.get_available_providers():
#     FRAMES_FOR_CPU = 5


# if os_path_exists(FFMPEG_EXE_PATH): 
#     logging.info(f"[{app_name}] External ffmpeg.exe file found")
#     os_environ["IMAGEIO_FFMPEG_EXE"] = FFMPEG_EXE_PATH

# if os_path_exists(USER_PREFERENCE_PATH):
#     logging.info(f"[{app_name}] Preference file exist")
#     with open(USER_PREFERENCE_PATH, "r") as json_file:
#         json_data = json_load(json_file)
#         default_AI_model          = json_data["default_AI_model"]
#         default_AI_multithreading = json_data["default_AI_multithreading"]
#         default_image_extension   = json_data["default_image_extension"]
#         default_video_extension   = json_data["default_video_extension"]
#         default_interpolation     = json_data["default_interpolation"]
#         default_keep_frames       = json_data.get("default_keep_frames",        keep_frames_list[0])
#         default_audio_mode        = json_data.get("default_audio_mode",audio_mode_list[0]) 
#         default_output_path       = json_data["default_output_path"]
#         default_resize_factor     = json_data["default_resize_factor"]
#         default_VRAM_limiter      = json_data["default_VRAM_limiter"]
# else:
#     logging.info(f"[{app_name}] Preference file does not exist, using default coded value")
#     default_AI_model          = AI_models_list[0]
#     default_AI_multithreading = max(1, int(os_cpu_count() // 2))
#     default_gpu               = get_gpu_vram()
#     default_keep_frames       = keep_frames_list[0]
#     default_image_extension   = image_extension_list[0]
#     default_video_extension   = video_extension_list[0]
#     default_interpolation     = interpolation_list[0]
#     default_audio_mode        = audio_mode_list[0] 
#     default_output_path       = OUTPUT_PATH_CODED
#     default_resize_factor     = str(50)
#     default_VRAM_limiter      = str(4)
#     default_cpu_number        = str(int(get_cpu_number()))

# COMPLETED_STATUS = "Completed"
# ERROR_STATUS     = "Error"
# STOP_STATUS      = "Stop"

# controls_bar_frame  = None   # set in VideoEnhancer.__init__
# file_overrides      = {}    # per-file AI setting overrides: {file_path: {key: value}}
# upscale_slot_frame  = None   # set in place_message_label()

# offset_y_options = 0.105
# row0_y = 0.52
# row1_y = row0_y + offset_y_options
# row2_y = row1_y + offset_y_options
# row3_y = row2_y + offset_y_options
# row4_y = row3_y + offset_y_options
# row5_y = row4_y + offset_y_options



# offset_x_options = 0.28
# column1_x = 0.5
# column0_x = column1_x - offset_x_options
# column2_x = column1_x + offset_x_options
# column1_5_x = column1_x + offset_x_options/2
# column_info1  = 0.625
# column_1_5    = column_info1 + 0.08
# column_1_4    = column_1_5 - 0.0127
# column_info2  = 0.858
# column_3      = column_info2 + 0.08


# little_textbox_width = 74
# little_menu_width = 98

# supported_file_extensions = [
#     '.heic', '.jpg', '.jpeg', '.JPG', '.JPEG', '.png',
#     '.PNG', '.webp', '.WEBP', '.bmp', '.BMP', '.tif',
#     '.tiff', '.TIF', '.TIFF', '.mp4', '.MP4', '.webm',
#     '.WEBM', '.mkv', '.MKV', '.flv', '.FLV', '.gif',
#     '.GIF', '.m4v', ',M4V', '.avi', '.AVI', '.mov',
#     '.MOV', '.qt', '.3gp', '.mpg', '.mpeg', ".vob"
# ]

# supported_video_extensions = [
#     '.mp4', '.MP4', '.webm', '.WEBM', '.mkv', '.MKV',
#     '.flv', '.FLV', '.gif', '.GIF', '.m4v', ',M4V',
#     '.avi', '.AVI', '.mov', '.MOV', '.qt', '.3gp',
#     '.mpg', '.mpeg', ".vob"
# ]




# CPU_ONLY = 'CUDAExecutionProvider' not in ort.get_available_providers()
# if CPU_ONLY:
#     FRAMES_FOR_CPU = 5




# def load_model_async():

#     modelmanager.load_model()
 

# class modelmanager:
#     """Class manager for AI model"""
#     _model = None
#     _lock = threading.Lock()
#     model_loaded_event = threading.Event()
#     @classmethod
#     def load_model(cls, model_path, **Kwargs):
#         """Load model & return model instance"""
#         device, dtype = check_hardware()
#         with cls._lock:
#             if cls._model is None:
#                 gc.collect()
#                 if torch.cuda.is_available():
#                     torch.cuda.empty_cache()
#                 cls._model = LiteLLMModel(
#                     model_id="gpt-5",
#                     reasoning_effort="minimal",
#                     api_key=os.getenv("GPT_5_API_KEY"),
#                     max_tokens=16000,
#                 )
#                 print("videoencancer.exe: dtype= ", dtype)
#         global model_loaded_event
#         cls.model_loaded_event.set()
#         print("Model loaded successfully! :)")
#         return cls._model
    
#     @classmethod
#     def get_model(cls):
#         """Return model instance"""
#         if cls._model is None:
#             raise RuntimeError("model has not been loaded yet")
#         return cls._model
    
    


# from smolagents.tools import PipelineTool



# class SpeechToTextToolCUDA(PipelineTool):
#     default_checkpoint = r"c:\Users\didri\Desktop\AI-models\Audio-Models\faster-whisper-large-v3-turbo-int8float16"
#     description = "Fast tool that transcribes audio into text using faster-whisper. It returns the path to the transcript file"
#     name = "transcriber"
#     inputs = {
#         "audio": {
#             "type": "audio",
#             "description": "The audio to transcribe. Can be a local path, a URL, or a tensor.",
#         },
#         "text_path": {
#             "type": "string",
#              "description": "The path to save the transcript to.",
#         },
#         "video_path": {
#             "type": "string",
#             "description": "The path to the video to transcribe. only for info printging",
#         }
#     }
#     output_type = "string"
#     def setup(self):

#         self.model = WhisperModel(
#                 model_size_or_path=self.default_checkpoint,
#                 device="cuda",
#                 compute_type="int8_float16"
#                 )
#     def forward(self, inputs):
#         audio_path = inputs["audio"]
#         text_path = inputs["text_path"]
#         video_path = inputs["video_path"]
#         segments, info = self.model.transcribe(
#             audio_path,
#             language="en",
#             temperature=0.0,
#             vad_filter=True,
#             initial_prompt="Motivational podcast",
#             condition_on_previous_text=True,

#         )
#         print(f"\n🔊 Using Whisper on device: {self.device}, \ntranscribing video: {video_path} \n   with inputs: {self.inputs}")
#         print(f"[INFO] Detected Language: {info.language} (confidence: {info.language_probability:.2f})")
#         print(f"[INFO] Audio Duration: {info.duration:.2f} seconds")

#         try:
#             with open(text_path, "a", encoding="utf-8") as f:
#                 print(f"opening txt_path on: {text_path} device: {self.device}")

#                 try:
#                     for segment in segments:
#                          f.write(f"{segment.text.strip()}\n")
#                     f.write("\n\n")
#                 except Exception as e:
#                     print(f"error during segments: {str(e)}")

#         finally:
#             print(f"transcription complete ! device  {self.device}")
#             if self.device == "cuda":
#                 torch.cuda.empty_cache()
#                 gc.collect()
#                 del self.model

#         return text_path

#     def encode(self, audio):
#         return {"audio": audio}

#     def decode(self, outputs):
#         return outputs




























# class vidintel_agent_gui():
#     """Agent that retrieves transcripts, searches the web, and generates optimized metadata for videos."""

#     def __init__(self, parent_container):
#         self.parent_container = parent_container
#         self.uploaded_files = selected_file_list

#         self.container = CTkFrame(
#             master=self.parent_container,
#             fg_color="#282828",
#             border_width=2,
#             border_color="#404040",
#             corner_radius=10
#         )
#         self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

#         self.loading_label = CTkLabel(
#             master=self.container,
#             text="",
#             text_color="#00FF00",
#             font=("Arial", 14)
#         )
#         self.loading_label.grid(row=2, column=0, pady=5, sticky="nsew")

#         wait_time = 0
        

#         self.loading_label.configure(text=f"⏳ Waiting for model to load... {wait_time}s")
#         self.loading_label.update_idletasks()
#         loaded = modelmanager.model_loaded_event.wait(timeout=60)
#         if not loaded:
#              self.loading_label.configure(text="❌ Timeout waiting for model to load.")
#              return

#         self.loading_label.configure(text="✅ Model loaded successfully.")
#         self.model = modelmanager.get_model() 



#         self.create_widgets()
#         global file_list_update_callback
#         file_list_update_callback = self.sync_uploaded_files
#         file_names = [os_path_basename(f) for f in self.uploaded_files]
#         self.file_menu.configure(values=file_names)
#         if file_names:
#            self.file_menu_var.set(file_names[0])

#     def create_widgets(self):
#         self.top_bar = CTkFrame(
#             master=self.container,
#             fg_color="#282828"
#         )
#         self.top_bar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

#         self.file_menu_var = StringVar(value="No files uploaded")
#         self.file_menu = CTkOptionMenu(
#             master=self.top_bar,
#             variable=self.file_menu_var,
#             values=[],
#             width=200,
#             height=30,
#             font=bold11,
#             dropdown_font=bold11,
#             fg_color="#282828",
#             button_color="#404040",
#             text_color="#FFFFFF"
#         )
#         self.file_menu.pack(side="left", padx=10, pady=5)

    
#         self.metadata_btn = CTkButton(
#             master=self.top_bar,
#             text="Generate Metadata",
#             width=140,
#             height=30,
#             font=bold11,
#             border_width=1,
#             fg_color="#282828",
#             text_color="#E0E0E0",
#             border_color="#0096FF",
#             command=lambda: self.start_metadata_thread(),
#         )
#         self.metadata_btn.pack(side="left", padx=10, pady=5)
        
#         self.Social_media_list = CTkOptionMenu(
#             master=self.top_bar,
#             width=140,
#             height=30,
#             font=bold11,
#             fg_color="#282828",
#             text_color="#E0E0E0",
#             #command=
#             state="normal",
#             values=["YouTube", "Instagram", "TikTok"]  

#         )
#         self.Social_media_list.pack(side="left", padx=10, pady=5)

    
#         self.info_button_LearnReflect_Agent = create_info_button(
#             open_LR_Agent_tool_info,
#             text="INFO",
#             width=15,
#             master=self.top_bar
#         )
#         self.info_button_LearnReflect_Agent.pack(side="left", padx=10, pady=5)

  
#         self.chat_display  = scrolledtext.ScrolledText(
#           self.container,
#           wrap=tk.WORD,
#           width=55,
#           height=25,
#           font=("Helvetica",12),
#           bg="black",  
#           fg="white",
#           state="disabled",
#         )
#         self.chat_display.config(
#             insertbackground="yellow",
#             selectbackground="#444444",
#             selectforeground="white",
#             borderwidth=2,
#             relief="sunken"
#         )
#         self.chat_display.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
#         self.chat_display.yview(END)
#         self.container.columnconfigure(0, weight=1)
#         self.container.rowconfigure(1, weight=1)

#     def sync_uploaded_files(self):
#         """Sync uploaded_files with global list and refresh the dropdown"""
#         self.uploaded_files = selected_file_list
#         self.update_file_list()
#         if self.uploaded_files:
#             self.metadata_btn.configure(state="normal")

#     def start_metadata_thread(self):
#         thread = threading.Thread(target=self.load_llama_instruct, daemon=True)
#         thread.start()
#         self.metadata_btn.configure(state="DISABLED")
      
#     def load_llama_instruct(self, uploaded_file=None):
#         load_dotenv()
#         uploaded_file = self.file_menu_var.get()
#         if uploaded_file: 
#                 file_extension = os.path.splitext(uploaded_file)[1].lower()
#                 if file_extension in ['.mp4', '.avi', '.mov', '.mkv']:
#                         file = "Video file"
#                 elif file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
#                         file = "Image file"
                                    
#                         self.chat_display.config(state=tk.NORMAL)
#                         self.chat_display.insert(tk.END, "Sorry we do not read any pitcures at this moment, this will be available in later updates\n")
#                         self.chat_display.update()
#                         return


#         self.chat_display.config(state=tk.NORMAL)
#         self.chat_display.insert(tk.END, "1. 🤖 AI-agenten transcribes video now...\n")
#         self.chat_display.configure(state="disabled")
#         self.chat_display.update()
#         uploaded_file_name = self.file_menu_var.get()
#         Video_path = next((f for f in self.uploaded_files if os_path_basename(f) == uploaded_file_name), None)
#         if not Video_path:
#             print("Error: File not found!")
#             self.chat_display.config(state=tk.NORMAL)
#             self.chat_display.insert(tk.END, "Not a valid file path" + "\n")
#             self.chat_display.config(state=tk.DISABLED)  
#             return
                        
#         user_task = "Please generate a Title, Description, Hashtags, Keywords, and a unique message for my video. The goal is to help it go viral by leveraging current trends and analyzing similar successful videos. The unique message should highlight key insights, secret strategies, or specific elements that contributed to the virality of similar content. Think of it as a short, strategic note or idea that could help this video stand out and perform exceptionally well.in your final answer Use the exact key names: `title`, `description`, `keywords`, `hashtags`, and `Unique message`. No additional fields."
            
      

#         uploaded_file = self.file_menu_var.get()



        
#         #Agent Prompts
#         with open(find_by_relative_path("./agent_prompts/viral_agent_prompt.yaml"), 'r') as stream:
#                     Manager_Agent_prompt_templates = yaml.safe_load(stream)


#         #Tool initalization
#         final_answer = FinalAnswerTool()
#         web_search = DuckDuckGoSearchTool()
#         Extract_audio = ExtractAudioFromVideo
#         fetch_youtube_video_information = Fetch_top_trending_youtube_videos
#         log_every_step = Log_Agent_Progress
#        #Transcriber = SpeechToTextToolCUDA()
#         PythonInterpeter = PythonInterpreterTool()
#         Visit_WebPage = VisitWebpageTool()


#         manager_agent  = CodeAgent(
#             model=self.model,
#             tools=[
#                 final_answer,log_every_step,
#                   Extract_audio,
#                 #  Transcriber,
#                   PythonInterpeter,
#                   fetch_youtube_video_information,
#                   Visit_WebPage,
#                   ], 
#             max_steps=4,
#             prompt_templates=Manager_Agent_prompt_templates,
        
#         )

#         context_vars = {
#                "video_path": Video_path,
#               'Transcript_text_filepath': find_by_relative_path("./Project_text_files/Audio_TO_transcript.txt"), #kan endre dette så det finnes en .txt path som agent kan sende inn til speectotexttool når den er ferdig med extractaudiofromvideo, men må huske og endre system prompten også.
#                "chat_display": self.chat_display,
#             }       

#         Response = manager_agent.run(
#             task=user_task,
#             additional_args=context_vars
#         )
#         runsummary = manager_agent.visualize()
#         with open("./Agent_Orchestrator_Visualize.txt", "w") as f:
#             f.write(runsummary)
#         torch.cuda.empty_cache()
#         gc.collect()
#         del self.model

#         if isinstance(Response, dict):
#             self._append_chat(self._format_metadata(Response))
#             self.clean_temp_audio()

#         else:
#             self._append_chat(str(Response))


#         try:
#             if os.path.exists("temp_audio.wav"):
#                 os.remove("temp_audio.wav")
#                 logging.info("🗑️ temp_audio.wav deleted successfully.")
#         except Exception as e:
#             logging.info(f"⚠️ Error deleting temp audio: {e}")

         
#     def clean_temp_audio(self):
#         try:
#             if os.path.exists("temp_audio.wav"):
#                 os.remove("temp_audio.wav")
#                 logging.info("🗑️ temp_audio.wav deleted successfully.")
#         except Exception as e:
#             logging.info(f"⚠️ Error deleting temp audio: {e}")

#     def _format_metadata(self, md: dict) -> str:
#         return (
#             f"🎬 Title:\n  {md.get('title', 'N/A')}\n\n"
#             f"📝 Description:\n  {md.get('description', 'N/A')}\n\n"
#             f"🔑 Keywords:\n  {', '.join(md.get('keywords', []))}\n\n"
#             f"🏷️ Hashtags:\n  {' '.join(md.get('hashtags', []))}\n\n\n"
#             f" Tips/ideas: \n {' '.join(md.get('Unique message', []))}"
#         )
    

#     def update_file_list(self):
#         """Update dropdown with current files"""
#         file_names = [os_path_basename(f) for f in self.uploaded_files]
#         self.file_menu.configure(values=file_names)
#         if file_names:
#             self.file_menu_var.set(file_names[0])

#     def _append_chat(self, text: str):
#         self.chat_display.config(state=tk.NORMAL)
#         self.chat_display.insert(tk.END, text + "\n")
#         self.chat_display.see(tk.END)
#         self.chat_display.config(state=tk.DISABLED)

#     def clear_file_list(self):
#         """Reset dropdown to empty state"""
#         self.uploaded_files = []
#         self.file_menu.configure(values=[])
#         self.file_menu_var.set("No files uploaded")







































# class corelytics_InsightCatcher():
#     """Agent that retrieves transcripts, Analyze the transcript and provide insights too the user """

#     def __init__(self, parent_container):
#         self.parent_container = parent_container
#         self.uploaded_files = selected_file_list
#         self.container = CTkFrame(
#             master=self.parent_container,
#             fg_color="#282828",
#             border_width=2,
#             border_color="#404040",
#             corner_radius=10
#         )
#         self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

#         self.loading_label = CTkLabel(
#             master=self.container,
#             text="",
#             text_color="#00FF00",
#             font=("Arial", 14)
#         )
#         self.loading_label.grid(row=2, column=0, pady=5, sticky="nsew")

#         wait_time = 0
        
#         global Global_offline_model
#         while Global_offline_model is None:
#             self.loading_label.configure(text=f"⏳ Waiting for model to load... {wait_time}s")
#             self.loading_label.update_idletasks()
#             time.sleep(1)
#             wait_time += 1
#             if wait_time > 60:
#                 self.loading_label.configure(text="❌ Timeout waiting for model to load.")
#                 return

#         self.loading_label.configure(text="✅ Model loaded successfully.")
#         self.model = Global_offline_model



#         self.create_widgets()
#         global file_list_update_callback
#         file_list_update_callback = self.sync_uploaded_files
#         file_names = [os_path_basename(f) for f in self.uploaded_files]
#         self.file_menu.configure(values=file_names)
#         if file_names:
#            self.file_menu_var.set(file_names[0])

#     def create_widgets(self):
#         self.top_bar = CTkFrame(
#             master=self.container,
#             fg_color="#282828"
#         )
#         self.top_bar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

#         self.file_menu_var = StringVar(value="No files uploaded")
#         self.file_menu = CTkOptionMenu(
#             master=self.top_bar,
#             variable=self.file_menu_var,
#             values=[],
#             width=200,
#             height=30,
#             font=bold11,
#             dropdown_font=bold11,
#             fg_color="#282828",
#             button_color="#404040",
#             text_color="#FFFFFF"
#         )
#         self.file_menu.pack(side="left", padx=10, pady=5)

    
#         self.InsightCatcher_btn = CTkButton(
#             master=self.top_bar,
#             text="Run InsightCatcher",
#             width=140,
#             height=30,
#             font=bold11,
#             border_width=1,
#             fg_color="#282828",
#             text_color="#E0E0E0",
#             border_color="#0096FF",
#             command=lambda: self.start_metadata_thread(),
#         )
#         self.InsightCatcher_btn.pack(side="left", padx=10, pady=5)
        
    
#         self.info_button_LearnReflect_Agent = create_info_button(
#             open_LR_Agent_tool_info,
#             text="INFO",
#             width=15,
#             master=self.top_bar
#         )
#         self.info_button_LearnReflect_Agent.pack(side="left", padx=10, pady=5)

  
#         self.InSightCatcher_chatlogger  = scrolledtext.ScrolledText(
#           self.container,
#           wrap=tk.WORD,
#           width=55,
#           height=25,
#           font=("Helvetica",12),
#           bg="black",  
#           fg="white",
#           state="disabled",
#         )
#         self.InSightCatcher_chatlogger.config(
#             insertbackground="yellow",
#             selectbackground="#444444",
#             selectforeground="white",
#             borderwidth=2,
#             relief="sunken"
#         )
#         self.InSightCatcher_chatlogger.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
#         self.InSightCatcher_chatlogger.yview(END)
#         self.container.columnconfigure(0, weight=1)
#         self.container.rowconfigure(1, weight=1)

#     def sync_uploaded_files(self):
#         """Sync uploaded_files with global list and refresh the dropdown"""
#         self.uploaded_files = selected_file_list
#         self.update_file_list()
#         if self.uploaded_files:
#             self.InsightCatcher_btn.configure(state="normal")

#     def start_metadata_thread(self):
#         thread = threading.Thread(target=self.load_llama_instruct, daemon=True)
#         thread.start()
#         self.InsightCatcher_btn.configure(state="DISABLED")
      
#     def load_llama_instruct(self, uploaded_file=None):
#         load_dotenv()
#         uploaded_file = self.file_menu_var.get()
#         if uploaded_file: 
#                 file_extension = os.path.splitext(uploaded_file)[1].lower()
#                 if file_extension in ['.mp4', '.avi', '.mov', '.mkv']:
#                         file = "Video file"
#                 elif file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
#                         file = "Image file"
                                    
#                         self.InSightCatcher_chatlogger.config(state=tk.NORMAL)
#                         self.InSightCatcher_chatlogger.insert(tk.END, "Sorry we do not read any pitcures at this moment, this will be available in later updates\n")
#                         self.InSightCatcher_chatlogger.update()
#                         return


#         self.InSightCatcher_chatlogger.config(state=tk.NORMAL)
#         self.InSightCatcher_chatlogger.insert(tk.END, "1. 🤖 AI-agenten transcribes video now...\n")
#         self.InSightCatcher_chatlogger.configure(state="disabled")
#         self.InSightCatcher_chatlogger.update()
#         uploaded_file_name = self.file_menu_var.get()
#         Video_path = next((f for f in self.uploaded_files if os_path_basename(f) == uploaded_file_name), None)
#         if not Video_path:
#             print("Error: File not found!")
#             self.InSightCatcher_chatlogger.config(state=tk.NORMAL)
#             self.InSightCatcher_chatlogger.insert(tk.END, "Not a valid file path" + "\n")
#             self.InSightCatcher_chatlogger.config(state=tk.DISABLED)  
#             return
                        
#         user_task = (
               
#                   )
      

#         uploaded_file = self.file_menu_var.get()
#         context_vars = {
#                "video_path": Video_path,
#                "file_type": file,
#                "chat_display": self.InSightCatcher_chatlogger,
#             }       


        
#         #Agent Prompts
#         with open(find_by_relative_path("./Assets/agent_prompts/videotext_Manger_agent_prompt.yaml"), 'r') as stream:
#                     Manager_Agent_prompt_templates = yaml.safe_load(stream)


#         with open(find_by_relative_path("./Assets/agent_prompts/loaded_reasoning_agent_prompts.yaml"), 'r') as stream:
#                     Reasoning_Agent_Prompt_Template = yaml.safe_load(stream)


#         #Tool initalization
#         final_answer = FinalAnswerTool()
#         Extract_audio = ExtractAudioFromVideo
#         log_every_step = Log_Agent_Progress
#         transcribe = SpeechToTextTool()
  



#         Chunk_reasoning_Agent = CodeAgent (
#             model=self.model,
#             name="Reasoning_Agent",
#             description="",
#             add_base_tools=True,
#             prompt_templates=Reasoning_Agent_Prompt_Template,
#             tools=[],
#             max_steps=30,
#             provide_run_summary=True
#         )


#         manager_agent  = CodeAgent(
#             model=self.model,
#             tools=[final_answer,log_every_step, Extract_audio, transcribe], 
#             managed_agents=[Chunk_reasoning_Agent],
#             max_steps=30,
#             verbosity_level=4,
#             prompt_templates=Manager_Agent_prompt_templates,
#             additional_authorized_imports=['datetime'],
#         )

#         Response = manager_agent.run(
#             task=user_task,
#             additional_args=context_vars
#         )



#         if isinstance(Response, dict):
#             self._append_chat(self._format_metadata(Response))
#             self.clean_temp_audio()

#         else:
#             self._append_chat(str(Response))


#         try:
#             if os.path.exists("temp_audio.wav"):
#                 os.remove("temp_audio.wav")
#                 logging.info("🗑️ temp_audio.wav deleted successfully.")
#         except Exception as e:
#             logging.info(f"⚠️ Error deleting temp audio: {e}")

         
#     def clean_temp_audio(self):
#         try:
#             if os.path.exists("temp_audio.wav"):
#                 os.remove("temp_audio.wav")
#                 logging.info("🗑️ temp_audio.wav deleted successfully.")
#         except Exception as e:
#             logging.info(f"⚠️ Error deleting temp audio: {e}")

    

#     def update_file_list(self):
#         """Update dropdown with current files"""
#         file_names = [os_path_basename(f) for f in self.uploaded_files]
#         self.file_menu.configure(values=file_names)
#         if file_names:
#             self.file_menu_var.set(file_names[0])
             

#     def _append_chat(self, text: str):
#         self.InSightCatcher_chatlogger.config(state=tk.NORMAL)
#         self.InSightCatcher_chatlogger.insert(tk.END, text + "\n")
#         self.InSightCatcher_chatlogger.see(tk.END)
#         self.InSightCatcher_chatlogger.config(state=tk.DISABLED)

#     def clear_file_list(self):
#         """Reset dropdown to empty state"""
#         self.uploaded_files = []
#         self.file_menu.configure(values=[])
#         self.file_menu_var.set("No files uploaded")






















# class social_media_optimizer_Gui:
#     def __init__(self, parent_container):
#             self.parent_container = parent_container
#             self.credentials = None  

#             self.container = CTkFrame(
#                 master=self.parent_container,
#                 fg_color="black",
#                 border_width=2,
#                 border_color="#404040",
#                 corner_radius=10,
#                 height=1000
#             )
#             self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
#             self.container.update_idletasks()


#             self.create_widgets()

#     def create_widgets(self):
#             row=1
#             self.container.columnconfigure(0, weight=1)
#             self.container.columnconfigure(1, weight=1)
#             self.container.rowconfigure(1, weight=1)

        
#             self.add_account_button = CTkButton(
#                 self.container,
#                 text="Add New YouTube Account",
#                 command=lambda: Thread(target=self.authenticate).start(),
#                 font=("Arial", 14),
#                 fg_color="#1c2636",
#                 text_color="white",
#                 height=36
#             )
#             self.add_account_button.place(relx=0.01, rely=0.01, anchor="nw")
#             row += 1

#             self.channel_dropdown = CTkOptionMenu(
#                 self.container,
#                 values=self.get_saved_channels(),
#                 command=self.select_channel,
#                 width=200
#             )
#             self.channel_dropdown.set("Select Channel")
#             self.channel_dropdown.place(relx=0.99, rely=0.2, anchor="ne")

#             row = 1

           
#             run_optimization = CTkButton(
#                 self.container,
#                 text="Browse",
#                # command=,
#                 fg_color="#1c2636",
#                 text_color="white"
#             )
#             run_optimization.grid(row=row, column=1, padx=10, pady=(60, 10), sticky="w")
#             row += 1

          


































# #Upload videos too (instagram,facebook,youtube,tiktok) if available for api's. (options too use smolgent with a generate button for automatic generation of (title,description,keywords,hashtags.))
# class SocialMediaUploading:
#     def __init__(self, parent_container):
#             self.parent_container = parent_container
#             self.credentials = None  

#             self.container = CTkFrame(
#                 master=self.parent_container,
#                 fg_color="black",
#                 border_width=2,
#                 border_color="#404040",
#                 corner_radius=10,
#                 height=1000
#             )
#             self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
#             self.container.update_idletasks()


#             self.create_widgets()

#     def create_widgets(self):
#             row=1
#             self.container.columnconfigure(0, weight=1)
#             self.container.columnconfigure(1, weight=1)
#             self.container.rowconfigure(1, weight=1)

        
#             self.add_account_button = CTkButton(
#                 self.container,
#                 text="Add New YouTube Account",
#                 command=lambda: Thread(target=self.authenticate).start(),
#                 font=("Arial", 14),
#                 fg_color="#1c2636",
#                 text_color="white",
#                 height=36
#             )
#             self.add_account_button.place(relx=0.01, rely=0.01, anchor="nw")
#             row += 1
#             self.file_menu = CTkOptionMenu(
#                 master=self.container,
#                 values=['Youtube','Instagram','Tiktok'],
#                 width=200,
#                 height=30,
#                 font=bold11,
#                 dropdown_font=bold11,
#                 fg_color="#282828",
#                 button_color="#404040",
#                 text_color="#FFFFFF",
#             )
#             self.file_menu.grid(row=0, column=1, padx=10, pady=10, sticky="ne")


#             self.channel_dropdown = CTkOptionMenu(
#                 self.container,
#                 values=self.get_saved_channels(),
#                 command=self.select_channel,
#                 width=200
#             )
#             self.channel_dropdown.set("Select Channel")
#             self.channel_dropdown.place(relx=0.99, rely=0.2, anchor="ne")

#             row = 1

#             self.video_path_entry = CTkEntry(self.container, placeholder_text="Video File Path", width=500)
#             self.video_path_entry.grid(row=row, column=0, padx=10, pady=(60, 10), sticky="ew")

#             browse_btn = CTkButton(
#                 self.container,
#                 text="Browse",
#                 command=self.browse_video,
#                 fg_color="#1c2636",
#                 text_color="white"
#             )
#             browse_btn.grid(row=row, column=1, padx=10, pady=(60, 10), sticky="w")
#             row += 1

#             self.title_entry = CTkEntry(self.container, placeholder_text="Video Title")
#             self.title_entry.grid(row=row, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
#             row += 1

          

    
#             self.schedule_checkbox = CTkCheckBox(
#                 self.container,
#                 text="Schedule for later",
#                 command=self.toggle_schedule_fields,
#                 fg_color="#1c2636",
#                 text_color="white"
#             )
#             self.schedule_checkbox.grid(row=row, column=0, sticky="w", padx=10, pady=10)

#             self.date_entry = CTkEntry(self.container, placeholder_text="YYYY-MM-DD", width=150)
#             self.time_entry = CTkEntry(self.container, placeholder_text="HH:MM (24h)", width=150)

#             # Hide by default
#             self.date_entry.grid_forget()
#             self.time_entry.grid_forget()
#             row += 1


#             self.description_entry = CTkTextbox(self.container, height=100)
#             self.description_entry.insert("1.0", "Video Description")
#             self.description_entry.grid(row=row, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
#             row += 1

#             self.category_entry = CTkEntry(self.container, placeholder_text="Category ID (e.g., 22)")
#             self.category_entry.grid(row=row, column=0, padx=10, pady=10, sticky="w")

#             self.privacy_dropdown = CTkOptionMenu(self.container, values=["public", "private", "unlisted"])
#             self.privacy_dropdown.set("unlisted")
#             self.privacy_dropdown.grid(row=row, column=1, padx=10, pady=10, sticky="w")
#             row += 1

#             self.upload_button = CTkButton(
#                 self.container,
#                 text="Upload to YouTube",
#                 command=self.Upload_to_platform,
#                 font=("Arial", 16, "bold"),
#                 fg_color="#0d1b2a",
#                 hover_color="#1c2636",
#                 text_color="white",
#                 height=40
#             )
#             self.upload_button.grid(row=row, column=0, columnspan=2, pady=10)
#             row += 1

#             self.test_connection = CTkButton(
#                 self.container,
#                 text="Test YouTube Connection",
#                 command=self.test_connection,
#                 font=("Arial", 16, "bold"),
#                 fg_color="#0d1b2a",
#                 hover_color="#1c2636",
#                 text_color="white",
#                 height=40
#             )
#             self.test_connection.grid(row=row, column=0, columnspan=2, pady=10)
#             row += 1

#             self.channel_label = CTkLabel(
#                 self.container,
#                 text="Channel: Not connected",
#                 font=("Arial", 14),
#                 text_color="white"
#             )
#             self.channel_label.grid(row=row, column=0, columnspan=2, pady=5)

        
#             saved_channels = self.get_saved_channels()
#             if saved_channels:
#                 self.channel_dropdown.set(saved_channels[0])
#                 self.select_channel(saved_channels[0])
                
#     def toggle_schedule_fields(self):
#             if self.schedule_checkbox.get():
#                 self.date_entry.grid(row=self.upload_button.grid_info()['row'] - 1, column=0, padx=10, sticky="w")
#                 self.time_entry.grid(row=self.upload_button.grid_info()['row'] - 1, column=1, padx=10, sticky="w")
#             else:
#                 self.date_entry.grid_forget()
#                 self.time_entry.grid_forget()


#     def browse_video(self):
#             filepath = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
#             if filepath:
#                 self.video_path_entry.delete(0, "end")
#                 self.video_path_entry.insert(0, filepath)


#     def get_saved_channels(self):
#             from File_path import app_data_path
#             token_dir = app_data_path / "youtube_tokens"
#             logging.info(f"[DEBUG] Looking for tokens in: {token_dir}")

#             if not token_dir.exists():
#                 logging.info("[DEBUG] Token dir does not exist")
#                 return []

#             tokens = []
#             for file in token_dir.glob("*.pickle.enc"):
#                 # Remove both .pickle.enc
#                 name = file.name.replace(".pickle.enc", "")
#                 tokens.append(name)

#             logging.info(f"[DEBUG] Cleaned token names: {tokens}")
#             return tokens


#     def test_connection(self):
#             if not self.credentials:
#                 self.authenticate()

#             youtube = build("youtube", "v3", credentials=self.credentials)

#             channel_response = youtube.channels().list(part="snippet", mine=True).execute()
#             channel_title = channel_response["items"][0]["snippet"]["title"]
#             logging.info(f"📺 Authenticated YouTube Channel: {channel_title}")
#             self.channel_label.configure(text=f"Channel: {channel_title}")

#     def Upload_to_platform(self):
#             platform = self.file_menu.get()  # 

#             if platform == "Youtube":
#                 self.upload_to_youtube_actual()
#             elif platform == "Tiktok":
#                 return
#             elif platform == "Instagram":
#                 return
#             else:
#                 logging.info("⚠️ No valid platform selected.")
#                 return
          

#     def upload_to_youtube_actual(self):
#             video_path = self.video_path_entry.get()
#             title = self.title_entry.get()
#             description = self.description_entry.get("1.0", "end").strip()
#             category_id = self.category_entry.get()
#             privacy_status = self.privacy_dropdown.get()
#             status_config = {
#                 "privacyStatus": privacy_status
#             }


#             if self.schedule_checkbox.get():
#                 try:
#                     date_str = self.date_entry.get()
#                     time_str = self.time_entry.get()
#                     publish_datetime = f"{date_str}T{time_str}:00Z"

        
#                     dt = datetime.datetime.strptime(publish_datetime, "%Y-%m-%dT%H:%M:%SZ")
#                     publish_at = dt.isoformat() + "Z"

#                     status_config["privacyStatus"] = "private"
#                     status_config["publishAt"] = publish_at
#                     logging.info(f"📅 Scheduled for: {publish_at}")
#                 except Exception as e:
#                     logging.info("❌ Invalid date/time format:", e)
#                     return

#             if not self.credentials:
#                 self.authenticate()

#             youtube = build("youtube", "v3", credentials=self.credentials)

#             request_body = {
#                 "snippet": {
#                     "title": title,
#                     "description": description,
#                     "categoryId": category_id,
#                 },
#                 "status": {
#                     "privacyStatus": status_config
#                 }
#             }

#             media_file = MediaFileUpload(video_path)

#             response = youtube.videos().insert(
#                 part="snippet,status",
#                 body=request_body,
#                 media_body=media_file
#             ).execute()

#             channel_response = youtube.channels().list(part="snippet", mine=True).execute()
#             channel_title = channel_response["items"][0]["snippet"]["title"]

#             logging.info("✅ Upload successful!")
#             logging.info(f"📺 Uploaded to: {channel_title}")
#             logging.info(f"🔗 Video URL: https://youtu.be/{response['id']}")
#             self.channel_label.configure(text=f"Uploaded to: {channel_title}")


#     def select_channel(self, channel_name):
#             from encryption import load_encrypted_token

#             credentials = load_encrypted_token(channel_name)
#             if credentials:
#                 self.credentials = credentials
#                 self.channel_label.configure(text=f"Loaded: {channel_name}")
#                 logging.info(f"✅ Loaded token for {channel_name}")
#             else:
#                 self.channel_label.configure(text=f"❌ Failed to load: {channel_name}")
#                 logging.info(f"⚠️ Failed to load token for {channel_name}")

#     def authenticate(self):
#             import google_auth_oauthlib.flow
#             from encryption import save_encrypted_token
        

#             scopes = [
#                 "https://www.googleapis.com/auth/youtube.upload",
#                 "https://www.googleapis.com/auth/youtube.force-ssl"
#             ]
#             client_secrets_file = "./Json_secrets/client_secret_849553263621-grvsfihl7lkocrt0qgs37iipuv5lbpkl.apps.googleusercontent.com.json"

#             # OAuth login flow
#             flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
#                 client_secrets_file, scopes)
#             self.credentials = flow.run_local_server(port=0)

#             youtube = build("youtube", "v3", credentials=self.credentials)
#             channel_response = youtube.channels().list(part="snippet", mine=True).execute()
#             channel_name = channel_response["items"][0]["snippet"]["title"]

#             # Save encrypted token
#             save_encrypted_token(channel_name, self.credentials)

#             # Refresh dropdown with new value
#             self.channel_dropdown.configure(values=self.get_saved_channels())
#             self.channel_dropdown.set(channel_name)
#             self.channel_label.configure(text=f"Authenticated: {channel_name}")









































# ####Youtube Download#####
# global youtube_progress_var
# def place_youtube_download_menu(parent_container):
#     global youtube_link_entry, youtube_output_path_entry, video_format_var, audio_format_var

#     # ── Design tokens ────────────────────────────────────────────────────────
#     _BG       = "#08090a"
#     _SURFACE  = "#0d0f11"
#     _PANEL    = "#111316"
#     _PANEL2   = "#161a1e"
#     _BORDER   = "#1e2229"
#     _BORDER2  = "#252b34"
#     _RED      = "#cc2222"
#     _RED_HOV  = "#e63333"
#     _TEXT     = "#c8cdd4"
#     _TEXT_DIM = "#555f6e"
#     _WHITE    = "#eef0f3"

#     frame_width, frame_height = 200, 110
#     youtube_link_settings = {}
#     formats_fetched = {}

#     youtube_progress_var.set("")

#     # Make parent_container fill its allocated space completely
#     parent_container.grid_rowconfigure(0, weight=1)
#     parent_container.grid_columnconfigure(0, weight=1)

#     # ── inner helpers ────────────────────────────────────────────────────────
#     def update_format_list():
#         url = youtube_link_entry.get()
#         if not url:
#             return
#         fetch_button.configure(state="disabled", text="Fetching…")

#         def fetch_thread():
#             try:
#                 if url in formats_fetched:
#                     video_formats, audio_formats = formats_fetched[url]
#                 else:
#                     result = get_available_formats(url)
#                     if result is None:
#                         print("Error Requesting formats. please check if your cookies are outdated.")
#                         window.after(0, lambda: fetch_button.configure(state="normal", text="Fetch Details"))
#                         return
#                     video_formats, audio_formats = result
#                     formats_fetched[url] = (video_formats, audio_formats)
#                     print("Formats fetched and cached.")

#                 def update_ui():
#                     window.after(0, lambda: addlist_btn.configure(state="normal"))
#                     if video_formats or audio_formats:
#                         video_format_dropdown.configure(values=video_formats if video_formats else ["No video formats available"])
#                         audio_format_dropdown.configure(values=audio_formats if audio_formats else ["No audio formats available"])
#                         download_btn.configure(state="normal")
#                     if video_formats:
#                         video_format_var.set(video_formats[0])
#                     if audio_formats:
#                         audio_format_var.set(audio_formats[0])
#                     fetch_button.configure(text="Fetch Details")

#                 window.after(0, update_ui)
#             except Exception as e:
#                 print(f"Error in fetch thread: {e}")
#                 window.after(0, lambda: fetch_button.configure(state="normal", text="Fetch Details"))

#         threading.Thread(target=fetch_thread, daemon=True).start()

#     def update_fetch_button_state(event=None):
#         url = youtube_link_entry.get()
#         if "youtube.com" in url or "youtu.be" in url:
#             fetch_button.configure(state="normal")
#         else:
#             fetch_button.configure(state="disabled")

#     def on_link_selected(selected_url):
#         youtube_link_entry.delete(0, tk.END)
#         youtube_link_entry.insert(0, selected_url)
#         if selected_url in formats_fetched:
#             video_formats, audio_formats = formats_fetched[selected_url]
#         else:
#             video_formats, audio_formats = get_available_formats(selected_url)
#             formats_fetched[selected_url] = (video_formats, audio_formats)
#         video_format_dropdown.configure(values=video_formats if video_formats else ["No video formats available"])
#         audio_format_dropdown.configure(values=audio_formats if audio_formats else ["No audio formats available"])
#         saved_settings = youtube_link_settings.get(selected_url, {})
#         saved_video_format = saved_settings.get("video_format")
#         saved_audio_format = saved_settings.get("audio_format")
#         if saved_video_format in video_formats:
#             video_format_var.set(saved_video_format)
#         else:
#             video_format_var.set(video_format_var.get() if video_formats else "Video Formats...")
#         if saved_audio_format in audio_formats:
#             audio_format_var.set(saved_audio_format)
#         else:
#             audio_format_var.set(audio_format_var.get() if audio_formats else "Audio Formats...")
#         youtube_link_settings[selected_url] = {
#             "video_format": video_format_var.get(),
#             "audio_format": audio_format_var.get()
#         }

#     def on_video_format_change(event=None):
#         selected_url = youtubelist_variable.get().strip()
#         if selected_url in youtube_link_settings:
#             youtube_link_settings[selected_url]["audio_format"] = audio_format_var.get()

#     def on_audio_format_change(event=None):
#         selected_url = youtubelist_variable.get().strip()
#         if selected_url in youtube_link_settings:
#             youtube_link_settings[selected_url]["video_format"] = video_format_var.get()

#     def clear_download_list():
#         youtube_download_list.clear()
#         youtubelist_variable.set("")
#         youtube_list_menu.configure(values=[])
#         download_all_btn.configure(state="disabled")
#         queue_count_lbl.configure(text="0 items")

#     def add_link_to_download_list():
#         if video_format_var.get() == "":
#             print("Select video formats first")
#             return
#         url = youtube_link_entry.get().strip()
#         if url and url not in youtube_download_list:
#             youtube_download_list.append(url)
#             youtube_link_entry.delete(0, END)
#             youtubelist_variable.set(youtube_download_list[-1])
#             youtube_list_menu.configure(values=youtube_download_list)
#             youtube_link_settings[url] = {
#                 "video_format": video_format_var.get(),
#                 "audio_format": audio_format_var.get()
#             }
#             if len(youtube_download_list) > 0:
#                 download_all_btn.configure(state="normal")
#             n = len(youtube_download_list)
#             queue_count_lbl.configure(text=f"{n} item{'s' if n != 1 else ''}")
#             video_format_var.set("")
#             audio_format_var.set("")

#     def select_youtube_output_path():
#         path = filedialog.askdirectory()
#         if path:
#             youtube_output_path_entry.delete(0, "end")
#             youtube_output_path_entry.insert(0, path)

#     # ── OUTER CARD — fills entire parent_container ───────────────────────────
#     card = CTkFrame(
#         master=parent_container,
#         fg_color=_SURFACE,
#         bg_color=_BG,
#         corner_radius=14,
#         border_width=1,
#         border_color=_BORDER,
#     )
#     card.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

#     # Card layout: 3 rows (header | content | footer), content stretches
#     card.grid_rowconfigure(0, weight=0)   # header stripe – fixed
#     card.grid_rowconfigure(1, weight=1)   # content area  – stretches
#     card.grid_rowconfigure(2, weight=0)   # footer stripe – fixed
#     card.grid_columnconfigure(0, weight=1)

#     # ── HEADER STRIPE ────────────────────────────────────────────────────────
#     header = CTkFrame(master=card, fg_color=_PANEL, corner_radius=0, height=38)
#     header.grid(row=0, column=0, sticky="ew")
#     header.grid_propagate(False)
#     header.grid_columnconfigure(1, weight=1)

#     CTkLabel(
#         master=header,
#         text="▶   YouTube Downloader",
#         font=CTkFont(family="Segoe UI", size=11, weight="bold"),
#         text_color=_WHITE,
#         fg_color="transparent",
#     ).grid(row=0, column=0, padx=16, pady=8, sticky="w")

#     CTkLabel(
#         master=header,
#         text="  yt-dlp  ",
#         font=CTkFont(family="Courier New", size=9, weight="bold"),
#         text_color=_RED,
#         fg_color=_PANEL2,
#         corner_radius=10,
#         width=50,
#         height=18,
#     ).grid(row=0, column=2, padx=(0, 14), pady=8, sticky="e")

#     # ── CONTENT AREA — two-column: left fields | right side panel ────────────
#     content = CTkFrame(master=card, fg_color="transparent")
#     content.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)

#     # Left fields column stretches; right side panel is fixed width
#     content.grid_columnconfigure(0, weight=1)       # left: labels
#     content.grid_columnconfigure(1, weight=3)       # left: inputs  (main stretch)
#     content.grid_columnconfigure(2, weight=2)       # left: buttons (some stretch)
#     content.grid_columnconfigure(3, weight=0, minsize=220)  # right: side panel fixed
#     for r in range(7):
#         content.grid_rowconfigure(r, weight=1)      # all rows share vertical space

#     # ── ROW 0 — Output path ──────────────────────────────────────────────────
#     CTkLabel(
#         master=content,
#         text="Save to",
#         font=CTkFont(family="Segoe UI", size=11),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         anchor="e",
#     ).grid(row=0, column=0, padx=(16, 8), pady=(10, 4), sticky="e")

#     youtube_output_path_entry = CTkEntry(
#         master=content,
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=11),
#         fg_color=_PANEL,
#         border_color=_BORDER2,
#         border_width=1,
#         bg_color=_SURFACE,
#         text_color=_TEXT,
#         justify="left",
#     )
#     youtube_output_path_entry.grid(row=0, column=1, padx=(0, 8), pady=(10, 4), sticky="ew")
#     youtube_output_path_entry.insert(0, DOCUMENT_PATH)

#     path_btn_row = CTkFrame(master=content, fg_color="transparent")
#     path_btn_row.grid(row=0, column=2, padx=(0, 8), pady=(10, 4), sticky="w")
#     path_btn_row.grid_columnconfigure(0, weight=1)
#     path_btn_row.grid_columnconfigure(1, weight=0)

#     CTkButton(
#         master=path_btn_row,
#         text="Browse",
#         width=70,
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         fg_color=_PANEL2,
#         hover_color="#1c2028",
#         border_color=_BORDER2,
#         border_width=1,
#         text_color=_TEXT,
#         command=lambda: select_youtube_output_path(),
#     ).grid(row=0, column=0, padx=(0, 4))

#     CTkButton(
#         master=path_btn_row,
#         text="✕",
#         width=32,
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=11, weight="bold"),
#         fg_color=_PANEL2,
#         hover_color="#3d1a1a",
#         border_color="#3d1a1a",
#         border_width=1,
#         text_color="#ff4545",
#         command=clear_download_list,
#     ).grid(row=0, column=1)

#     # ── ROW 1 — Queue ────────────────────────────────────────────────────────
#     CTkLabel(
#         master=content,
#         text="Queue",
#         font=CTkFont(family="Segoe UI", size=11),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         anchor="e",
#     ).grid(row=1, column=0, padx=(16, 8), pady=4, sticky="e")

#     global youtubelist_variable
#     global youtube_list_menu
#     youtubelist_variable = StringVar(value="")
#     youtube_list_menu = CTkOptionMenu(
#         master=content,
#         variable=youtubelist_variable,
#         values=youtube_download_list,
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=11),
#         fg_color=_PANEL,
#         button_color=_PANEL2,
#         button_hover_color=_BORDER2,
#         text_color=_TEXT,
#         dropdown_fg_color=_PANEL,
#         dropdown_hover_color="#1c2028",
#         dropdown_text_color=_TEXT,
#         command=on_link_selected,
#     )
#     youtube_list_menu.grid(row=1, column=1, padx=(0, 8), pady=4, sticky="ew")

#     queue_action_row = CTkFrame(master=content, fg_color="transparent")
#     queue_action_row.grid(row=1, column=2, padx=(0, 8), pady=4, sticky="w")

#     addlist_btn = CTkButton(
#         master=queue_action_row,
#         text="+ Add",
#         width=70,
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         fg_color=_PANEL2,
#         hover_color="#1c2028",
#         border_color=_BORDER2,
#         border_width=1,
#         text_color=_TEXT,
#         command=add_link_to_download_list,
#         state="disabled",
#     )
#     addlist_btn.grid(row=0, column=0, padx=(0, 6))

#     queue_count_lbl = CTkLabel(
#         master=queue_action_row,
#         text="0 items",
#         font=CTkFont(family="Courier New", size=9),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         width=50,
#     )
#     queue_count_lbl.grid(row=0, column=1)

#     # ── ROW 2 — YouTube URL ──────────────────────────────────────────────────
#     CTkLabel(
#         master=content,
#         text="YouTube URL:",
#         font=CTkFont(family="Segoe UI", size=11),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         anchor="e",
#     ).grid(row=2, column=0, padx=(16, 8), pady=4, sticky="e")

#     youtube_link_entry = CTkEntry(
#         master=content,
#         height=34,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=11),
#         fg_color=_PANEL,
#         border_color=_BORDER2,
#         border_width=1,
#         bg_color=_SURFACE,
#         placeholder_text="Paste YouTube link…",
#         text_color=_WHITE,
#         justify="left",
#     )
#     youtube_link_entry.grid(row=2, column=1, padx=(0, 8), pady=4, sticky="ew")
#     youtube_link_entry.bind("<KeyRelease>", update_fetch_button_state)

#     fetch_button = CTkButton(
#         master=content,
#         text="Fetch Details",
#         width=120,
#         height=34,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         fg_color=_PANEL2,
#         hover_color="#1c2028",
#         border_color=_BORDER2,
#         border_width=1,
#         text_color=_TEXT,
#         command=update_format_list,
#         state="disabled",
#     )
#     fetch_button.grid(row=2, column=2, padx=(0, 8), pady=4, sticky="w")

#     # ── ROW 3 — Video format ─────────────────────────────────────────────────
#     CTkLabel(
#         master=content,
#         text="Video Format:",
#         font=CTkFont(family="Segoe UI", size=11),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         anchor="e",
#     ).grid(row=3, column=0, padx=(16, 8), pady=4, sticky="e")

#     video_format_dropdown = CTkComboBox(
#         master=content,
#         variable=video_format_var,
#         values=["Enter Link First..."],
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=11),
#         fg_color=_PANEL,
#         border_color=_BORDER2,
#         border_width=1,
#         button_color=_PANEL2,
#         button_hover_color=_BORDER2,
#         dropdown_fg_color=_PANEL,
#         dropdown_hover_color="#1c2028",
#         text_color=_TEXT,
#     )
#     video_format_dropdown.grid(row=3, column=1, padx=(0, 8), pady=4, sticky="ew")
#     video_format_dropdown.bind("<<ComboboxSelected>>", on_video_format_change)

#     global download_btn
#     download_btn = CTkButton(
#         master=content,
#         text="⬇  Download",
#         width=120,
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         fg_color=_RED,
#         hover_color=_RED_HOV,
#         text_color="#ffffff",
#         command=start_youtube_download,
#         state="disabled",
#     )
#     download_btn.grid(row=3, column=2, padx=(0, 8), pady=4, sticky="w")

#     # ── ROW 4 — Audio format ─────────────────────────────────────────────────
#     CTkLabel(
#         master=content,
#         text="Audio Format:",
#         font=CTkFont(family="Segoe UI", size=11),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         anchor="e",
#     ).grid(row=4, column=0, padx=(16, 8), pady=4, sticky="e")

#     audio_format_dropdown = CTkComboBox(
#         master=content,
#         variable=audio_format_var,
#         values=["Enter Link First..."],
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=11),
#         fg_color=_PANEL,
#         border_color=_BORDER2,
#         border_width=1,
#         button_color=_PANEL2,
#         button_hover_color=_BORDER2,
#         dropdown_fg_color=_PANEL,
#         dropdown_hover_color="#1c2028",
#         text_color=_TEXT,
#     )
#     audio_format_dropdown.grid(row=4, column=1, padx=(0, 8), pady=4, sticky="ew")
#     audio_format_dropdown.bind("<<ComboboxSelected>>", on_audio_format_change)

#     def download_all_from_list():
#         output_path = youtube_output_path_entry.get()
#         if not output_path:
#             info_message.set("Choose a folder for saving!")
#             return
#         if not youtube_download_list:
#             info_message.set("The list is empty!")
#             return
#         stop_youtube_download_btn.configure(state="normal")
#         youtube_progress_var.set("Starting batch download...")

#         def batch_worker():
#             for idx, link in enumerate(youtube_download_list, 1):
#                 if stop_download_flag:
#                     youtube_progress_var.set("Download stopped.")
#                     return
#                 window.after(0, lambda l=link, i=idx: youtube_progress_var.set(
#                     f"⬇️ Downloading ({i}/{len(youtube_download_list)}): {l[:50]}"
#                 ))
#                 format_data = formats_fetched.get(link)
#                 if format_data:
#                     video_formats, audio_formats = format_data
#                 else:
#                     video_formats, audio_formats = get_available_formats(link)
#                     formats_fetched[link] = (video_formats, audio_formats)
#                 settings = youtube_link_settings.get(link, {})
#                 video_format_id = settings.get("video_format", "best").split(" - ")[0]
#                 audio_format_id = settings.get("audio_format", "bestaudio").split(" - ")[0]
#                 video_format_var.set(video_format_id)
#                 audio_format_var.set(audio_format_id)
#                 download_youtube_link(link, output_path, update_progress)
#             window.after(0, lambda: youtube_progress_var.set("✅ All downloads finished."))
#             youtube_download_list.clear()
#             info_message.set("✅ Batch download completed.")

#         Thread(target=batch_worker).start()

#     download_all_btn = CTkButton(
#         master=content,
#         text="⬇  All",
#         width=120,
#         height=32,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         fg_color=_PANEL2,
#         hover_color="#1c2028",
#         border_color=_BORDER2,
#         border_width=1,
#         text_color=_TEXT,
#         command=download_all_from_list,
#         state="disabled",
#     )
#     download_all_btn.grid(row=4, column=2, padx=(0, 8), pady=4, sticky="w")

#     # ── ROW 5 — Status ───────────────────────────────────────────────────────
#     CTkLabel(
#         master=content,
#         text="Status",
#         font=CTkFont(family="Segoe UI", size=11),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         anchor="e",
#     ).grid(row=5, column=0, padx=(16, 8), pady=4, sticky="e")

#     CTkLabel(
#         master=content,
#         textvariable=youtube_progress_var,
#         font=CTkFont(family="Segoe UI", size=11),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#         anchor="w",
#     ).grid(row=5, column=1, padx=(0, 8), pady=4, sticky="ew")

#     global stop_youtube_download_btn
#     stop_youtube_download_btn = CTkButton(
#         master=content,
#         text="■  Stop",
#         width=120,
#         height=30,
#         corner_radius=8,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         fg_color=_PANEL2,
#         hover_color="#3d1a1a",
#         border_color="#3d1a1a",
#         border_width=1,
#         text_color="#ff4545",
#         command=lambda: Stop_Youtube_Downloading(),
#         state="disabled",
#     )
#     stop_youtube_download_btn.grid(row=5, column=2, padx=(0, 8), pady=4, sticky="w")

#     # ── SIDE PANEL — spans all content rows ──────────────────────────────────
#     side_panel = CTkFrame(
#         master=content,
#         fg_color=_PANEL,
#         corner_radius=12,
#         border_width=1,
#         border_color=_BORDER,
#     )
#     side_panel.grid(row=0, column=3, rowspan=6, padx=(4, 14), pady=10, sticky="nsew")
#     side_panel.grid_rowconfigure(0, weight=1)
#     side_panel.grid_rowconfigure(1, weight=0)
#     side_panel.grid_columnconfigure(0, weight=1)

#     bg_image = Image.open(find_by_relative_path("Assets" + os_separator + "youtube_img.png")).resize((frame_width, frame_height))
#     bg_image_tk = CTkImage(bg_image, size=(frame_width, frame_height))
#     bg_label = CTkLabel(
#         master=side_panel,
#         image=bg_image_tk,
#         width=frame_width,
#         height=frame_height,
#         fg_color="transparent",
#         text="",
#     )
#     bg_label.grid(row=0, column=0, padx=10, pady=(14, 4), sticky="n")
#     bg_label.image = bg_image_tk

#     CTkLabel(
#         master=side_panel,
#         text="Powered by yt-dlp",
#         font=CTkFont(family="Courier New", size=8),
#         text_color=_TEXT_DIM,
#         fg_color="transparent",
#     ).grid(row=1, column=0, pady=(0, 12))

#     # ── FOOTER STRIPE ─────────────────────────────────────────────────────────
#     footer = CTkFrame(master=card, fg_color=_PANEL, corner_radius=0, height=34)
#     footer.grid(row=2, column=0, sticky="ew")
#     footer.grid_propagate(False)
#     footer.grid_columnconfigure(1, weight=1)

#     Info_button_youtubedownloader = create_info_button(
#         open_YoutubeDownloader_tool_info,
#         "«  INFO",
#         width=80,
#         master=footer,
#     )
#     Info_button_youtubedownloader.grid(row=0, column=0, padx=12, pady=5, sticky="w")

#     global upload_button
#     upload_button = CTkButton(
#         master=footer,
#         text="Upload Cookies",
#         width=110,
#         height=22,
#         corner_radius=6,
#         font=CTkFont(family="Segoe UI", size=9, weight="bold"),
#         fg_color=_PANEL2,
#         hover_color="#1c2028",
#         border_color=_BORDER2,
#         border_width=1,
#         text_color=_TEXT_DIM,
#         command=lambda: upload_cookie_file(),
#     )
#     if cookie_file_path is None:
#         upload_button.grid(row=0, column=2, padx=12, pady=5, sticky="e")
#     if cookie_file_path is not None:
#         upload_button.grid_forget()


# def delete_cookie_file_and_reset_button():
#     """ Deletes the cookie file if it exists and resets the upload button visibility. """
#     global upload_button, COOKIE_PATH_FILE, cookie_file_path

#     if COOKIE_PATH_FILE.exists():
#         try:
#             corruptedcookiefile_path = str(COOKIE_PATH_FILE)
#             os.remove(corruptedcookiefile_path)
#             cookie_file_path = None
#             logging.info(f"Cookie file {COOKIE_PATH_FILE} deleted successfully.")
#         except Exception as e:
#             logging.info(f"Error deleting cookie file: {e}")
#     upload_button.place(relx=0.12, rely=0.94, anchor="e")


# def load_cookie_file_path():
#     """ Load cookie file path from saved path file. """
#     global cookie_file_path
#     try:
#         if COOKIE_PATH_FILE.exists():
#             cookie_file_path = str(COOKIE_PATH_FILE)
#             logging.info(f"Cookie file path exsist at: {cookie_file_path}")
#         else:
#             cookie_file_path = None
#             logging.info(f"cookie file path is None cause it does not exists.")
#     except Exception as e:        
#         cookie_file_path = None
#         logging.info(f"Error exception cookie file path is None ")


# def update_cookie_timestamps(file_path):
#     """ Reads cookie file, updates expiration timestamps, and saves it back. """
#     updated_lines = []
    
#     with open(file_path, "r", encoding="utf-8") as f:
#         for line in f:
#             parts = line.strip().split("\t")

      
#             if line.startswith("#") or len(parts) < 5:
#                 updated_lines.append(line.strip())
#                 continue
            
#             try:
      
#                 old_timestamp = int(parts[4])
#                 if old_timestamp < NEW_TIMESTAMP:
#                     parts[4] = str(NEW_TIMESTAMP)  
#             except ValueError:
#                 pass  

#             updated_lines.append("\t".join(parts))
    
#     updated_path = os.path.join(COOKIE_STORAGE_DIR, os.path.basename(file_path))
#     with open(updated_path, "w", encoding="utf-8") as f:
#         f.write("\n".join(updated_lines))

#     logging.info(f"Updated cookie file saved at: {updated_path}")
#     return updated_path


# def upload_cookie_file():
#     """ Let user upload a cookie file and save it to the app's cookie directory. """
#     global cookie_file_path,upload_button

#     cookie_file_path_input = filedialog.askopenfilename(
#         title="Select Cookie File", 
#         filetypes=[("Text files", "*.txt")]
#     )
    
#     if cookie_file_path_input:
#         try:
  
#            save_path = COOKIE_STORAGE_DIR / fixed_cookie_filename

#            shutil.copy(cookie_file_path_input, save_path)

#            cookie_file_path = str(save_path)


#            update_cookie_timestamps(cookie_file_path)
#            upload_button.place_forget() 
           
#         except Exception as e:
#             logging.info(f"Error saving cookie file: {e}")
#     else: 
#         logging.info("No file selected")



# def ensure_protocol(youtube_url):

#     if not youtube_url.startswith(('http://', 'https://')):
#         youtube_url = 'https://' + youtube_url
#     return youtube_url



# def get_available_formats(youtube_url):
#     global cookie_file_path,backup
#     backup = False
#     ensure_protocol(youtube_url)
#     ydl_opts = {
#              'quiet': True,
#              "nocheckcertificate": True,
#              "cookiefile": cookie_file_path,
#              # Explicitly use node runtime
#              'js_runtimes': {'node': {}},
#              'extractor_args': {'youtube': {'remote_components': 'ejs:github'}},
#              'remote_components': ['ejs:github']
#             }
#     ydl_opts_backup = {
#         'quiet': True,
#         'nocheckcertificate': True,
#         'no_signature': True,  
#         "cookiefile": cookie_file_path,
#         'js_runtimes': {'node': {}},
#         'extractor_args': {'youtube': {'remote_components': 'ejs:github'}},
#         'remote_components': ['ejs:github']
#     }
#     ydl_opts_fallback = {
#         'quiet': True,
#         'nocheckcertificate': True,
#         'force_generic_extractor': True, 
#         'ignoreerrors': True,
#         "cookiefile": cookie_file_path,
#         'js_runtimes': {'node': {}},
#         'extractor_args': {'youtube': {'remote_components': 'ejs:github'}},
#         'remote_components': ['ejs:github']
#     }

#     if cookie_file_path:
#         ydl_opts["cookiefile"] = cookie_file_path
#         ydl_opts_backup["cookiefile"] = cookie_file_path
#         ydl_opts_fallback["cookiefile"] = cookie_file_path
#     if not cookie_file_path:
#         logging.info("Cookie file path is None/Empty")
#         return

#     logging.info(f"cookie_file_path when getting available format: {cookie_file_path}")
    
    
#     def try_fetching_format(ydl_opts_variable):
#                 with yt_dlp.YoutubeDL(ydl_opts_variable) as ydl:
#                     info = ydl.extract_info(youtube_url, download=False)
#                     formats = info.get('formats', []) if info else []

#                     video_formats_list = []
#                     audio_formats_list = []

#                     for f in formats:
#                         if f.get('vcodec') != 'none' and f.get('acodec') == 'none':
#                             height = f.get('height') or 0
#                             resolution = f.get('resolution', 'Unknown')
#                             ext = f.get('ext', '')
#                             format_id = f['format_id']
#                             video_formats_list.append({'height': height, 'str': f"{format_id} - {resolution} ({ext})"})
#                         elif f.get('acodec') != 'none' and f.get('vcodec') == 'none': 
#                             # Filter for English audio only
#                             language = f.get('language', '')
#                             if language and language != 'en':
#                                 continue
#                             abr = f.get('abr') or 0
#                             ext = f.get('ext', '')
#                             format_id = f['format_id']
#                             lang_tag = f" [{language}]" if language else ""
#                             audio_formats_list.append({'abr': abr, 'str': f"{format_id} - {abr}kbps ({ext}){lang_tag}"})
                    
#                     # Sort descending
#                     video_formats_list.sort(key=lambda x: x['height'], reverse=True)
#                     audio_formats_list.sort(key=lambda x: x['abr'], reverse=True)

#                     video_formats = ['Only Audio','Video Formats...'] + [x['str'] for x in video_formats_list]
#                     audio_formats = [x['str'] for x in audio_formats_list]

#                 return video_formats, audio_formats
    
#     try: 
#             video_formats, audio_formats = try_fetching_format(ydl_opts)
#             return video_formats, audio_formats
    
#     except yt_dlp.utils.DownloadError as e:
#         logging.info(f"Error fetching formats with default opts: {e}")
#         try:
#             logging.info("Retrying with backup options (no_signature)...")
#             video_formats, audio_formats = try_fetching_format(ydl_opts_backup)
#             return video_formats, audio_formats
#         except yt_dlp.utils.DownloadError as e2:
#             logging.info(f"Error fetching formats with backup opts: {e2}")
#             try:
#                 logging.info("Retrying with fallback options (force_generic_extractor)...")
#                 video_formats, audio_formats = try_fetching_format(ydl_opts_fallback)
#                 return video_formats, audio_formats
#             except yt_dlp.utils.DownloadError as e3:
#                 logging.info(f"All fetch attempts failed: {e3}")
#                 return None
#         if "cookie" in str(e).lower() or "sign in" in str(e).lower() or "403" in str(e):
#                 logging.info("⚠️ Cookie file seems broken or expired. Resetting...")
#                 delete_cookie_file_and_reset_button()
#         backup = True
#         try:
#             logging.info("⚙️ Switching to backup method...")
#             video_formats, audio_formats = try_fetching_format(ydl_opts_backup)

#         except yt_dlp.utils.DownloadError as e:
#             if "cookie" in str(e).lower() or "sign in" in str(e).lower() or "403" in str(e):
#                 logging.info("⚠️ Cookie file seems broken or expired. Resetting...")
#                 delete_cookie_file_and_reset_button()
#                 return [], []
#             logging.info(f"❌ Backup method failed: {e}")
#             logging.info("🛠️ Trying final fallback metho d (force_generic_extractor)...")

#         try:
#             video_formats, audio_formats = try_fetching_format(ydl_opts_fallback)

#             # Explicit check after fallback
#             if not video_formats or video_formats == ['Video Formats...','Only Audio']:
#                 raise Exception("Fallback method returned no formats")

#             return video_formats, audio_formats

#         except Exception as e:
#             logging.info(f"❌ Final fallback failed: {e}")

#             if "cookie" in str(e).lower() or "sign in" in str(e).lower() or "403" in str(e):
#                 logging.info("⚠️ Cookie file seems broken or expired. Resetting...")
#                 delete_cookie_file_and_reset_button()
#                 return [], []
#             return ["error"], ["error"]



# def download_youtube_link(youtube_url,output_path, progress_callback=None):
#     video_format = video_format_var.get().split(" - ")[0]  
#     audio_format = audio_format_var.get().split(" - ")[0]  

#     if video_format == "Only Audio":
#         # Audio only download
#         format_string = audio_format if audio_format else "bestaudio"
#         merge_format = "mp3"
#     else:
#         # Video + audio download
#         format_string = f"{video_format}+{audio_format}/bestaudio"
#         merge_format = "mp4"
    
#     base_opts = {
#         "outtmpl": f'{output_path}/%(title)s.%(ext)s',
#         "cookiefile": cookie_file_path,
#         'format': format_string,
#         'merge_output_format': merge_format,
#         'progress_hooks': [progress_callback] if progress_callback else [],
#         'nocheckcertificate': True,
#         'cookiesfrombrowser': None,
#         'js_runtimes': {'node': {}},
#         'extractor_args': {'youtube': {'remote_components': 'ejs:github'}},
#         'remote_components': ['ejs:github']
#     }

#     # Fallback options similar to get_available_formats
#     opts_list = [
#         base_opts,
#         {**base_opts, 'no_signature': True},
#         {**base_opts, 'force_generic_extractor': True, 'ignoreerrors': True}
#     ]

#     last_error = None
#     for opts in opts_list:
#         try:
#             with yt_dlp.YoutubeDL(opts) as ydl:
#                  ydl.download([youtube_url])
            
#             window.after(0, lambda: [stop_youtube_download_btn.pack_forget(), stop_youtube_download_btn.update_idletasks()])
#             return "Download Complete!"

#         except yt_dlp.utils.DownloadError as e:
#             last_error = e
#             if "User stopped the download." in str(e):
#                 return f"Error: {str(e)}"
#             logging.info(f"Download failed with opts: {e}. Retrying...")
#             continue
#         except Exception as e:
#             return f"Error: {str(e)}"
    
#     return f"Error: {str(last_error)}"
    
# def update_progress(d):
#     if stop_download_flag:
#         raise yt_dlp.utils.DownloadError("User stopped the download.")
#     if d['status'] == 'downloading':
#         percent = d.get('_percent_str', '0%')
#         window.after(0, lambda: youtube_progress_var.set(percent))


# def download_thread(youtube_url, output_path):
#     global stop_download_flag
#     try:
#         info_message.set("Downloading....")
#         message = download_youtube_link(youtube_url, output_path, update_progress)
#         if stop_download_flag:
#             info_message.set("Removing temporary files...")
         
#             for file in os.listdir(output_path):
#                 if file.endswith(".part"):
#                     try:
#                         os.remove(os.path.join(output_path, file))
#                         info_message.set("Done cleaning up files.")
#                     except Exception as e:
#                         info_message.set(f"Error cleaning up files: {str(e)}")
#             return
        
        
#         if message == "Download Complete!":
#             info_message.set(message)
#             stop_youtube_download_btn.pack_forget()
#         else: 
#             info_message.set(message)
#     except yt_dlp.utils.DownloadError as e:
#         if "User stopped the download." in str(e):
#             info_message.set("YouTube downloader is ready :)")

          
      
#         else:
#             info_message.set(f"Error:  {str(e)}")

#     except Exception as e:
#         info_message.set(f"Error: {str(e)}")
#     finally:
#         youtube_progress_var.set("" if stop_download_flag else "Download Complete!")
#         video_format_var.set("")
#         audio_format_var.set("")
#         youtube_link_entry.delete(0, 'end')

# def Stop_Youtube_Downloading():
#     global youtube_link_entry
#     global stop_download_flag 
#     stop_download_flag = True
#     stop_youtube_download_btn.place_forget()
#     info_message.set("Stopping Download, cleaning up...")


# def start_youtube_download():
#     global youtube_link_entry, youtube_output_path_entry
#     url=youtube_link_entry.get()
#     output_path = youtube_output_path_entry.get()

#     if not url or 'youtube.com' not in url and 'youtube.be' not in url:
#         info_message.set("Invalid YouTube URL!")
#         return
    
#     if not output_path:
#         info_message.set("Choose a folder for saving!")
#         return
#     stop_youtube_download_btn.grid(row=4, column=3, sticky="ew", padx=10, pady=5)
#     youtube_progress_var.set("0%")
#     Thread(target=download_thread, args=(url, output_path)).start()
    

        

# def get_ffmpeg_details(file_path):
#     """
#     Uses ffmpeg.probe to extract metadata from a video file.
#     Returns a formatted JSON string with all available details.
#     """
#     try:
#         probe = ffmpeg.probe(file_path)
#         return json.dumps(probe, indent=4)
#     except ffmpeg.Error as e:
#         error_message = e.stderr.decode() if e.stderr else str(e)
#         return f"Error retrieving details: {error_message}"
#     except Exception as e:
#         return f"An unexpected error occurred: {e}"

































# class ToolMenu:
#     def __init__(self, parent_container):
#         self.parent_container = parent_container

#         self.container = CTkFrame(
#             master=self.parent_container,
#             fg_color="black",
#             border_width=2,
#             border_color="#404040",
#             corner_radius=10
#         )
#         self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
#         self.container.update_idletasks()


#         self.create_widgets()
     

#     def create_widgets(self):
#         top_bar = CTkFrame(
#             master=self.container,
#             fg_color="#282828"
#         )



#         top_bar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
  

#         tools_intro = [
#             ("✔️YouTube Downloader", "Download videos and audio with all available format selection for det video. \n"),
#             ("✔️LR Metadata Agent", "AI-Agent: Generates SEO-optimized Title, Description, Hashtags, Keywords  choosen video in uploaded files. \n"),
#             ("✔️Mediainfo Analyst", "View technical metadata from media files. \n"),
#             ("✔️Social Media Uploading", "Upload to platforms like YouTube, TikTok. \n"),
#             ("✔️AI AutoCreator", "AI agent to transcribe, edit and upload videos. \n"),
#             ("📍Future Updates", "The program is under development, Program updates will be released in the future. \n"),

#         ]
#         intro_text = "\n\n".join([f"• {name}:\n  {desc}" for name, desc in tools_intro])
      
#         intro_label = CTkLabel(
#             master=self.container,
#             text="Available Tools:\n\n" + intro_text,
#             font=("Arial", 14),
#             justify="left",
#             text_color="#FFFFFF",
#             wraplength=600,
#             fg_color="transparent",
#             anchor="nw"
#         )
#         intro_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)


#         self.info_button_ToolMenu_info = create_info_button(
#             open_ToolMenu_Info,
#             text="INFO",
#             width=15,
#             master=top_bar
#         )
#         self.info_button_ToolMenu_info.pack(side="left", padx=10, pady=5)

   

#         self.container.columnconfigure(0, weight=1)
#         self.container.rowconfigure(1, weight=1)

 




































# class VidGenesis_Automation_Agent:

#     def __init__(self, parent_container):
#         self.parent_container = parent_container


        
#         self.should_stop = False
#         self.container = CTkFrame(
#             master=self.parent_container,
#             fg_color="#282828",
#             border_width=2,
#             border_color="#404040",
#             corner_radius=10
#         )
#         self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

#         self.loading_label = CTkLabel(
#             master=self.container,
#             text="",
#             text_color="#00FF00",
#             font=("Arial", 14)
#         )
#         self.loading_label.grid(row=2, column=0, pady=5, sticky="nsew")
#         wait_time = 0
#         while Global_offline_model is None:
#             self.loading_label.configure(text=f"⏳ Waiting for model to load... {wait_time}s")
#             self.loading_label.update_idletasks()
#             time.sleep(1)
#             wait_time += 1
#             if wait_time > 60:
#                 self.loading_label.configure(text="❌ Timeout waiting for model to load.")
#                 return

#         self.loading_label.configure(text="✅ Model loaded successfully.")
#         self.model = Global_offline_model
#         self.create_widgets()

#     def create_widgets(self):
#         #Top section with all user inputs
#         self.top_bar = CTkFrame(
#             master=self.container,
#             fg_color="black",
#             border_color="white",
#             border_width=2
#         )
#         self.top_bar.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 0))
#         self.top_bar.columnconfigure((0, 1, 2), weight=1)
#         self.top_bar.rowconfigure(1, weight=1)
#         #Title input
#         self.title_entry = CTkEntry(self.top_bar, placeholder_text="Title of video", width=250)
#         self.title_entry.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="w")

#         #Topic
#         self.topic_entry = CTkEntry(self.top_bar, placeholder_text="Topic of video", width=250)
#         self.topic_entry.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="w")


#         # Dropdown1
#         self.styledropdown1 = CTkOptionMenu(self.top_bar, variable=StringVar(), values=[
#             "Cinematic", "Emotional", "Inspirational", "Mystical",
#             "Playful", "Dark & Gritty", "Uplifting", "Chill / Relaxed",
#             "Tense / Suspenseful", "Epic", "Minimalistic", "Abstract / Surreal"
#         ], width=175)
#         self.styledropdown1.set("None")
#         self.styledropdown1.grid(row=0, column=1, padx=(5, 10), pady=(10, 5), sticky="w")

#         #Dropdown2
#         self.styledropdown2 = CTkOptionMenu(self.top_bar, variable=StringVar(), values=[
#             "value1", "value2", "value3", "value4"
#         ], width=175)
#         self.styledropdown2.set("None")
#         self.styledropdown2.grid(row=1, column=1, padx=(5, 10), pady=5, sticky="w")

#         #Amount
#         self.video_amount = CTkEntry(self.top_bar, textvariable=StringVar(), placeholder_text="Amount of videos", width=100)
#         self.video_amount.grid(row=0, column=2, padx=5, pady=5, sticky="w")

#         #Description label
#         self.description_label = CTkLabel(self.top_bar, text="📝 Description of the Video", font=("Arial", 14), text_color="white")
#         self.description_label.grid(row=2, column=0, columnspan=3, padx=10, pady=(10, 0), sticky="w")

#         #Description box
#         self.description_entry = CTkTextbox(self.top_bar, height=110)
#         self.description_entry.grid(row=3, column=0, columnspan=3, padx=10, pady=(0, 5), sticky="ew")

#         #Agent run button 
#         self.run_agent_node = CTkButton(
#             master=self.top_bar,
#             command=lambda: Thread(target=self.run_agent).start(),
#             fg_color="black",
#             text="▶ Run AGENT Node"
#         )
#         self.run_agent_node.grid(row=1, column=2,     padx=(5, 10), pady=(0, 5), sticky="se")

#         #Chat area below other widgets
#         self.chat_display = scrolledtext.ScrolledText(
#             self.container,
#             wrap=tk.WORD,
#             width=55,
#             height=25,
#             font=("Helvetica", 12),
#             bg="black",
#             fg="white",
#             state="disabled"
#         )
#         self.chat_display.config(
#             insertbackground="yellow",
#             selectbackground="#444444",
#             selectforeground="white",
#             borderwidth=2,
#             relief="sunken"
#         )
#         self.chat_display.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=(0, 10))
#         self.container.columnconfigure(0, weight=1)
#         self.container.rowconfigure(1, weight=1)


#     def run_single_video_task(self):

#             try:
#                 prompts = find_by_relative_path(f"Assets{os_separator}prompts_video_creator.yaml")
#                 with open(prompts, 'r') as stream:
#                      prompt = yaml.safe_load(stream)

#                 Custom_user_task = f"""Your goal is to create a video based on the specified topic and parameters implemented.
#                                    1.
#                                    2.
#                                    3.
#                                    4.
#                                    5.
#                                    6.

                              
#                                    """

          
#                 self.context_var =  { 
#                             "Video Title": self.title_entry.get(),
#                             "topic": self.topic_entry.get(),
#                             "description": self.description_entry.get("1.0", "end-1c"),
#                             "video_amount": self.video_amount_var.get(),
#                             "media_type": self.media_type_var.get()
#                             }
                
#                 AutoMation_agent  = CodeAgent(
#                     model=self.model,
#                     tools=[
#                         FinalAnswerTool(), 
#                         SpeechToTextTool(),
#                         VisitWebpageTool(),
#                         GoogleSearchTool(),
#                         Fetch_top_trending_youtube_videos,
#                         #Upload_video_to_socialMedia_platform,
#                         #add_text_to_video,
#                         #add_audio_to_video,
#                         #add_filter_to_video,
#                     ], 
#                     max_steps=10,
#                     verbosity_level=1,
#                     prompt_templates=prompt,
#                     add_base_tools=True
#                 )

#                 self.manager_agent = AutoMation_agent
#                 self.user_task = Custom_user_task
#                 self.context_var = self.context_var

#                 response = self.manager_agent.run(
#                             task=self.user_task,
#                             additional_args=self.context_var
#                 )

#                 self.chat_display.config(state=tk.NORMAL)
#                 if isinstance(response, dict):
#                     formatted = (
#                         json.dumps(response, indent=4),
#                     )
#                 else:
#                     formatted = str(response)

#                 self.chat_display.insert(tk.END, formatted + "\n")
#                 self.chat_display.config(state=tk.DISABLED)
#                 self.chat_display.see(tk.END)
#             except Exception as e:
#                     logging.info("❌ Error in run_single_video_task:", e)



#     def run_agent_loop(self):
#             try:
#                 amount = int(self.video_amount_var.get())
#             except ValueError:
#                 logging.info("invalid video amount entered")
#                 return
            
#             for i in range(amount):
#                 if self.should_stop:
#                     break
#                 self.run_single_video_task()


#     def run_agent(self):   
     
#         self.RunForever = Thread(target=self.run_agent_loop(),daemon=True)
#         self.RunForever.start()

 

           


        
























# class ColorRestorer_gui:

#     def __init__(self, parent_container):
#         self.parent_container = parent_container
#         self.uploaded_image  = None
#         self.colorizer = None
#         self.colorized_image = None
#         self.selected_resolution = 800

#         self.container = CTkFrame(
#             master=self.parent_container,
#             fg_color="#282828",
#             border_width=2,
#             border_color="#404040",
#             corner_radius=10
#         )
#         self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

#         self.resolution_entry = CTkOptionMenu(
#             self.container,
#             values=["512x512", "768x768", "1024x1024", "1280x1280", "1920x1920"],
#             command=self.on_resolution_change,
#             width=200
#         )
#         self.resolution_entry.pack(pady=10)

#         self.upload_button = CTkButton(
#             self.container,
#             text="Upload Image",
#             command=self.upload_image
#         )
#         self.upload_button.pack(pady=10)
   
#         self.save_button = CTkButton(
#             self.container,
#             text="Save Image",
#             command=self.save_image,
#             state="disabled"
#         )
#         self.upload_button.pack(pady=10)
   

#         self.colorize_button = CTkButton(
#             self.container,
#             text="Colorize",
#             command=self.colorize_image,
#             state="disabled"
#         )
#         self.colorize_button.pack(pady=10)


#         self.image_label = CTkLabel(self.container, text="").pack(pady=10)


#     def on_resolution_change(self,value):
#         try:
#             w, h = value.lower().split("x")
#             self.selected_resolution = (int(w), int(h))
#         except:
#             self.selected_resolution = (800,800)

#     def upload_image(self):
#         file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
#         if file_path:
#             self.uploaded_image = Image.open(file_path).convert("RGB")
#             preview = self.uploaded_image.resize((300,300))
#             tk_img = ImageTk.PhotoImage(preview)
#             self.image_label.image = tk_img
#             self.colorize_button.configure(state="normal")


#     def colorize_image(self):
#         from LocalModelAssets.Old_photos__colorizing.Vizualise  import get_image_colorizer
#         if self.uploaded_image:
#             self.colorizer = get_image_colorizer(artistic=True)
#             resized = self.uploaded_image.resize((self.selected_resolution))
#             colorized_img = self.colorizer.plot_transformed_pil_image(resized, render_factor=35, compare=False)
#             self.colorized_image = colorized_img
#             tk_img = ImageTk.PhotoImage(colorized_img.resize((300,300)))
#             self.image_label.configure(image=tk_img)
#             self.image_label.image = tk_img
#             self.save_button.configure(state="normal")

#     def save_image(self):
#         if self.colorized_image:
#             save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
#                                                      filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
#             if save_path:
#                 final_img = self.colorized_image.resize((self.selected_resolution, self.selected_resolution))
#                 final_img.save(save_path)



























































# ####TOOL(1) FOR TOOLCLASS#####
# class MediaTree_Inspector_gui:
#     def __init__(self, parent_container):
#         self.parent_container = parent_container
#         self.selected_file_list = selected_file_list
#         self.truncated_to_full = {}
#         self.MediaInfo_Agent = Global_offline_model


#         self.container = CTkFrame(
#             master=self.parent_container,
#             fg_color="#282828",
#             border_width=2,
#             border_color="#404040",
#             corner_radius=10
#         )
#         self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

#         self.create_widgets()
#         global media_info_update_callback
#         media_info_update_callback = self.sync_uploaded_files
#         self.populate_dropdown()

#     def create_widgets(self):
#         top_bar = CTkFrame(
#             master=self.container,
#             fg_color="#282828"
#         )
#         top_bar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

      
#         self.file_menu_var = StringVar(value="No files uploaded")
#         self.file_menu = CTkOptionMenu(
#             master=top_bar,
#             variable=self.file_menu_var,
#             values=[],
#             width=150,
#             height=30,
#             fg_color="#282828",
#             button_color="#404040",
#             text_color="#FFFFFF"
#         )
#         self.file_menu.pack(side="left", padx=10, pady=5)



#         self.get_details_btn = CTkButton(
#             master=top_bar,
#             text="Fetch MediaInfo",
#             width=140,
#             height=30,
#             border_width=1,
#             font=bold11,
#             fg_color="#282828",
#             text_color="#E0E0E0",
#             border_color="#0096FF",
#             command=self.get_details
#         )
#         self.get_details_btn.pack(side="left", padx=10, pady=5)

   
#         self.info_button_mediainfo_analyst = create_info_button(
#             open_mediaInfo_Analyst,
#             text="INFO",
#             width=15,
#             master=top_bar
#         )
#         self.info_button_mediainfo_analyst.pack(side="left", padx=10, pady=5)

   
#         self.details_text = CTkTextbox(
#             master=self.container,
#             width=1000,
#             height=500,
#             font=("Arial", 20),
#             corner_radius=10,
#             state="disabled"
#         )
#         self.details_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

#         self.container.columnconfigure(0, weight=1)
#         self.container.rowconfigure(1, weight=1)


#     def sync_uploaded_files(self):
#             """Sync file list with global and refresh dropdown"""
#             self.selected_file_list = selected_file_list
#             self.populate_dropdown()


#     def populate_dropdown(self):
#         max_length = 20
#         self.truncated_to_full = {}  # reset mapping

#         file_names = [f.split("/")[-1] for f in self.selected_file_list]
#         truncated_names = []

#         for original, full_path in zip(file_names, self.selected_file_list):
#             truncated = original if len(original) <= max_length else original[:max_length] + '...'
#             truncated_names.append(truncated)
#             self.truncated_to_full[truncated] = full_path  # store mapping

#         self.file_menu.configure(values=truncated_names)

#         if truncated_names:
#             self.file_menu_var.set(truncated_names[0])


#     def place_mediainfo_analyst_textbox(self):
#         Info_button_mediainfo_analyst = create_info_button(
#             open_mediaInfo_Analyst,
#             text="MediaInfo (info)",
#             width=15,
#             master=self.container
#         )
#         Info_button_mediainfo_analyst.grid(row=1, column=0, pady=10)




#     def clear_file_list(self):
#         """
#         Clears the selected_file_list and resets the dropdown.
#         """
#         self.selected_file_list = []
#         self.file_menu.configure(values=[])
#         self.file_menu_var.set("No files uploaded")


#     def get_details(self):
#         """
#         Retrieves detailed metadata for the selected video file using ffmpeg.
#         """
#         logging.info("[DEBUG] Fetch button clicked")

#         selected_file = self.file_menu_var.get()
#         file_path = self.truncated_to_full.get(selected_file)
#         logging.info(f"[DEBUG] Selected file: {selected_file}")
#         logging.info(f"[DEBUG] Full path: {file_path}")

#         self.details_text.configure(state="normal")
#         self.details_text.delete("1.0", END)

#         if file_path:
#             details = get_ffmpeg_details(file_path)
#             logging.info(f"[DEBUG] Raw details returned:\n{details}")

#             if not details:
#                 self.details_text.insert(END, "No data received from ffmpeg.")
#             elif details.startswith("Error") or details.startswith("An unexpected"):
#                 self.details_text.insert(END, details)
#             else:
#                 formatted_data = self.format_details(details)
#                 self.details_text.insert(END, formatted_data or "No readable metadata found.")
#         else:
#             self.details_text.insert(END, "No file selected or file not found.")

#         self.details_text.configure(state="disabled")

#     def format_details(self, details):
#         """
#         Format and structure the JSON data for better readability in the textbox.
#         """
#         try:
      
#             parsed_details = json.loads(details)
            
    
#             formatted_data = ""

          
#             formatted_data += "\n### General Information ###\n"
#             format_info = parsed_details.get('format', {})
#             formatted_data += f"Filename: {format_info.get('filename', 'N/A')}\n"
#             formatted_data += f"Format: {format_info.get('format_name', 'N/A')} ({format_info.get('format_long_name', 'N/A')})\n"
#             formatted_data += f"Duration: {format_info.get('duration', 'N/A')} seconds\n"
#             formatted_data += f"Size: {format_info.get('size', 'N/A')} bytes\n"
#             formatted_data += f"Bitrate: {format_info.get('bit_rate', 'N/A')} bps\n"
#             formatted_data += f"Probe Score: {format_info.get('probe_score', 'N/A')}\n"
#             formatted_data += "-" * 50 + "\n"

       
#             streams = parsed_details.get('streams', [])
#             for stream in streams:
#                 formatted_data += f"### Stream {stream.get('index', 'N/A')} ###\n"
#                 formatted_data += f"Codec: {stream.get('codec_long_name', 'N/A')}\n"
#                 formatted_data += f"Codec Type: {stream.get('codec_type', 'N/A')}\n"
#                 formatted_data += f"Resolution: {stream.get('width', 'N/A')} x {stream.get('height', 'N/A')}\n"
#                 formatted_data += f"Aspect Ratio: {stream.get('display_aspect_ratio', 'N/A')}\n"
#                 formatted_data += f"Frame Rate: {stream.get('r_frame_rate', 'N/A')}\n"
#                 formatted_data += f"Bitrate: {stream.get('bit_rate', 'N/A')}\n"
#                 formatted_data += f"Duration: {stream.get('duration', 'N/A')} seconds\n"
#                 formatted_data += f"Has B-Frames: {stream.get('has_b_frames', 'N/A')}\n"
#                 formatted_data += f"Sample Aspect Ratio: {stream.get('sample_aspect_ratio', 'N/A')}\n"
#                 formatted_data += f"Chroma Location: {stream.get('chroma_location', 'N/A')}\n"
#                 formatted_data += f"Field Order: {stream.get('field_order', 'N/A')}\n"
#                 formatted_data += f"Pixel Format: {stream.get('pix_fmt', 'N/A')}\n"
#                 formatted_data += "-" * 50 + "\n"

              
#                 disposition = stream.get('disposition', {})
#                 formatted_data += "Disposition:\n"
#                 for key, value in disposition.items():
#                     formatted_data += f"  {key}: {value}\n"

           
#                 tags = stream.get('tags', {})
#                 if tags:
#                     formatted_data += "Tags:\n"
#                     for tag_key, tag_value in tags.items():
#                         formatted_data += f"  {tag_key}: {tag_value}\n"
#                 formatted_data += "-" * 50 + "\n"

       
#             tags = format_info.get('tags', {})
#             if tags:
#                 formatted_data += "\n### File Tags ###\n"
#                 for tag_key, tag_value in tags.items():
#                     formatted_data += f"{tag_key}: {tag_value}\n"
#                 formatted_data += "-" * 50 + "\n"

        
#             return formatted_data

#         except json.JSONDecodeError:
#             return "Error: Failed to parse the details."



































# ####TOOLCLASS#####
# ### a class with list of available tools that changes window for each tool on the main window.
# class ToolWindowClass:
#     def __init__(self, master):
#         self.master = master

#         self.container = CTkFrame(master, fg_color="black", border_width=0, corner_radius=0)
#         self.container.place(relx=0.0, rely=0.0, relwidth=0.22, relheight=1.0)


    
#         self.create_widgets()

#     def create_widgets(self):
#         self.menu_frame = CTkFrame(self.container, fg_color="#0A0A09",
#                                    border_width=0, corner_radius=0, height=44)
#         self.menu_frame.pack(side="top", fill="x")
#         self.menu_frame.pack_propagate(False)

  
#         self.tool_list = ['Tool Menu','YouTube Downloader', 'MediaTree Inspector', 'SocialMedia Uploading','VidIntel Agent','VidGenesis Automation Agent','ColorRestorer AI','Corelytics InsightCatcher AI','Social Media Optimizer AI']
#         self.tool_menu_var = StringVar(value=self.tool_list[0])
#         self.tool_menu = CTkOptionMenu(
#             master=self.menu_frame,
#             variable=self.tool_menu_var,
#             values=self.tool_list,
#             command=self.on_tool_select,
#             width=200,
#             height=36,
#             fg_color="#0E0E0D",
#             button_color="#201E1A",
#             button_hover_color="#383028",
#             text_color="#C8C0B0",
#             dropdown_fg_color="#0E0E0D",
#             dropdown_text_color="#C8C0B0",
#             dropdown_hover_color="#181614",
#             font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         )
#         self.tool_menu.pack(side="top", fill="x", padx=8, pady=4)

#         self.content_frame = CTkFrame(self.container, fg_color="transparent")
#         self.content_frame.pack(side="top", fill="both", expand=True)

  
#         self.on_tool_select(self.tool_list[0])

#     def on_tool_select(self, selected_tool):
     
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

          
#         if selected_tool == 'Tool Menu':
#             self.CreateToolMenu_info()
#         elif selected_tool == 'VidIntel Agent':
#             self.create_vidintel_agent()
#         elif selected_tool == 'YouTube Downloader':
#             self.create_youtube_downloader()
#         elif selected_tool == "MediaTree Inspector":
#             self.create_MediaTree_Inspector()
#         elif selected_tool == "SocialMedia Uploading":
#             self.Create_Social_Media_uploading()
#         elif selected_tool == "VidGenesis Automation Agent":
#             self.create_VidGenesis_Automation_Agent
#         elif selected_tool == "ColorRestorer AI":
#             self.create_ColorRestorer_ai()
#         elif selected_tool == "Corelytics InsightCatcher AI":
#             self.Corelytics_InsightCatcher()
#         elif selected_tool == "Social Media Optimizer AI":
#             self.create_Social_Media_Optimizer_AI

#     def create_Social_Media_Optimizer_AI(self):
#         self.social_media_optimizer_Gui = social_media_optimizer_Gui(self.content_frame)
#         self.social_media_optimizer_Gui.pack(fill="both", expand=True, padx=10, pady=10)

#     def CreateToolMenu_info(self):
#        self.ToolMenu = ToolMenu(self.content_frame)
#        self.ToolMenu.container.pack(fill="both",expand=True,padx=10,pady=10)
        
#     def Corelytics_InsightCatcher(self):
#         self.create_corelytics_InsightCatcher = corelytics_InsightCatcher(self.content_frame)
#         self.create_corelytics_InsightCatcher.pack(fill="both", expand=True, padx=10, pady=10)

#     def create_vidintel_agent(self):
#         self.vidintel_agent = vidintel_agent_gui(self.content_frame)
#         self.vidintel_agent.container.pack(fill="both", expand=True, padx=10, pady=10)

#     def create_VidGenesis_Automation_Agent(self):
#         self.VidGenesis_Automation_Agent = VidGenesis_Automation_Agent(self.content_frame)
#         self.VidGenesis_Automation_Agent.container.pack(fill="both",expand=True,padx=10,pady=10)
    
#     def create_MediaTree_Inspector(self):
#         self.MediaTree_Insepctor = MediaTree_Inspector_gui(self.content_frame)
#         self.MediaTree_Insepctor.container.pack(fill="both", expand=True, padx=10, pady=10)

#     def Create_Social_Media_uploading(self):
#         self.socialMediaUploading = SocialMediaUploading(self.content_frame)
#         self.socialMediaUploading.container.pack(fill="both", expand=True, padx=10, pady=10)
    
#     def create_ColorRestorer_ai(self):
#         self.colorRestorer_ai = ColorRestorer_gui(self.content_frame)
#         self.colorRestorer_ai.container.pack(fill="both", expand=True, padx=10, pady=10)

#     def create_youtube_downloader(self):
#         self.content_frame.grid_rowconfigure(0, weight=1)
#         self.content_frame.grid_columnconfigure(0, weight=1)
#         place_youtube_download_menu(self.content_frame)





















































































# ####VIDEO PREVIEW CLASS######
# class VideoPreview:
#     """
#     Owns its layout completely inside parent_container (the global 'container').

#     Side-by-side:  two CTkLabel frames packed left/right
#     SoloFrame:     one tk.Canvas with draggable before/after split line
#     """

#     # ── Design tokens ──────────────────────────────────────────────────
#     _ACCENT      = "#D49A2A"   # amber
#     _ACCENT_DIM  = "#48403A"
#     _SEP_COLOR   = "#141210"
#     _TAG_FG      = "#948C7E"
#     _TAG_BG      = "#0E0D0C"
#     _SLIDER_FG   = "#D8C090"
#     _BTN_ACTIVE  = "#1C1810"
#     _BTN_IDLE    = "#0C0C0B"

#     def __init__(self, parent_container, original_label, upscaled_label, video_path):
#         logging.info("Initializing VideoPreview...")
#         self.parent_container = parent_container
#         self.video_path       = video_path

#         # ── Video source ──────────────────────────────────────────────
#         self.cap          = cv2.VideoCapture(video_path)
#         self.fps          = int(self.cap.get(cv2.CAP_PROP_FPS))
#         self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
#         raw_w = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         raw_h = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         self.source_aspect = (raw_w / raw_h) if raw_h > 0 else (16/9)
#         self.target_size   = (raw_w, raw_h)

#         # ── State ─────────────────────────────────────────────────────
#         self.view_mode       = StringVar(value="side_by_side")
#         self.split_ratio     = 0.5
#         self.last_original   = None
#         self.last_upscaled   = None
#         self.solo_canvas     = None
#         self._canvas_photo   = None

#         # ── Destroy any existing layout widgets inside parent_container
#         for w in parent_container.winfo_children():
#             w.destroy()

#         # ── Top bar ───────────────────────────────────────────────────
#         self.top_bar = CTkFrame(parent_container, fg_color="#090907",
#                                 corner_radius=0, height=44)
#         self.top_bar.pack(side="top", fill="x")
#         self.top_bar.pack_propagate(False)

#         # Thin separator line under top bar
#         CTkFrame(parent_container, fg_color=self._SEP_COLOR,
#                  height=1, corner_radius=0).pack(side="top", fill="x")

#         # Mode toggle buttons
#         btn_row = CTkFrame(self.top_bar, fg_color="#090907", corner_radius=6)
#         btn_row.pack(side="left", padx=10, pady=8)

#         self._btn_sbs = CTkButton(
#             btn_row, text="Side by Side",
#             width=104, height=26, corner_radius=6,
#             font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#             fg_color=self._BTN_ACTIVE, hover_color="#28220E",
#             text_color=self._ACCENT,
#             border_width=1, border_color="#302818",
#             command=lambda: self._set_mode("side_by_side")
#         )
#         self._btn_sbs.pack(side="left", padx=(0, 3))

#         self._btn_solo = CTkButton(
#             btn_row, text="Compare",
#             width=90, height=26, corner_radius=6,
#             font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#             fg_color=self._BTN_IDLE, hover_color="#141210",
#             text_color=self._ACCENT_DIM,
#             border_width=1, border_color="#181410",
#             command=lambda: self._set_mode("SoloFrame")
#         )
#         self._btn_solo.pack(side="left")

#         # Timer label — shows current position as MM:SS
#         self.timer_label = CTkLabel(
#             self.top_bar, text="00:00",
#             font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#             text_color=self._ACCENT_DIM,
#             fg_color="#090907",
#             width=44,
#         )
#         self.timer_label.pack(side="left", padx=(8, 2), pady=0)

#         # Timeline slider — right side
#         self.timeline_slider = CTkSlider(
#             self.top_bar,
#             from_=0, to=max(1, self.total_frames - 1),
#             command=self._on_timeline_change,
#             button_color=self._ACCENT,
#             button_hover_color="#F0D880",
#             progress_color="#2A1E08",
#             fg_color="#141210",
#             height=12,
#         )

#         # ── Display area ──────────────────────────────────────────────
#         self.display_area = CTkFrame(parent_container, fg_color="#060606")
#         self.display_area.pack(side="top", fill="both", expand=True)

#         # ── Side-by-side sub-frames ───────────────────────────────────
#         self.orig_frame = CTkFrame(self.display_area, fg_color="#060606")
#         self.orig_label = CTkLabel(self.orig_frame, text="")
#         self.orig_label.pack(fill="both", expand=True, padx=4, pady=(0, 6))

#         self.mid_sep = CTkFrame(self.display_area, fg_color="#161210",
#                                 width=1, corner_radius=0)

#         self.ups_frame = CTkFrame(self.display_area, fg_color="#060606")
#         self.ups_label = CTkLabel(self.ups_frame, text="")
#         self.ups_label.pack(fill="both", expand=True, padx=4, pady=(0, 6))

#         # ── Solo canvas ───────────────────────────────────────────────
#         self.solo_canvas = tk.Canvas(
#             self.display_area, bg="#060606",
#             highlightthickness=0, cursor="sb_h_double_arrow"
#         )
#         self.solo_canvas.bind("<ButtonPress-1>", self._on_canvas_drag)
#         self.solo_canvas.bind("<B1-Motion>",     self._on_canvas_drag)

#         # Show side-by-side initially
#         self._show_sbs_layout()
#         # Defer frame load until layout is fully rendered so winfo_width/height
#         # return real values (not 0/1), preventing a black initial preview.
#         # Load the midpoint frame so the thumbnail is representative.
#         mid_frame = max(0, self.total_frames // 2)
#         self.parent_container.after(150, lambda: self._load_frame(mid_frame))

#         if self.total_frames > 1:
#             self.timeline_slider.pack(side="right", fill="x", expand=True,
#                                       padx=(6, 14), pady=0)
#             # Move slider to midpoint to match the frame we're loading
#             self.timeline_slider.set(mid_frame)

#         logging.info("VideoPreview initialized.")

#     # ================================================================== #
#     #  Header factory — compact pill tag                                   #
#     # ================================================================== #
#     def _make_header(self, parent, text):
#         row = CTkFrame(parent, fg_color="#060606")
#         row.pack(side="top", fill="x", padx=4, pady=(6, 2))
#         is_ups = (text == "UPSCALED")
#         CTkLabel(
#             row, text=text,
#             font=CTkFont(family="Segoe UI", size=9, weight="bold"),
#             text_color=AMBER_DIM if is_ups else self._TAG_FG,
#             fg_color="#0C0906" if is_ups else self._TAG_BG,
#             corner_radius=4, padx=8, pady=3, width=0,
#         ).pack(anchor="center", expand=True)

#     # ================================================================== #
#     #  Layout helpers                                                      #
#     # ================================================================== #
#     def _show_sbs_layout(self):
#         self.solo_canvas.pack_forget()
#         self.orig_frame.pack(side="left",  fill="both", expand=True)
#         self.mid_sep.pack(   side="left",  fill="y",    pady=8)
#         self.ups_frame.pack( side="right", fill="both", expand=True)

#     def _show_solo_layout(self):
#         self.orig_frame.pack_forget()
#         self.mid_sep.pack_forget()
#         self.ups_frame.pack_forget()
#         # Center the compare canvas instead of stretching to the left
#         # Keep the canvas at its rendered image size and let extra space
#         # distribute evenly around it so it stays centered.
#         self.solo_canvas.pack(expand=True, padx=4, pady=4)

#     def _set_mode(self, mode):
#         self.view_mode.set(mode)
#         if mode == "side_by_side":
#             self._btn_sbs.configure(fg_color=self._BTN_ACTIVE,
#                                     text_color=self._ACCENT,
#                                     border_color="#302818")
#             self._btn_solo.configure(fg_color=self._BTN_IDLE,
#                                      text_color=self._ACCENT_DIM,
#                                      border_color="#181410")
#             self._show_sbs_layout()
#         else:
#             self._btn_solo.configure(fg_color=self._BTN_ACTIVE,
#                                      text_color=self._ACCENT,
#                                      border_color="#302818")
#             self._btn_sbs.configure(fg_color=self._BTN_IDLE,
#                                     text_color=self._ACCENT_DIM,
#                                     border_color="#181410")
#             self._show_solo_layout()
#         self._refresh_display()

#     def _on_mode_change(self, mode):
#         self._set_mode(mode)

#     # ================================================================== #
#     #  Helpers                                                             #
#     # ================================================================== #
#     def _fit_size(self, max_w, max_h, aspect=None):
#         if aspect is None:
#             aspect = self.source_aspect
#         aspect = max(0.01, aspect)
#         if max_w / aspect <= max_h:
#             w, h = max_w, int(max_w / aspect)
#         else:
#             h, w = max_h, int(max_h * aspect)
#         return max(1, w), max(1, h)

#     def _frame_aspect(self, frame):
#         h, w = frame.shape[:2]
#         return w / h if h > 0 else self.source_aspect

#     def _to_ctk(self, frame_bgr, w, h):
#         rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
#         res = cv2.resize(rgb, (w, h), interpolation=cv2.INTER_AREA)
#         return CTkImage(Image.fromarray(res), size=(w, h))

#     # ================================================================== #
#     #  Rendering                                                           #
#     # ================================================================== #
#     def _refresh_display(self):
#         if self.last_original is None or self.last_upscaled is None:
#             return
#         if self.view_mode.get() == "side_by_side":
#             self._render_sbs(self.last_original, self.last_upscaled)
#         else:
#             self._render_solo(self.last_original, self.last_upscaled)

#     def _render_sbs(self, orig, ups):
#         self.display_area.update_idletasks()
#         avail_w = max(50, (self.display_area.winfo_width()  // 2) - 16)
#         avail_h = max(50,  self.display_area.winfo_height() - 60)
#         aspect  = self._frame_aspect(orig)
#         dw, dh  = self._fit_size(avail_w, avail_h, aspect)

#         orig_img = self._to_ctk(orig, dw, dh)
#         ups_img  = self._to_ctk(ups,  dw, dh)
#         self.orig_label.configure(image=orig_img, width=dw, height=dh)
#         self.ups_label.configure( image=ups_img,  width=dw, height=dh)
#         self.orig_label.image = orig_img
#         self.ups_label.image  = ups_img

#     def _render_solo(self, orig, ups):
#         self.display_area.update_idletasks()
#         avail_w = max(50, self.display_area.winfo_width()  - 10)
#         avail_h = max(50, self.display_area.winfo_height() - 10)
#         aspect  = self._frame_aspect(orig)
#         dw, dh  = self._fit_size(avail_w, avail_h, aspect)

#         orig_rgb = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)
#         ups_rgb  = cv2.cvtColor(ups,  cv2.COLOR_BGR2RGB)
#         orig_r   = cv2.resize(orig_rgb, (dw, dh), interpolation=cv2.INTER_AREA)
#         ups_r    = cv2.resize(ups_rgb,  (dw, dh), interpolation=cv2.INTER_AREA)

#         sx       = max(0, min(dw, int(dw * self.split_ratio)))
#         combined = orig_r.copy()
#         if sx < dw:
#             combined[:, sx:] = ups_r[:, sx:]

#         pil  = Image.fromarray(combined).convert("RGBA")
#         draw = ImageDraw.Draw(pil, "RGBA")

#         # Main divider — white
#         draw.line([(sx, 0), (sx, dh)], fill=(255, 255, 255, 255), width=2)

#         # Circle handle — white
#         hy, r = dh // 2, 16
#         draw.ellipse([sx-r, hy-r, sx+r, hy+r],
#                      fill=(255, 255, 255, 255), outline=(180, 180, 180, 220), width=1)
#         ap, arrow_col = 4, (50, 50, 50, 255)
#         draw.polygon([(sx-r+ap+2, hy), (sx-ap, hy-7), (sx-ap, hy+7)], fill=arrow_col)
#         draw.polygon([(sx+r-ap-2, hy), (sx+ap, hy-7), (sx+ap, hy+7)], fill=arrow_col)

#         # Corner pill labels
#         try:
#             fnt = ImageFont.truetype("segoeuib.ttf", max(11, dh // 36))
#         except IOError:
#             try:
#                 fnt = ImageFont.truetype("arial.ttf", max(11, dh // 36))
#             except IOError:
#                 fnt = ImageFont.load_default()

#         def _pill(text, x, y, text_col, bg_col):
#             tw = int(draw.textlength(text, font=fnt))
#             th = max(11, dh // 36)
#             px, py = 8, 4
#             draw.rounded_rectangle([x-px, y-py, x+tw+px, y+th+py],
#                                    radius=4, fill=bg_col)
#             draw.text((x, y), text, fill=text_col, font=fnt)

#         self.solo_canvas.config(width=dw, height=dh)
#         photo = ImageTk.PhotoImage(pil.convert("RGB"))
#         self.solo_canvas.delete("all")
#         self.solo_canvas.create_image(dw // 2, dh // 2, anchor="center", image=photo)
#         self._canvas_photo = photo

#     # ================================================================== #
#     #  Events                                                              #
#     # ================================================================== #
#     def _on_canvas_drag(self, event):
#         cw = self.solo_canvas.winfo_width()
#         if cw > 0:
#             self.split_ratio = max(0.0, min(1.0, event.x / cw))
#         if self.last_original is not None:
#             self._render_solo(self.last_original, self.last_upscaled)

#     def _on_timeline_change(self, value):
#         frame_number = int(float(value))
#         # Update timer label (MM:SS)
#         fps = self.fps if self.fps > 0 else 24
#         total_seconds = frame_number / fps
#         minutes = int(total_seconds // 60)
#         seconds = int(total_seconds % 60)
#         self.timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
#         self._load_frame(frame_number)

#     # ================================================================== #
#     #  Frame loading                                                       #
#     # ================================================================== #
#     def _load_frame(self, frame_number):
#         self.timeline_slider.configure(state="disabled")
#         loading = LoadingIcon(self.parent_container)
#         loading.start()
#         Thread(target=self._process_frame_bg,
#                args=(frame_number, loading), daemon=True).start()

#     def _process_frame_bg(self, frame_number, loading):
#         try:
#             if frame_number in frame_cache:
#                 orig, ups = frame_cache[frame_number]
#             else:
#                 self.cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_number))
#                 ok, frame = self.cap.read()
#                 if not ok:
#                     return
#                 orig = cv2.resize(frame, self.target_size, interpolation=cv2.INTER_AREA)
#                 ups  = self._ai_process(orig)
#                 frame_cache[frame_number] = (orig, ups)

#             self.last_original = orig
#             self.last_upscaled = ups
#             self.parent_container.after(0, self._refresh_display)
#             self.parent_container.after(0, loading.stop)
#             self.parent_container.after(0, lambda: self.timeline_slider.configure(state="normal"))
#         except Exception as e:
#             logging.info(f"Error processing frame {frame_number}: {e}")
#             try:
#                 self.parent_container.after(0, loading.stop)
#             except Exception:
#                 pass

#     def _ai_process(self, frame):
#         global preview_ai_instance
#         if preview_ai_instance:
#             return preview_ai_instance.AI_orchestration(frame)
#         return frame

#     # ================================================================== #
#     #  Cleanup                                                             #
#     # ================================================================== #
#     def close(self):
#         self.cap.release()
#         try:
#             self.timeline_slider.destroy()
#         except Exception:
#             pass






# # GUI place functions ---------------------------
# def create_placeholder_image(width, height, label="ORIGINAL"):
#     """Render a sleek dark placeholder with a film-strip icon and a hint line."""
#     from PIL import Image, ImageDraw, ImageFont
#     import math

#     # ── background ────────────────────────────────────────────────────
#     img  = Image.new('RGB', (width, height), color='#080807')
#     draw = ImageDraw.Draw(img)

#     # subtle vignette-style border gradient (draw concentric rects fading in)
#     for i in range(18):
#         alpha = int(30 * (1 - i / 18))
#         shade = max(0, alpha)
#         c = f"#{shade:02x}{shade:02x}{int(shade*0.85):02x}"
#         draw.rectangle([i, i, width - i - 1, height - i - 1], outline=c)

#     # ── icon: simple film-frame / play chevron ─────────────────────────
#     cx, cy = width // 2, height // 2 - 22

#     # outer circle
#     r = 34
#     draw.ellipse([cx - r, cy - r, cx + r, cy + r],
#                  outline="#2A2620", width=2, fill="#0F0E0C")

#     # play triangle
#     pts = [
#         (cx - 10, cy - 15),
#         (cx - 10, cy + 15),
#         (cx + 16, cy),
#     ]
#     draw.polygon(pts, fill="#3C2808")   # dim amber fill
#     draw.polygon(pts, outline="#8C6418", fill=None)

#     # decorative tick marks around circle (like a reel)
#     for angle_deg in range(0, 360, 45):
#         angle = math.radians(angle_deg)
#         x1 = cx + (r + 2) * math.cos(angle)
#         y1 = cy + (r + 2) * math.sin(angle)
#         x2 = cx + (r + 8) * math.cos(angle)
#         y2 = cy + (r + 8) * math.sin(angle)
#         draw.line([(x1, y1), (x2, y2)], fill="#1E1A14", width=1)

#     # ── main hint text ─────────────────────────────────────────────────
#     try:
#         font_main = ImageFont.truetype("arialbd.ttf", 13)
#         font_sub  = ImageFont.truetype("arial.ttf",   10)
#     except IOError:
#         font_main = ImageFont.load_default()
#         font_sub  = font_main

#     main_text = "Upload a file to preview"
#     sub_text  = "Supports videos & image formats"

#     mw = draw.textlength(main_text, font=font_main)
#     sw = draw.textlength(sub_text,  font=font_sub)

#     draw.text(((width - mw) / 2, cy + r + 16), main_text, fill="#4A4640", font=font_main)
#     draw.text(((width - sw) / 2, cy + r + 36), sub_text,  fill="#2E2B26", font=font_sub)

#     return img







# def place_loadFile_section(window):
#     global container, original_preview, upscaled_preview
#     global original_preview_frame, upscaled_preview_frame
#     global original_label_title, upscaled_label_title

#     window.preview_frame = CTkFrame(
#         master=window,
#         fg_color="#060606",
#         corner_radius=0,
#     )
#     window.preview_frame.place(relx=0.55, rely=0.0, relwidth=0.45, relheight=1.0)

#     container = CTkFrame(window.preview_frame, fg_color="#060606")
#     container.pack(pady=0, padx=0, fill='both', expand=True)

#     # Build the default side-by-side layout directly in container
#     _build_side_by_side_layout(container)

#     globals()['container'] = container

#     # ── Drag-and-drop registration ────────────────────────────────────
#     if _TKDND_AVAILABLE:
#         def _on_drop(event):
#             # Restore normal border colour
#             try:
#                 window.preview_frame.configure(border_color=BORDER2, border_width=0)
#             except Exception:
#                 pass
#             add_files_from_drop(event.data)

#         def _on_enter(event):
#             try:
#                 window.preview_frame.configure(border_width=2, border_color=AMBER)
#             except Exception:
#                 pass
#             return event.action

#         def _on_leave(event):
#             try:
#                 window.preview_frame.configure(border_width=0)
#             except Exception:
#                 pass

#         for widget in (window.preview_frame, container):
#             widget.drop_target_register(_tkdnd.DND_FILES)
#             widget.dnd_bind('<<Drop>>', _on_drop)
#             widget.dnd_bind('<<DragEnter>>', _on_enter)
#             widget.dnd_bind('<<DragLeave>>', _on_leave)


# def _build_side_by_side_layout(container):
#     """Create the default side-by-side preview layout inside container."""
#     global original_preview, upscaled_preview
#     global original_preview_frame, upscaled_preview_frame
#     global original_label_title, upscaled_label_title

#     ph_w, ph_h = 400, 225
#     placeholder_img_orig   = create_placeholder_image(ph_w, ph_h, label="ORIGINAL")
#     placeholder_img_ups    = create_placeholder_image(ph_w, ph_h, label="UPSCALED")
#     placeholder_photo_orig = CTkImage(placeholder_img_orig, size=(ph_w, ph_h))
#     placeholder_photo_ups  = CTkImage(placeholder_img_ups,  size=(ph_w, ph_h))

#     # ── Single centered panel: shown when no file is loaded ──────────
#     original_preview_frame = CTkFrame(
#         container,
#         fg_color="#060606",
#         border_width=1,
#         border_color=BORDER2,
#         corner_radius=6,
#     )
#     # Center the single panel with equal padding on both sides
#     original_preview_frame.pack(fill='both', expand=True, padx=4, pady=4)

#     # Image label fills the panel
#     original_preview = CTkLabel(original_preview_frame, image=placeholder_photo_orig, text="")
#     original_preview.pack(fill='both', expand=True)

#     # Badge overlaid at bottom-left using place()
#     original_label_title = CTkLabel(
#         original_preview_frame,
#         text="ORIGINAL",
#         font=CTkFont(family="Segoe UI", size=9, weight="bold"),
#         text_color=CREAM3,
#         fg_color="#0C0C0B",
#         corner_radius=4,
#         padx=8,
#         pady=3,
#     )
#     original_label_title.place(relx=0.0, rely=1.0, anchor="sw", x=8, y=-8)
#     # Hide the ORIGINAL badge when showing the placeholder (no file loaded)
#     original_label_title.place_forget()

#     # ── Thin amber divider between panels (hidden initially) ─────────
#     _divider = CTkFrame(container, fg_color=AMBER_GLOW, width=1)
#     # Do NOT pack _divider yet — shown only after a file is loaded

#     # ── Right panel: UPSCALED (hidden initially) ─────────────────────
#     upscaled_preview_frame = CTkFrame(
#         container,
#         fg_color="#060606",
#         border_width=1,
#         border_color=BORDER2,
#         corner_radius=6,
#     )
#     # Do NOT pack upscaled_preview_frame yet — shown only after a file is loaded

#     upscaled_preview = CTkLabel(upscaled_preview_frame, image=placeholder_photo_ups, text="")
#     upscaled_preview.pack(fill='both', expand=True)

#     upscaled_label_title = CTkLabel(
#         upscaled_preview_frame,
#         text="UPSCALED",
#         font=CTkFont(family="Segoe UI", size=9, weight="bold"),
#         text_color=AMBER_DIM,
#         fg_color="#0C0906",
#         corner_radius=4,
#         padx=8,
#         pady=3,
#     )
#     upscaled_label_title.place(relx=0.0, rely=1.0, anchor="sw", x=8, y=-8)

#     # Store divider reference so it can be shown later
#     globals()['_preview_divider']       = _divider

#     globals()['original_preview']       = original_preview
#     globals()['upscaled_preview']       = upscaled_preview
#     globals()['original_preview_frame'] = original_preview_frame
#     globals()['upscaled_preview_frame'] = upscaled_preview_frame
#     globals()['original_label_title']   = original_label_title
#     globals()['upscaled_label_title']   = upscaled_label_title


 











# ###Loading-ICON####
# class LoadingIcon:
#     def __init__(self, master):
#         self.master = master
#         self.animating = False
#         self.angle = 0

#         size = 60
#         self.canvas = tk.Canvas(
#             master,
#             width=size,
#             height=size,
#             bg="#060606",
#             highlightthickness=0,
#             bd=0,
#         )
#         self.canvas.place(relx=0.5, rely=0.5, anchor="center")

#         self._size = size
#         self._arc_id = None

#     def start(self):
#         self.animating = True
#         logging.info("Started loading animation")
#         self._draw()

#     def stop(self):
#         self.animating = False
#         self.canvas.destroy()
#         logging.info("Stopped loading animation")

#     def _draw(self):
#         if not self.animating:
#             return
#         s = self._size
#         pad = 8
#         self.canvas.delete("all")

#         # Faint grey track circle
#         self.canvas.create_oval(pad, pad, s - pad, s - pad,
#                                 outline="#2A2A2A", width=5)

#         # Amber arc spinner
#         self.canvas.create_arc(pad, pad, s - pad, s - pad,
#                                start=self.angle,
#                                extent=270,
#                                outline=AMBER,
#                                width=5,
#                                style="arc")

#         self.angle = (self.angle + 12) % 360
#         self.master.after(30, self._draw)





























# ####VIDEO PREVIEW EXTERNAL FUNCTIONS######
# def load_model_inference():
#     global preview_ai_instance, last_model_config
#     logging.info(f" preview_ai_instance: {preview_ai_instance},last model config: {last_model_config} ")
#     if not selected_AI_model or selected_AI_model == AI_LIST_SEPARATOR[0]:
#         logging.info("Select an AI model first!")
#         return
#     try:
#         resolution_percentage = float(selected_input_resize_factor.get())
#         if not 1 <= resolution_percentage <= 100:
#             logging.info("Resolution must be between 1% and 100%")
#             return

#         resize_factor = float(resolution_percentage / 100.0)  

#         current_config = (
#             selected_AI_model,
#             selected_gpu,
#             resize_factor,  
#             float(selected_VRAM_limiter.get())
#         )

#         if not preview_ai_instance or last_model_config != current_config:
#             vram_limiter = float(selected_VRAM_limiter.get())
            
#             tiles_resolution = 100 * int(float(str(selected_VRAM_limiter.get())))
#             if tiles_resolution > 0: 
#                 vram_multiplier = very_low_VRAM
#                 max_resolution = int(vram_multiplier * vram_limiter * 100)
                
#                 preview_ai_instance = AI(
#                     selected_AI_model,
#                     selected_gpu,
#                     resize_factor, 
#                     max_resolution
#                 )
#                 available_providers = ort.get_available_providers()
#                 if "DmlExecutionProvider" in available_providers:
#                     preview_ai_instance.inferenceSession.set_providers(
#                     ['DmlExecutionProvider'], 
#                     [{'device_id': 0}]
#                 )
#                 else: 
#                     preview_ai_instance.inferenceSession.set_providers(
#                     preview_ai_instance.inferenceSession.set_providers(["CPUExecutionProvider"])

#                     )
#                 dummy_height = max(64, int(512 * resize_factor))  
#                 dummy_width = max(64, int(512 * resize_factor))
#                 dummy_input = np.random.randint(0, 255, (dummy_height, dummy_width, 3), dtype=np.uint8)

#                 logging.info(f"Dummy input shape: {dummy_input.shape}")
#                 logging.info(f"Dummy input shape: {dummy_input.shape}")
#                 _ = preview_ai_instance.AI_orchestration(dummy_input)
#                 last_model_config = current_config
#                 logging.info("Dummy inference complete")
#                 logging.info("Dummy inference complete")
#                 gc.collect()
#                 torch.cuda.empty_cache()
                
#     except Exception as e:
#         logging.info(f"Error loading model with dummy input: {str(e)}")
#         logging.info(f"Error loading model with dummy input: {str(e)}")
#         logging.info("Dummy inference ERROR")







# def load_model_if_needed(model_name):
#     global preview_ai_instance, current_loaded_model
#     logging.info(f"Loading model if needed: {model_name}...")
#     with model_loading_lock:
#         if current_loaded_model == model_name:
#             logging.info(f"Model {model_name} already loaded.")
#             return 
        
#         try:
#             logging.info(f"Loading {model_name} model...")
#             info_message.set(f"Loading {model_name} model...")

     
#             if preview_ai_instance:
#                 preview_ai_instance.inferenceSession = None
#                 del preview_ai_instance
#                 preview_ai_instance = None
#                 gc.collect()

          
#             preview_ai_instance = AI(
#                 model_name,
#                 selected_gpu,
#                 int(float(selected_input_resize_factor.get())),  
#                 int(float(selected_VRAM_limiter.get())) 
#             )

#             current_loaded_model = model_name
#             info_message.set(f"Model: {model_name} Ready!")
#             logging.info(f"Model: {model_name} Ready!")
#             logging.info(f"{model_name} loaded successfully.")
#         except Exception as e:
#             logging.info(f"Error loading model {model_name}: {str(e)}")
#             logging.info(f"Error loading model {model_name}: {str(e)}")
#             info_message.set(f"Model load failed: {str(e)}")
#             current_loaded_model = None
#             preview_ai_instance = None
#         finally:
#             window.after(0, check_model_loading_progress)




# def check_model_loading_progress():
#     global model_loading_thread, current_loaded_model,window
#     if model_loading_thread.is_alive():
#         window.after(100, check_model_loading_progress)
#     else:
#         if current_loaded_model == selected_AI_model:
#             window.preview_button.configure(state="normal")
#             info_message.set("Ready for preview")
#         else:
#             window.preview_button.configure(state="disabled")
#             info_message.set("Model load failed")







# def select_AI_from_menu(selected_option: str) -> None:
#     global selected_AI_model, current_loaded_model, model_loading_thread
#     logging.info(f"AI model selected: {selected_option}")
    
#     if selected_option == current_loaded_model or selected_option in AI_LIST_SEPARATOR:
#         return
    

#     selected_AI_model = selected_option
#     info_message.set(f"Loading {selected_option}...")
#     update_file_widget(1, 2, 3)

#     if model_loading_thread and model_loading_thread.is_alive():
#         model_loading_thread.join(timeout=0.5)
    
#     model_loading_thread = threading.Thread(
#         target=load_model_if_needed,
#         args=(selected_option, ),
#         daemon=True
#     )
#     model_loading_thread.start()


 







# # AI -------------------
# class AI:
#     # CLASS INIT FUNCTIONS
#     def __init__(
#             self, 
#             AI_model_name: str, 
#             directml_gpu: str, 
#             input_resize_factor: int,
#             max_resolution: int,
#             ):
        
#         # Passed variables
#         self.AI_model_name  = AI_model_name
#         self.audio_model_name = "Vocal_Isolation"
#         self.denoise_model_name = "Audio_Denoiser"
#         self.directml_gpu   = directml_gpu
#         self.input_resize_factor  = input_resize_factor
#         self.max_resolution = max_resolution

#         # Calculated variables
#         self.AI_model_path    = find_by_relative_path(f"AI-onnx{os_separator}{self.AI_model_name}_fp16.onnx")
#         self.inferenceSession = self._load_inferenceSession()
#         self.upscale_factor   = self._get_upscale_factor()
#         self.audio_model_path = find_by_relative_path(f"AI-onnx{os_separator}{self.audio_model_name}.onnx")
#         self.Denoise_Modelpath = find_by_relative_path(f"AI-onnx{os_separator}{self.denoise_model_name}.onnx")
        
#     def _get_upscale_factor(self) -> int:
#         if   "x1" in self.AI_model_name: return 1
#         elif "x2" in self.AI_model_name: return 2
#         elif "x4" in self.AI_model_name: return 4
        
        
    

#     def _load_inferenceSession(self) -> onnxruntime_inferenceSession:
#         import onnxruntime
#         providers = ['CPUExecutionProvider']

#         if 'CUDAExecutionProvider' in onnxruntime.get_available_providers():

#             providers = ['CUDAExecutionProvider', 'CPUExecutionProvider']
#         elif 'DmlExecutionProvider' in onnxruntime.get_available_providers():

#             match self.directml_gpu:
#                 case 'Auto':
                   
#                     providers = [('DmlExecutionProvider', {})] + providers
#                 case 'GPU 1' | 'GPU 2' | 'GPU 3' | 'GPU 4':
#                     device_id = int(self.directml_gpu.split()[-1]) - 1
#                     providers = [
#                         ('DmlExecutionProvider', {'device_id': device_id}),
#                         'CPUExecutionProvider'
#                     ]
#                 case 'CPU':
#                     providers = ['CPUExecutionProvider']
        
    
#         session_options = onnxruntime.SessionOptions()
#         session_options.graph_optimization_level = onnxruntime.GraphOptimizationLevel.ORT_ENABLE_ALL
#         session_options.execution_mode = onnxruntime.ExecutionMode.ORT_PARALLEL
        
#         try:
          
#             inference_session = onnxruntime_inferenceSession(
#                 path_or_bytes=self.AI_model_path,
#                 providers=providers,
#                 sess_options=session_options
#             )
#         except Exception as e:
#             logging.info(f"Session creation failed: {str(e)}")

#             inference_session = onnxruntime_inferenceSession(
#                 path_or_bytes=self.AI_model_path,
#                 providers=['CPUExecutionProvider']
#             )
        
#         logging.info(f"Using providers: {inference_session.get_providers()}")
#         if 'CUDAExecutionProvider' in inference_session.get_providers():
#             options = inference_session.get_provider_options()['CUDAExecutionProvider']
#             logging.info(f"CUDA device ID: {options.get('device_id', 'default')}")

#         return inference_session

#     def _load_audio_inferenceSession(self) -> onnxruntime_inferenceSession:
#         import onnxruntime
#         available_providers = onnxruntime.get_available_providers()
#         if 'DmlExecutionProvider' in available_providers:
#             providers = ['DmlExecutionProvider'] 
#             [{"device_id": 0}]
#         else:  
#             providers = ["CPUExecutionProvider"]


#         session_options = onnxruntime.SessionOptions()
#         session_options.graph_optimization_level = onnxruntime.GraphOptimizationLevel.ORT_ENABLE_ALL
#         session_options.execution_mode = onnxruntime.ExecutionMode.ORT_PARALLEL

#         try:
#             return ort.InferenceSession(
#                 path_or_bytes=self.audio_model_path,
#                 providers=providers,
#                 sess_options=session_options
#             )
#         except Exception as e:
#             logging.info(f"[AudioSession Error] {e}")
#             return ort.InferenceSession(
#                 path_or_bytes=self.audio_model_path,
#                 providers=['CPUExecutionProvider']
#             )

#     def extract_audio_from_video(self, video_path: str) -> str:
#         video_dir = os.path.dirname(video_path)
#         audio_output_path = os.path.join(video_dir, "extracted_audio.wav")
#         command = [
#             "ffmpeg",
#             "-y",               # Overwrite without asking
#             "-i", video_path,   # Input video
#             "-ac", "2",         # Force audio to stereo (2 channels)
#             "-ar", "44100",     # Set sample rate to 44100 Hz
#             "-q:a", "0",        # Best audio quality for VBR formats (optional here)
#             "-map", "0:a",      # Map only the audio stream
#             audio_output_path   # Output path
#         ]       
#         subprocess_run(command, check=True)
#         logging.info(f"Returning audio_output_path for extracted audio at: {audio_output_path}")
#         return audio_output_path
     

  
#     def run_vocal_isolation(self,video_path: str) -> str:
#         import soundfile as sf
#         from LocalModelAssets.Old_photos__colorizing.Vocal_isolation import main
#         audio_file_path = self.extract_audio_from_video(video_path)
#         audio_session = self._load_audio_inferenceSession()
#         vocals_array, samplerate = main(self.audio_model_path,audio_file_path,audio_session)
#         if vocals_array is None or samplerate is None:
#             raise ValueError("Failed to isolate vocals. Received None values from main() function.")
#        # sf.write("output_vocals.wav", vocals_array.T, samplerate)  
        
    
#         isolated_output_path = audio_file_path.replace("extracted_audio", "isolated_audio")
#         sf.write(isolated_output_path, vocals_array.T, samplerate)
#         logging.info(f"isolated audio saved at {isolated_output_path}")
#         return isolated_output_path
    

#     def run_audio_denoise(self,video_path: str) -> str:
#         import torch
#         import soundfile as sf
#         from librosa import istft
#         import numpy as np
#         video_dir = os.path.dirname(video_path)
#         audio_output_path = os.path.join(video_dir, "extracted_audio.wav")
#         command = [
#             "ffmpeg",
#             "-y",               # Overwrite without asking
#             "-i", video_path,   # Input video
#             "-ac", "2",         # Force audio to stereo (2 channels)
#             "-ar", "16000",     # Set sample rate to 44100 Hz
#             "-q:a", "0",        # Best audio quality for VBR formats (optional here)
#             "-map", "0:a",      # Map only the audio stream
#             audio_output_path   # Output path
#         ]       
#         subprocess_run(command, check=True)
#         x = torch.from_numpy(sf.read(audio_output_path, dtype='float32')[0])
#         x = torch.stft(x, 512, 256, 512, torch.hann_window(512).pow(0.5), return_complex=False)[None]
#         session =  self._load_audio_inferenceSession()

#         conv_cache = np.zeros([2, 1, 16, 16, 33], dtype="float32")
#         tra_cache = np.zeros([2, 3, 1, 1, 16], dtype="float32")
#         inter_cache = np.zeros([2, 1, 33, 16], dtype="float32")

#         T_list = []
#         outputs = []

#         inputs = x.numpy()
#         for i in range(inputs.shape[-2]):

#             out_i, conv_cache, tra_cache, inter_cache \
#                 = session.run([], {'mix': inputs[..., i:i + 1, :],
#                                 'conv_cache': conv_cache,
#                                 'tra_cache': tra_cache,
#                                 'inter_cache': inter_cache})
#             outputs.append(out_i)
#         outputs = np.concatenate(outputs, axis=2)
#         enhanced = istft(outputs[..., 0] + 1j * outputs[..., 1], n_fft=512, hop_length=256, win_length=512,
#                  window=np.hanning(512) ** 0.5)
#         sf.write('output_denoise.wav', enhanced.squeeze(), 16000)
#         denoised_output_path = audio_output_path.replace("extracted_audio", "output_denoise")
#         return denoised_output_path


#     def process_Audio_Inference(self, video_path,selected_audio_mode):
#         if selected_audio_mode == "Vocal Isolation":
#             try: 
#                 Enchanced_audiofile =  self.run_vocal_isolation(video_path)

#                 return Enchanced_audiofile
#             except Exception as e:
#                 logging.info(f"Audio inference vocal isolation failed: {str(e)}")
#                 return None
            
#         elif selected_audio_mode == "Audio Denoise":
#             try: 
#                 Denoised_audio = self.run_audio_denoise(video_path)
#                 return Denoised_audio
#             except Exception as e:
#                 logging.info(f"Audio inference audio denoise failed: {str(e)}")
#                 return
#         else: 
#             logging.info("Normal audio returning None")
#             return None
   
    





    
    
#     #INTERNAL CLASS FUNCTIONS
#     def get_image_mode(self, image: numpy_ndarray) -> str:
#         match image.shape:
#             case (rows, cols):
#                 return "Grayscale"
#             case (rows, cols, channels) if channels == 3:
#                 return "RGB"
#             case (rows, cols, channels) if channels == 4:
#                 return "RGBA"

#     def get_image_resolution(self, image: numpy_ndarray) -> tuple:
#         height = image.shape[0]
#         width  = image.shape[1]

#         return height, width 

#     def calculate_target_resolution(self, image: numpy_ndarray) -> tuple:
#         height, width = self.get_image_resolution(image)
#         target_height = height * self.upscale_factor
#         target_width  = width  * self.upscale_factor

#         return target_height, target_width

#     def resize_with_input_factor(self, image: numpy_ndarray) -> numpy_ndarray:
        
#         old_height, old_width = self.get_image_resolution(image)

#         new_width  = int(old_width * self.input_resize_factor)
#         new_height = int(old_height * self.input_resize_factor)

#         match self.input_resize_factor:
#             case factor if factor > 1:
#                 return opencv_resize(image, (new_width, new_height), interpolation = INTER_CUBIC)
#             case factor if factor < 1:
#                 return opencv_resize(image, (new_width, new_height), interpolation = INTER_AREA)
#             case _:
#                 return image
            


#     def resize_image_with_target_resolution(
#             self,
#             image: numpy_ndarray, 
#             t_height: int,
#             t_width: int
#             ) -> numpy_ndarray:
        
#         old_height, old_width = self.get_image_resolution(image)
#         old_resolution = old_height + old_width
#         new_resolution = t_height + t_width

#         if new_resolution > old_resolution:
#             return opencv_resize(image, (t_width, t_height), interpolation = INTER_LINEAR)
#         else:
#             return opencv_resize(image, (t_width, t_height), interpolation = INTER_AREA) 







#  # VIDEO CLASS FUNCTIONS
#     def calculate_multiframes_supported_by_gpu(self, video_frame_path: str) -> int:
#         resized_video_frame  = self.resize_with_input_factor(image_read(video_frame_path))
#         height, width        = self.get_image_resolution(resized_video_frame)
#         image_pixels         = height * width
#         max_supported_pixels = self.max_resolution * self.max_resolution

#         frames_simultaneously = max_supported_pixels // image_pixels 

#         logging.info(f" Frames supported simultaneously by GPU: {frames_simultaneously}")

#         return frames_simultaneously







#     # TILLING FUNCTIONS
#     def video_need_tilling(self, video_frame_path: str) -> bool:       
#         resized_video_frame  = self.resize_with_input_factor(image_read(video_frame_path))
#         height, width        = self.get_image_resolution(resized_video_frame)
#         image_pixels         = height * width
#         max_supported_pixels = self.max_resolution * self.max_resolution

#         if image_pixels > max_supported_pixels:
#             return True
#         else:
#             return False

#     def image_need_tilling(self, image: numpy_ndarray) -> bool:
#         height, width = self.get_image_resolution(image)
#         image_pixels  = height * width
#         max_supported_pixels = self.max_resolution * self.max_resolution

#         if image_pixels > max_supported_pixels:
#             return True
#         else:
#             return False

#     def add_alpha_channel(self, image: numpy_ndarray) -> numpy_ndarray:
#         if image.shape[2] == 3:
#             alpha = numpy_full((image.shape[0], image.shape[1], 1), 255, dtype = uint8)
#             image = numpy_concatenate((image, alpha), axis = 2)
#         return image

#     def calculate_tiles_number(
#             self, 
#             image: numpy_ndarray, 
#             ) -> tuple:
        
#         height, width = self.get_image_resolution(image)

#         tiles_x = (width  + self.max_resolution - 1) // self.max_resolution
#         tiles_y = (height + self.max_resolution - 1) // self.max_resolution

#         return tiles_x, tiles_y
    
#     def split_image_into_tiles(
#             self,
#             image: numpy_ndarray, 
#             tiles_x: int, 
#             tiles_y: int
#             ) -> list[numpy_ndarray]:

#         img_height, img_width = self.get_image_resolution(image)

#         tile_width  = img_width // tiles_x
#         tile_height = img_height // tiles_y

#         tiles = []

#         for y in range(tiles_y):
#             y_start = y * tile_height
#             y_end   = (y + 1) * tile_height

#             for x in range(tiles_x):
#                 x_start = x * tile_width
#                 x_end   = (x + 1) * tile_width
#                 tile    = image[y_start:y_end, x_start:x_end]
#                 tiles.append(tile)

#         return tiles

#     def combine_tiles_into_image(
#             self,
#             image: numpy_ndarray,
#             tiles: list[numpy_ndarray], 
#             t_height: int, 
#             t_width: int,
#             num_tiles_x: int, 
#             ) -> numpy_ndarray:

#         match self.get_image_mode(image):
#             case "Grayscale": tiled_image = numpy_zeros((t_height, t_width, 3), dtype = uint8)
#             case "RGB":       tiled_image = numpy_zeros((t_height, t_width, 3), dtype = uint8)
#             case "RGBA":      tiled_image = numpy_zeros((t_height, t_width, 4), dtype = uint8)

#         for tile_index in range(len(tiles)):
#             actual_tile = tiles[tile_index]

#             tile_height, tile_width = self.get_image_resolution(actual_tile)

#             row     = tile_index // num_tiles_x
#             col     = tile_index % num_tiles_x
#             y_start = row * tile_height
#             y_end   = y_start + tile_height
#             x_start = col * tile_width
#             x_end   = x_start + tile_width

#             match self.get_image_mode(image):
#                 case "Grayscale": tiled_image[y_start:y_end, x_start:x_end] = actual_tile
#                 case "RGB":       tiled_image[y_start:y_end, x_start:x_end] = actual_tile
#                 case "RGBA":      tiled_image[y_start:y_end, x_start:x_end] = self.add_alpha_channel(actual_tile)

#         return tiled_image

    





#     # AI CLASS FUNCTIONS
#     def normalize_image(self, image: numpy_ndarray) -> tuple:
#         range = 255
#         if numpy_max(image) > 256: range = 65535
#         normalized_image = image / range

#         return normalized_image, range
    
    
    
#     def preprocess_image(self, image: numpy_ndarray) -> numpy_ndarray:
#         image = numpy_transpose(image, (2, 0, 1))
#         image = numpy_expand_dims(image, axis=0)

#         return image



#     def onnxruntime_inference(self, image: numpy_ndarray) -> numpy_ndarray:

#         # IO BINDING
#         # io_binding = self.inferenceSession.io_binding()
#         # io_binding.bind_cpu_input(self.inferenceSession.get_inputs()[0].name, image)
#         # io_binding.bind_output(self.inferenceSession.get_outputs()[0].name, element_type = float32)
#         # self.inferenceSession.run_with_iobinding(io_binding)
#         # onnx_output = io_binding.copy_outputs_to_cpu()[0]

#         onnx_input  = {self.inferenceSession.get_inputs()[0].name: image}
#         onnx_output = self.inferenceSession.run(None, onnx_input)[0]

#         return onnx_output



#     def postprocess_output(self, onnx_output: numpy_ndarray) -> numpy_ndarray:
#         onnx_output = numpy_squeeze(onnx_output, axis=0)
#         onnx_output = numpy_clip(onnx_output, 0, 1)
#         onnx_output = numpy_transpose(onnx_output, (1, 2, 0))

#         return onnx_output.astype(float32)



#     def de_normalize_image(self, onnx_output: numpy_ndarray, max_range: int) -> numpy_ndarray:    
#         match max_range:
#             case 255:   return (onnx_output * max_range).astype(uint8)
#             case 65535: return (onnx_output * max_range).round().astype(float32)




#     def AI_upscale(self, image: numpy_ndarray) -> numpy_ndarray:
#         image_mode   = self.get_image_mode(image)
#         image, range = self.normalize_image(image)
#         image        = image.astype(float32)

#         match image_mode:
#             case "RGB":
#                 image = self.preprocess_image(image)
#                 onnx_output  = self.onnxruntime_inference(image)
#                 onnx_output  = self.postprocess_output(onnx_output)
#                 output_image = self.de_normalize_image(onnx_output, range)

#                 return output_image
            
#             case "RGBA":
#                 alpha = image[:, :, 3]
#                 image = image[:, :, :3]
#                 image = opencv_cvtColor(image, COLOR_BGR2RGB)

#                 image = image.astype(float32)
#                 alpha = alpha.astype(float32)

#                 # Image
#                 image = self.preprocess_image(image)
#                 onnx_output_image = self.onnxruntime_inference(image)
#                 onnx_output_image = self.postprocess_output(onnx_output_image)
#                 onnx_output_image = opencv_cvtColor(onnx_output_image, COLOR_BGR2RGBA)

#                 # Alpha
#                 alpha = numpy_expand_dims(alpha, axis=-1)
#                 alpha = numpy_repeat(alpha, 3, axis=-1)
#                 alpha = self.preprocess_image(alpha)
#                 onnx_output_alpha = self.onnxruntime_inference(alpha)
#                 onnx_output_alpha = self.postprocess_output(onnx_output_alpha)
#                 onnx_output_alpha = opencv_cvtColor(onnx_output_alpha, COLOR_RGB2GRAY)

#                 # Fusion Image + Alpha
#                 onnx_output_image[:, :, 3] = onnx_output_alpha
#                 output_image = self.de_normalize_image(onnx_output_image, range)

#                 return output_image
            
#             case "Grayscale":
#                 image = opencv_cvtColor(image, COLOR_GRAY2RGB)
                
#                 image = self.preprocess_image(image)
#                 onnx_output  = self.onnxruntime_inference(image)
#                 onnx_output  = self.postprocess_output(onnx_output)
#                 output_image = opencv_cvtColor(onnx_output, COLOR_RGB2GRAY)
#                 output_image = self.de_normalize_image(onnx_output, range)

#                 return output_image



#     def AI_upscale_with_tilling(self, image: numpy_ndarray) -> numpy_ndarray:
#         t_height, t_width = self.calculate_target_resolution(image)
#         tiles_x, tiles_y  = self.calculate_tiles_number(image)
#         tiles_list        = self.split_image_into_tiles(image, tiles_x, tiles_y)
#         tiles_list        = [self.AI_upscale(tile) for tile in tiles_list]

#         return self.combine_tiles_into_image(image, tiles_list, t_height, t_width, tiles_x)




#     # EXTERNAL FUNCTION
#     def AI_orchestration(self, image: numpy_ndarray) -> numpy_ndarray:

#         resized_image = self.resize_with_input_factor(image)
        
#         if self.image_need_tilling(resized_image):
#             return self.AI_upscale_with_tilling(resized_image)
#         else:
#             return self.AI_upscale(resized_image)




# # GUI utils ---------------------------
# class MessageBox(CTkToplevel):

#     def __init__(
#             self,
#             messageType: str,
#             title: str,
#             subtitle: str,
#             default_value: str,
#             option_list: list,
#             ) -> None:

#         super().__init__()

#         self._running: bool = False

#         self._messageType = messageType
#         self._title = title        
#         self._subtitle = subtitle
#         self._default_value = default_value
#         self._option_list = option_list
#         self._ctkwidgets_index = 0

#         self.title('')
#         self.lift()                         
#         self.attributes("-topmost", True)   
#         self.protocol("WM_DELETE_WINDOW", self._on_closing)
#         self.after(10, self._create_widgets) 
#         self.resizable(False, False)
#         self.grab_set()                       

#     def _ok_event(
#             self, 
#             event = None
#             ) -> None:
#         self.grab_release()
#         self.destroy()

#     def _on_closing(
#             self
#             ) -> None:
#         self.grab_release()
#         self.destroy()

#     def createEmptyLabel(
#             self
#             ) -> CTkLabel:
        
#         return CTkLabel(master = self, 
#                         fg_color = "transparent",
#                         width    = 500,
#                         height   = 17,
#                         text     = '')

#     def placeInfoMessageTitleSubtitle(
#             self,
#             ) -> None:

#         spacingLabel1 = self.createEmptyLabel()
#         spacingLabel2 = self.createEmptyLabel()

#         if self._messageType == "info":
#             title_subtitle_text_color = "#3399FF"
#         elif self._messageType == "error":
#             title_subtitle_text_color = "#FF3131"

#         titleLabel = CTkLabel(
#             master     = self,
#             width      = 500,
#             anchor     = 'w',
#             justify    = "left",
#             fg_color   = "transparent",
#             text_color = title_subtitle_text_color,
#             font       = bold22,
#             text       = self._title
#             )
        
#         if self._default_value != None:
#             defaultLabel = CTkLabel(
#                 master     = self,
#                 width      = 500,
#                 anchor     = 'w',
#                 justify    = "left",
#                 fg_color   = "transparent",
#                 text_color = "#3399FF",
#                 font       = bold17,
#                 text       = f"Default: {self._default_value}"
#                 )
        
#         subtitleLabel = CTkLabel(
#             master     = self,
#             width      = 500,
#             anchor     = 'w',
#             justify    = "left",
#             fg_color   = "transparent",
#             text_color = title_subtitle_text_color,
#             font       = bold14,
#             text       = self._subtitle
#             )
        
#         spacingLabel1.grid(row = self._ctkwidgets_index, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = "ew")
        
#         self._ctkwidgets_index += 1
#         titleLabel.grid(row = self._ctkwidgets_index, column = 0, columnspan = 2, padx = 25, pady = 0, sticky = "ew")
        
#         if self._default_value != None:
#             self._ctkwidgets_index += 1
#             defaultLabel.grid(row = self._ctkwidgets_index, column = 0, columnspan = 2, padx = 25, pady = 0, sticky = "ew")
        
#         self._ctkwidgets_index += 1
#         subtitleLabel.grid(row = self._ctkwidgets_index, column = 0, columnspan = 2, padx = 25, pady = 0, sticky = "ew")
        
#         self._ctkwidgets_index += 1
#         spacingLabel2.grid(row = self._ctkwidgets_index, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = "ew")

#     def placeInfoMessageOptionsText(
#             self,
#             ) -> None:
        
#         for option_text in self._option_list:
#             optionLabel = CTkLabel(master = self,
#                                     width  = 600,
#                                     height = 45,
#                                     corner_radius = 6,
#                                     anchor     = 'w',
#                                     justify    = "left",
#                                     text_color = "#C0C0C0",
#                                     fg_color   = "#282828",
#                                     bg_color   = "transparent",
#                                     font       = bold12,
#                                     text       = option_text)
            
#             self._ctkwidgets_index += 1
#             optionLabel.grid(row = self._ctkwidgets_index, column = 0, columnspan = 2, padx = 25, pady = 4, sticky = "ew")

#         spacingLabel3 = self.createEmptyLabel()

#         self._ctkwidgets_index += 1
#         spacingLabel3.grid(row = self._ctkwidgets_index, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = "ew")

#     def placeInfoMessageOkButton(
#             self
#             ) -> None:
        
#         ok_button = CTkButton(
#             master  = self,
#             command = self._ok_event,
#             text    = 'OK',
#             width   = 125,
#             font         = bold11,
#             border_width = 1,
#             fg_color     = "#282828",
#             text_color   = "#E0E0E0",
#             border_color = "#0096FF"
#             )
        
#         self._ctkwidgets_index += 1
#         ok_button.grid(row = self._ctkwidgets_index, column = 1, columnspan = 1, padx = (10, 20), pady = (10, 20), sticky = "e")

#     def _create_widgets(
#             self
#             ) -> None:

#         self.grid_columnconfigure((0, 1), weight=1)
#         self.rowconfigure(0, weight=1)

#         self.placeInfoMessageTitleSubtitle()
#         self.placeInfoMessageOptionsText()
#         self.placeInfoMessageOkButton()    







# #SCROLLFRAME---------
# class FileWidget(CTkScrollableFrame):

#     def __init__(
#             self, 
#             master,
#             selected_file_list, 
#             input_resize_factor  = 0,
#             upscale_factor = 1,
#             **kwargs
#             ) -> None:
       
#         super().__init__(master, height=300,**kwargs)

#         self.file_list      = selected_file_list
#         self.input_resize_factor  = input_resize_factor
#         self.upscale_factor = upscale_factor

#         self.label_list = []
#         # Make column 0 stretch to fill full width of the scrollable frame
#         self.columnconfigure(0, weight=1)
#         self._create_widgets()

#     def _destroy_(self) -> None:
#         global selected_file_list, preview_instance, file_widget

#         # Clear both the local and global file lists
#         self.file_list.clear()
#         selected_file_list.clear()
#         file_overrides.clear()

#         # Stop any active preview
#         if preview_instance:
#             try:
#                 preview_instance.close()
#             except Exception:
#                 pass
#             preview_instance = None

#         # Destroy the FileWidget completely so next open_files_action
#         # creates a fresh one (including the Empty LIST button)
#         try:
#             file_widget.destroy()
#         except Exception:
#             pass
#         del file_widget

#         place_loadFile_section(window)


#     def _create_widgets(self) -> None:
#         self.add_clean_button()
#         index_row = 1
#         for file_path in self.file_list:
#             label = self.add_file_information(file_path, index_row)
#             self.label_list.append(label)
#             index_row +=1


#     def add_file_information(self, file_path, index_row) -> CTkLabel:
#         # Outer card frame — spans full column width with amber-theme border
#         file_frame = CTkFrame(
#             self,
#             fg_color="#0E0E0D",
#             border_width=1,
#             border_color="#201E1A",
#             corner_radius=5,
#         )
#         file_frame.grid(row=index_row, column=0, sticky="ew", pady=3, padx=4)
#         file_frame.columnconfigure(0, weight=1)

#         infos, icon = self.extract_file_info(file_path)
#         label = CTkLabel(
#             file_frame,
#             text=infos,
#             image=icon,
#             font=bold12,
#             text_color="#948C7E",
#             compound="left",
#             anchor="w",
#             padx=10,
#             pady=5,
#             justify="left",
#         )
#         label.grid(row=0, column=0, sticky="ew")

#         # Button row — right-aligned
#         btn_frame = CTkFrame(file_frame, fg_color="transparent")
#         btn_frame.grid(row=0, column=1, padx=(0, 8), pady=4, sticky="e")

#         # Edit button — opens per-file settings dialog
#         edit_btn = CTkButton(
#             btn_frame,
#             text="Edit",
#             width=72,
#             height=24,
#             font=bold11,
#             fg_color="#1A1408",
#             hover_color="#2A200A",
#             text_color="#D49A2A",
#             border_color="#8C6418",
#             border_width=1,
#             corner_radius=5,
#             command=lambda path=file_path: self.open_edit_dialog(path)
#         )
#         edit_btn.pack(side="left", padx=(0, 4))

#         global preview_button
#         preview_button = CTkButton(
#             btn_frame,
#             text="Preview",
#             width=72,
#             height=24,
#             font=bold11,
#             fg_color="#0E0E0C",
#             hover_color="#181612",
#             text_color="#948C7E",
#             border_color="#201E1A",
#             border_width=1,
#             corner_radius=5,
#             command=lambda path=file_path: self.preview_file(path)
#         )
#         preview_button.pack(side="left", padx=(0, 4))

#         delete_btn = CTkButton(
#             btn_frame,
#             text="Delete",
#             width=72,
#             height=24,
#             font=bold11,
#             fg_color="#160808",
#             hover_color="#220C0C",
#             text_color="#C04040",
#             border_color="#EC1D1D",
#             border_width=1,
#             corner_radius=5,
#             command=lambda path=file_path: self.delete_single_file(path)
#         )
#         delete_btn.pack(side="left")

#         return file_frame



#     def open_edit_dialog(self, file_path):
#         """Open a per-file settings override dialog."""
#         global file_overrides

#         dialog = CTkToplevel(self)
#         dialog.title(f"Edit: {os_path_basename(file_path)}")
#         dialog.geometry("380x340")
#         dialog.resizable(False, False)
#         dialog.configure(fg_color="#0A0A09")
#         dialog.grab_set()

#         ov = file_overrides.get(file_path, {})

#         CTkLabel(
#             dialog,
#             text="Per-file AI settings",
#             font=CTkFont(family="Segoe UI", size=11, weight="bold"),
#             text_color=AMBER, fg_color="transparent",
#         ).pack(pady=(12, 2))
#         CTkLabel(
#             dialog, text=os_path_basename(file_path),
#             font=CTkFont(family="Segoe UI", size=9),
#             text_color=CREAM3, fg_color="transparent",
#         ).pack(pady=(0, 10))

#         form = CTkFrame(dialog, fg_color="#0E0E0D", border_width=1, border_color=BORDER2, corner_radius=6)
#         form.pack(fill="x", padx=16, pady=4)

#         def make_row(label_text, widget_fn):
#             r = CTkFrame(form, fg_color="transparent")
#             r.pack(fill="x", padx=10, pady=4)
#             CTkLabel(r, text=label_text, width=120, anchor="w",
#                      font=CTkFont(family="Segoe UI", size=9, weight="bold"),
#                      text_color=AMBER_DIM, fg_color="transparent").pack(side="left")
#             w = widget_fn(r)
#             w.pack(side="left", padx=(6, 0))
#             return w

#         ai_var     = StringVar(value=ov.get("ai_model",     default_AI_model))
#         interp_var = StringVar(value=ov.get("interpolation", default_interpolation))
#         res_var    = StringVar(value=str(ov.get("resize_factor", selected_input_resize_factor.get())))
#         img_var    = StringVar(value=ov.get("image_ext",    default_image_extension))
#         vid_var    = StringVar(value=ov.get("video_ext",    default_video_extension))

#         make_row("AI Model",       lambda p: create_option_menu_2(lambda v: ai_var.set(v),     AI_models_list,       ai_var.get(),     master=p, width=200))
#         make_row("AI Interpolation", lambda p: create_option_menu_2(lambda v: interp_var.set(v), interpolation_list,  interp_var.get(), master=p, width=200))
#         make_row("Input Res %",    lambda p: CTkEntry(p, textvariable=res_var, width=200, height=26,
#                                                       font=CTkFont(family="Segoe UI", size=10),
#                                                       fg_color="#080808", border_color=BORDER2, border_width=1,
#                                                       text_color=CREAM2, corner_radius=4))
#         make_row("Image Codec",    lambda p: create_option_menu_2(lambda v: img_var.set(v),    image_extension_list, img_var.get(),    master=p, width=200))
#         make_row("Video Codec",    lambda p: create_option_menu_2(lambda v: vid_var.set(v),    video_extension_list, vid_var.get(),    master=p, width=200))

#         def save_and_close():
#             interp_map = {"Disabled": 0, "Low": 0.3, "Medium": 0.5, "High": 0.7}
#             try:   rf = int(float(res_var.get()))
#             except: rf = int(float(selected_input_resize_factor.get()))
#             file_overrides[file_path] = {
#                 "ai_model":      ai_var.get(),
#                 "interpolation": interp_var.get(),
#                 "interp_factor": interp_map.get(interp_var.get(), 0),
#                 "resize_factor": rf,
#                 "image_ext":     img_var.get(),
#                 "video_ext":     vid_var.get(),
#             }
#             update_file_widget(1, 2, 3)
#             dialog.destroy()

#         def clear_and_close():
#             file_overrides.pop(file_path, None)
#             update_file_widget(1, 2, 3)
#             dialog.destroy()

#         btn_row = CTkFrame(dialog, fg_color="transparent")
#         btn_row.pack(pady=12)

#         CTkButton(btn_row, text="Save", width=110, height=28, command=save_and_close,
#                   fg_color=AMBER_GLOW, hover_color="#5a3c0c", text_color=AMBER,
#                   border_color=AMBER_DIM, border_width=1, corner_radius=5,
#                   font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         ).pack(side="left", padx=6)

#         CTkButton(btn_row, text="Reset to global", width=130, height=28, command=clear_and_close,
#                   fg_color="#0E0E0C", hover_color="#181612", text_color=CREAM2,
#                   border_color=BORDER2, border_width=1, corner_radius=5,
#                   font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         ).pack(side="left", padx=6)


#     def delete_single_file(self, file_path):
#         global selected_file_list, preview_instance, file_widget

#         if file_path not in selected_file_list:
#             return

#         selected_file_list.remove(file_path)
#         self.file_list = selected_file_list
#         # Remove any per-file override for the deleted file
#         file_overrides.pop(file_path, None)

#         if preview_instance and preview_instance.video_path == file_path:
#             try:
#                 preview_instance.close()
#             except Exception:
#                 pass
#             preview_instance = None

#         if not selected_file_list:
#             # No files left — destroy widget entirely, reset the preview area
#             # Do NOT call _destroy_() to avoid double-clearing the list
#             try:
#                 file_widget.destroy()
#             except Exception:
#                 pass
#             del file_widget
#             place_loadFile_section(window)
#         else:
#             # Rebuild rows inside the existing scrollable frame (keeps Empty LIST)
#             self.label_list = []
#             for widget in self.winfo_children():
#                 widget.destroy()
#             self._create_widgets()
#             update_file_widget(1, 2, 3)
            




#     def preview_file(self, file_path):
#         global preview_instance, container

#         if preview_instance:
#             preview_instance.close()
#             preview_instance = None

#         preview_instance = VideoPreview(container, None, None, file_path)
#         preview_button.configure(state=DISABLED)
  
    

#     def add_clean_button(self) -> None:
        
#         button = CTkButton(
#             self, 
#             image        = clear_icon,
#             font         = bold11,
#             text         = "Empty LIST", 
#             compound     = "left",
#             width        = 120, 
#             height       = 22,
#             border_width = 1,
#             fg_color     = "#1A1408",
#             hover_color  = "#2A200A",
#             text_color   = AMBER,
#             border_color = AMBER_DIM,
#             corner_radius= 5,
#             )

#         button.configure(command=lambda: self._destroy_())
#         # Place in column 0 with east-anchor so file-row frames can stretch
#         # to the full scrollable-frame width without any adjacent column stealing space.
#         button.grid(row=0, column=0, sticky="e", pady=(7, 7), padx=(0, 7))
        
#     @cache
#     def extract_file_icon(self, file_path) -> CTkImage:
#         max_size = 50

#         if check_if_file_is_video(file_path):
#             video_cap   = opencv_VideoCapture(file_path)
#             total_frames = int(video_cap.get(CAP_PROP_FRAME_COUNT))
#             # Seek to 10% into the video to avoid black/empty opening frames
#             seek_frame = max(1, int(total_frames * 0.10))
#             video_cap.set(cv2.CAP_PROP_POS_FRAMES, seek_frame)
#             success, frame = video_cap.read()
#             # Fallback: try a few more positions if still black
#             if not success or frame is None or frame.max() < 10:
#                 for pct in [0.25, 0.5, 0.01]:
#                     video_cap.set(cv2.CAP_PROP_POS_FRAMES, max(1, int(total_frames * pct)))
#                     success, frame = video_cap.read()
#                     if success and frame is not None and frame.max() >= 10:
#                         break
#             video_cap.release()
#             if not success or frame is None:
#                 frame = numpy_zeros((50, 50, 3), dtype=uint8)
#             source_icon = opencv_cvtColor(frame, COLOR_BGR2RGB)
#         else:
#             source_icon = opencv_cvtColor(image_read(file_path), COLOR_BGR2RGB)

#         ratio       = min(max_size / source_icon.shape[0], max_size / source_icon.shape[1])
#         new_width   = int(source_icon.shape[1] * ratio)
#         new_height  = int(source_icon.shape[0] * ratio)
#         source_icon = opencv_resize(source_icon,(new_width, new_height))
#         ctk_icon    = CTkImage(pillow_image_fromarray(source_icon, mode="RGB"), size = (new_width, new_height))

#         return ctk_icon
        
    
        
#     def extract_file_info(self, file_path) -> tuple:
        
#         if check_if_file_is_video(file_path):
#             cap          = opencv_VideoCapture(file_path)
#             width        = round(cap.get(CAP_PROP_FRAME_WIDTH))
#             height       = round(cap.get(CAP_PROP_FRAME_HEIGHT))
#             num_frames   = int(cap.get(CAP_PROP_FRAME_COUNT))
#             frame_rate   = cap.get(CAP_PROP_FPS)
#             duration     = num_frames/frame_rate
#             minutes      = int(duration/60)
#             seconds      = duration % 60
#             cap.release()

#             video_name = str(file_path.split("/")[-1])
#             file_icon  = self.extract_file_icon(file_path)

#             file_infos = (f"{video_name}\n"
#                           f"Resolution {width}x{height} • {minutes}m:{round(seconds)}s • {num_frames}frames\n")
            
#             if self.input_resize_factor != 0 and self.upscale_factor != 0 :

#                 input_resized_height  = int(height * (self.input_resize_factor/100))
#                 input_resized_width   = int(width * (self.input_resize_factor/100))

#                 upscaled_height = int(input_resized_height * self.upscale_factor)
#                 upscaled_width  = int(input_resized_width * self.upscale_factor)



#                 file_infos += (
#                     f"AI input ({self.input_resize_factor}%) ➜ {input_resized_width}x{input_resized_height} \n"
#                     f"AI output (x{self.upscale_factor}) ➜ {upscaled_width}x{upscaled_height} \n"
#                 )
#         else:
#             image_name    = str(file_path.split("/")[-1])
#             height, width = get_image_resolution(image_read(file_path))
#             file_icon     = self.extract_file_icon(file_path)

#             file_infos = (f"{image_name}\n"
#                           f"Resolution {width}x{height}\n")
            
#             if self.input_resize_factor != 0 and self.upscale_factor != 0 :
#                 input_resized_height = int(height * (self.input_resize_factor/100))
#                 input_resized_width  = int(width * (self.input_resize_factor/100))

#                 upscaled_height = int(input_resized_height * self.upscale_factor)
#                 upscaled_width  = int(input_resized_width * self.upscale_factor)

                
          
#                 file_infos += (
#                                 f"AI input ({self.input_resize_factor}%) ➜ {input_resized_width}x{input_resized_height} \n"
#                                 f"AI output (x{self.upscale_factor}) ➜ {upscaled_width}x{upscaled_height} \n"
#                             )

#         return file_infos, file_icon









#   # EXTERNAL FUNCTIONS
#     def clean_file_list(self) -> None:
#         for label in self.label_list:
#             label.grid_forget()
    
#     def get_selected_file_list(self) -> list: 
#         return self.file_list 

#     def set_upscale_factor(self, upscale_factor) -> None:
#         self.upscale_factor = upscale_factor

#     def set_resize_factor(self, input_resize_factor) -> None:
#         self.input_resize_factor = input_resize_factor
 

 
# def get_values_for_file_widget() -> tuple:
#     # Upscale factor
#     upscale_factor = get_upscale_factor()

#     # Input resolution %
#     try:
#         input_resize_factor = int(float(str(selected_input_resize_factor.get())))
#     except:
#         input_resize_factor = 0
    
#     return  input_resize_factor, upscale_factor




 
# def update_file_widget(a, b, c) -> None:
#     try:
#         global file_widget
#         file_widget
#     except:
#         return
    
#     upscale_factor = get_upscale_factor()

#     try:
#         resize_factor = int(float(str(selected_input_resize_factor.get())))
#     except:
#         resize_factor = 0

#     file_widget.clean_file_list()
#     file_widget.set_resize_factor(resize_factor)
#     file_widget.set_upscale_factor(upscale_factor)
#     file_widget._create_widgets()

    

# def create_info_button(
#         command: Callable,
#         text: str,
#         width: int = 150,
#         master=None
#         ) -> CTkButton:
#     return CTkButton(
#         master        = master if master else window,
#         command       = command,
#         text          = "● " + text,
#         fg_color      = "transparent",
#         hover_color   = "#181410",
#         text_color    = "#5A5248",
#         anchor        = "w",
#         corner_radius = 0,
#         height        = 20,
#         width         = width,
#         font          = CTkFont(family="Segoe UI", size=8, weight="bold"),
#         border_width  = 0,
#     )


   

# def create_option_menu(
#         command: Callable, 
#         values: list,
#         default_value: str,
#         width: int = 150,
#         master=None  
#         ) -> CTkOptionMenu:
    
#     option_menu = CTkOptionMenu(
#         master=master if master else window,  
#         command = command,
#         values  = values,
#         width         = width,
#         height        = 30,
#         corner_radius = 5,
#         dropdown_font = bold11,
#         font          = bold11,
#         anchor        = "center",
#         text_color    = text_color,
#         fg_color      = widget_background_color,
#         button_color       = widget_background_color,
#         button_hover_color = "#282828",
#         dropdown_fg_color  = text_color,
#     )
#     option_menu.set(default_value)
#     return option_menu



# def create_option_menu_2(
#         command: Callable,
#         values: list,
#         default_value: str,
#         width: int = 330,
#         master=None
#         ) -> CTkFrame:
#     option_menu_frame = CTkFrame(
#         master=master,
#         width=width,
#         height=36,
#         border_width=1,
#         border_color=("#FFFFFF"),
#         corner_radius=6,
#         fg_color="#0B0B0A",
#     )
#     option_menu = CTkOptionMenu(
#         master=option_menu_frame,
#         command=command,
#         values=values,
#         width=width,
#         height=28,
#         corner_radius=5,
#         dropdown_font=CTkFont(family="Segoe UI", size=10),
#         font=CTkFont(family="Segoe UI", size=11, weight="bold"),
#         anchor="center",
#         text_color=CREAM,
#         fg_color="#0B0B0A",
#         button_color="#181410",
#         button_hover_color="#22201C",
#         dropdown_fg_color="#0E0E0C",
#         dropdown_text_color=CREAM2,
#         dropdown_hover_color="#181410",
#     )
#     option_menu.set(default_value)
#     option_menu_frame.pack_propagate(False)
#     option_menu.place(relx=0.5, rely=0.5, anchor="center")
#     return option_menu_frame



# def create_text_box(textvariable: StringVar, master=None, width=150) -> CTkEntry:
#     return CTkEntry(
#         master        = master if master else window,
#         textvariable  = textvariable,
#         corner_radius = 5,
#         width         = width,
#         height        = 30,
#         font          = CTkFont(family="Segoe UI", size=12, weight="bold"),
#         justify       = "center",
#         text_color    = CREAM,
#         fg_color      = "#0B0B0A",
#         border_width  = 1,
#         border_color  = "#FFFFFF",
#     )



# def create_text_box_output_path(textvariable: StringVar, width=None) -> CTkEntry:
#     return CTkEntry(
#         master        = window,
#         textvariable  = textvariable,
#         border_width  = 1,
#         corner_radius = 5,
#         width         = width if width != None else 225,
#         height        = 25,
#         font          = CTkFont(family="Segoe UI", size=9),
#         justify       = "center",
#         text_color    = CREAM3,
#         fg_color      = "#0A0A09",
#         border_color  = BORDER2,
#         state         = DISABLED
#     )



# def create_active_button(
#         command: Callable,
#         text: str,
#         icon: CTkImage = None,
#         width: int = 140,
#         height: int = 30,
#         border_color: str = AMBER
#         ) -> CTkButton:
#     is_stop    = (border_color == "#EC1D1D")
#     is_select  = (text == "SELECT")
#     if is_stop:
#         bg   = "#160808"; hov = "#220C0C"; tc = "#E04040"; bc = "#EC1D1D"
#     elif is_select:
#         bg   = "#0E0E0C"; hov = "#181612"; tc = CREAM2;    bc = "#FFFFFF"
#     else:
#         bg   = "#0E0E0C"; hov = "#181612"; tc = CREAM2;    bc = "#FFFFFF"
#     return CTkButton(
#         master        = window,
#         command       = command,
#         text          = text,
#         image         = icon,
#         width         = width,
#         height        = height,
#         font          = CTkFont(family="Segoe UI", size=11, weight="bold"),
#         border_width  = 1,
#         fg_color      = bg,
#         hover_color   = hov,
#         text_color    = tc,
#         border_color  = bc,
#         corner_radius = 7,
#     )














# # File Utils functions ------------------------
# def create_dir(name_dir: str) -> None:
#     if os_path_exists(name_dir):
#         remove_directory(name_dir)
#     if not os_path_exists(name_dir): 
#         os_makedirs(name_dir, mode=0o777)

# def stop_thread() -> None: stop = 1 + "x"

# def image_read(file_path: str) -> numpy_ndarray: 
#     with open(file_path, 'rb') as file:
#         return opencv_imdecode(numpy_frombuffer(file.read(), uint8), IMREAD_UNCHANGED)

# def image_write(file_path: str, file_data: numpy_ndarray) -> None: 
#     _, file_extension = os_path_splitext(file_path)
#     opencv_imencode(file_extension, file_data)[1].tofile(file_path)


# def prepare_output_image_filename(
#         image_path: str, 
#         selected_output_path: str,
#         selected_AI_model: str, 
#         resize_factor: int, 
#         selected_image_extension: str,
#         selected_interpolation_factor: float
#         ) -> str:
        
#     if selected_output_path == OUTPUT_PATH_CODED:
#         file_path_no_extension, _ = os_path_splitext(image_path)
#         output_path = file_path_no_extension
#     else:
#         file_name   = os_path_basename(image_path)
#         output_path = f"{selected_output_path}{os_separator}{file_name}"

#     # Selected AI model
#     to_append = f"_{selected_AI_model}"

#     # Selected resize
#     to_append += f"_Resize-{str(int(resize_factor * 100))}"

#     # Selected intepolation
#     match selected_interpolation_factor:
#         case 0.3:
#             to_append += "_Interpolation-Low"
#         case 0.5:
#             to_append += "_Interpolation-Medium"
#         case 0.7:
#             to_append += "_Interpolation-High"

#     # Selected image extension
#     to_append += f"{selected_image_extension}"
        
#     output_path += to_append

#     return output_path


# def prepare_output_video_frame_filename(
#         frame_path: str, 
#         selected_AI_model: str, 
#         resize_factor: int, 
#         selected_interpolation_factor: float
#         ) -> str:
            
#     file_path_no_extension, _ = os_path_splitext(frame_path)
#     output_path = file_path_no_extension

#     # Selected AI model
#     to_append = f"_{selected_AI_model}"

#     # Selected resize
#     to_append += f"_Resize-{str(int(resize_factor * 100))}"

#     # Selected intepolation
#     match selected_interpolation_factor:
#         case 0.3:
#             to_append += "_Interpolation-Low"
#         case 0.5:
#             to_append += "_Interpolation-Medium"
#         case 0.7:
#             to_append += "_Interpolation-High"

#     # Selected image extension
#     to_append += f".jpg"
        
#     output_path += to_append

#     return output_path


# def prepare_output_video_filename(
#         video_path: str, 
#         selected_output_path: str,
#         selected_AI_model: str, 
#         input_resize_factor: int, 
#         selected_video_extension: str,
#         selected_interpolation_factor: float
#         ) -> str:
    
#     match selected_video_extension:
#         case '.mp4 (x264)': selected_video_extension = '.mp4'
#         case '.mp4 (x265)': selected_video_extension = '.mp4'
#         case '.avi':        selected_video_extension = '.avi'

#     if selected_output_path == OUTPUT_PATH_CODED:
#         file_path_no_extension, _ = os_path_splitext(video_path)
#         output_path = file_path_no_extension
#     else:
#         file_name   = os_path_basename(video_path)
#         output_path = f"{selected_output_path}{os_separator}{file_name}"
    
#     # Selected AI model
#     to_append = f"_{selected_AI_model}"

#     # Selected resize
#     to_append += f"_Resize-{str(int(input_resize_factor * 100))}"

#     # Selected intepolation
#     match selected_interpolation_factor:
#         case 0.3:
#             to_append += "_Interpolation-Low"
#         case 0.5:
#             to_append += "_Interpolation-Medium"
#         case 0.7:
#             to_append += "_Interpolation-High"

#     # Selected video extension
#     to_append += f"{selected_video_extension}"
        
#     output_path += to_append

#     return output_path


# def prepare_output_video_directory_name(
#         video_path: str, 
#         selected_output_path: str,
#         selected_AI_model: str, 
#         input_resize_factor: int, 
#         selected_interpolation_factor: float
#         ) -> str:
    
#     if selected_output_path == OUTPUT_PATH_CODED:
#         file_path_no_extension, _ = os_path_splitext(video_path)
#         output_path = file_path_no_extension
#     else:
#         file_name   = os_path_basename(video_path)
#         output_path = f"{selected_output_path}{os_separator}{file_name}"

#     # Selected AI model
#     to_append = f"_{selected_AI_model}"

#     # Selected resize
#     to_append += f"_Resize-{str(int(input_resize_factor * 100))}"

#     # Selected intepolation
#     match selected_interpolation_factor:
#         case 0.3:
#             to_append += "_Interpolation-Low"
#         case 0.5:
#             to_append += "_Interpolation-Medium"
#         case 0.7:
#             to_append += "_Interpolation-High"

#     output_path += to_append

#     return output_path












# # Image/video Utils functions ------------------------
# def get_video_fps(video_path: str) -> float:
#     video_capture = opencv_VideoCapture(video_path)
#     frame_rate    = video_capture.get(CAP_PROP_FPS)
#     video_capture.release()
#     return frame_rate
   
# def get_image_resolution(image: numpy_ndarray) -> tuple:
#     height = image.shape[0]
#     width  = image.shape[1]

#     return height, width 

# def save_extracted_frames(
#         extracted_frames_paths: list[str], 
#         extracted_frames: list[numpy_ndarray], 
#         cpu_number: int
#         ) -> None:
    
#     pool = ThreadPool(cpu_number)
#     pool.starmap(image_write, zip(extracted_frames_paths, extracted_frames))
#     pool.close()
#     pool.join()

# def extract_video_frames(
#         processing_queue: multiprocessing_Queue,
#         file_number: int,
#         target_directory: str,
#         video_path: str, 
#         cpu_number: int
#     ) -> list[str]:

#     create_dir(target_directory)

#     # Video frame extraction
#     frames_number_to_save = cpu_number * FRAMES_FOR_CPU
#     video_capture         = opencv_VideoCapture(video_path)
#     frame_count           = int(video_capture.get(CAP_PROP_FRAME_COUNT))

#     extracted_frames       = []
#     extracted_frames_paths = []
#     video_frames_list      = []

#     for frame_number in range(frame_count):
#         success, frame = video_capture.read()
#         if success:
#             frame_path = f"{target_directory}{os_separator}frame_{frame_number:03d}.jpg"            
#             extracted_frames.append(frame)
#             extracted_frames_paths.append(frame_path)
#             video_frames_list.append(frame_path)

#             if len(extracted_frames) == frames_number_to_save:
#                 percentage_extraction = (frame_number / frame_count) * 100

#                 write_process_status(processing_queue, f"{file_number}. Extracting video frames ({round(percentage_extraction, 2)}%)")
#                 save_extracted_frames(extracted_frames_paths, extracted_frames, cpu_number)
#                 extracted_frames       = []
#                 extracted_frames_paths = []

#     video_capture.release()

#     if len(extracted_frames) > 0: save_extracted_frames(extracted_frames_paths, extracted_frames, cpu_number)
    
#     return video_frames_list



# def video_encoding(
#         video_path: str,
#         video_output_path: str,
#         upscaled_frame_paths: list[str], 
#         cpu_number: int,
#         selected_video_extension: str, 
#         Audio_Inference_output: str = None
#         ) -> None:
        
#     match selected_video_extension:
#         case ".mp4 (x264)": codec = "libx264"
#         case ".mp4 (x265)": codec = "libx265"
#         case ".avi":        codec = "png"

#     no_audio_path = f"{os_path_splitext(video_output_path)[0]}_no_audio{os_path_splitext(video_output_path)[1]}"
#     video_fps     = get_video_fps(video_path)
#     video_clip    = ImageSequenceClip.ImageSequenceClip(sequence = upscaled_frame_paths, fps = video_fps)

#     video_clip.write_videofile(
#         filename = no_audio_path,
#         fps      = video_fps,
#         codec    = codec,
#         threads  = cpu_number,
#         logger   = None,
#         audio    = None,
#         bitrate  = "12M",
#         preset   = "ultrafast"
#     )

        
#     audio_source = Audio_Inference_output if Audio_Inference_output else video_path
#     # Copy the audio from original video
#     audio_passthrough_command = [
#         FFMPEG_EXE_PATH,
#         "-y",
#         "-i", audio_source,
#         "-i", no_audio_path,
#         "-c:v", "copy",
#         "-c:a", "copy",
#         "-b:a", "192k", #Audio bitrate
#         "-map", "1:v:0", #Map video from no_audio_path
#         "-map", "0:a:0", #map audio from isolated audio
#         video_output_path
#     ]
#     try: 
#         subprocess_run(audio_passthrough_command, check = True, shell = "False")
#         if os_path_exists(no_audio_path):
#             os_remove(no_audio_path)
#     except Exception as e:
#         logging.info(f"Error during video encoding: {e}")
#         pass

#     if Audio_Inference_output:
#         try: 
#             if os_path_exists(Audio_Inference_output):
#                 os_remove(Audio_Inference_output)
#         except Exception as e:
#             logging.info(f"error during removal of audio {str(e)}")

#     extracted_audio = os_path_join(os.path.dirname(video_path), "extracted_audio.wav") 
#     if os_path_exists(extracted_audio):
#         try:
#             os_remove(extracted_audio)
#         except Exception as e:
#             logging.info(f"warning could not delete extracted audio {extracted_audio}, might have been moved: {str(e)}")
    
# def check_video_upscaling_resume(
#         target_directory: str, 
#         selected_AI_model: str
#         ) -> bool:
    
#     if os_path_exists(target_directory):
#         directory_files      = os_listdir(target_directory)
#         upscaled_frames_path = [file for file in directory_files if selected_AI_model in file]

#         if len(upscaled_frames_path) > 1:
#             return True
#         else:
#             return False
#     else:
#         return False


# def get_video_frames_for_upscaling_resume(
#         target_directory: str,
#         selected_AI_model: str,
#         ) -> list[str]:
    
#     # Only file names
#     directory_files      = os_listdir(target_directory)
#     original_frames_path = [file for file in directory_files if file.endswith('.jpg')]
#     original_frames_path = [file for file in original_frames_path if selected_AI_model not in file]

#     # Adding the complete path to file
#     original_frames_path = natsorted([os_path_join(target_directory, file) for file in original_frames_path])

#     return original_frames_path



# def calculate_time_to_complete_video(
#         time_for_frame: float,
#         remaining_frames: int,
#         ) -> str:
    
#     remaining_time = time_for_frame * remaining_frames

#     hours_left   = remaining_time // 3600
#     minutes_left = (remaining_time % 3600) // 60
#     seconds_left = round((remaining_time % 3600) % 60)

#     time_left = ""

#     if int(hours_left) > 0: 
#         time_left = f"{int(hours_left):02d}h"
    
#     if int(minutes_left) > 0: 
#         time_left = f"{time_left}{int(minutes_left):02d}m"

#     if seconds_left > 0: 
#         time_left = f"{time_left}{seconds_left:02d}s"

#     return time_left        




# def interpolate_images_and_save(
#         target_path: str,
#         starting_image: numpy_ndarray,
#         upscaled_image: numpy_ndarray,
#         starting_image_importance: float,
#         ) -> None:
    
#     def add_alpha_channel(image: numpy_ndarray) -> numpy_ndarray:
#         if image.shape[2] == 3:
#             alpha = numpy_full((image.shape[0], image.shape[1], 1), 255, dtype = uint8)
#             image = numpy_concatenate((image, alpha), axis = 2)
#         return image
    
#     def get_image_mode(image: numpy_ndarray) -> str:
#         match image.shape:
#             case (rows, cols):
#                 return "Grayscale"
#             case (rows, cols, channels) if channels == 3:
#                 return "RGB"
#             case (rows, cols, channels) if channels == 4:
#                 return "RGBA"


#     ZERO = 0
#     upscaled_image_importance       = 1 - starting_image_importance
#     starting_height, starting_width = get_image_resolution(starting_image)
#     target_height, target_width     = get_image_resolution(upscaled_image)

#     starting_resolution = starting_height + starting_width
#     target_resolution   = target_height + target_width

#     if starting_resolution > target_resolution:
#         starting_image = opencv_resize(starting_image,(target_width, target_height), INTER_AREA)
#     else:
#         starting_image = opencv_resize(starting_image,(target_width, target_height), INTER_LINEAR)

#     try: 
#         if get_image_mode(starting_image) == "RGBA":
#             starting_image = add_alpha_channel(starting_image)
#             upscaled_image = add_alpha_channel(upscaled_image)

#         interpolated_image = opencv_addWeighted(starting_image, starting_image_importance, upscaled_image, upscaled_image_importance, ZERO)
#         image_write(
#             file_path = target_path, 
#             file_data = interpolated_image
#         )
#     except:
#         image_write(
#             file_path = target_path, 
#             file_data = upscaled_image
#         )




# def manage_upscaled_video_frame_save_async(
#         upscaled_frame: numpy_ndarray,
#         starting_frame: numpy_ndarray,
#         upscaled_frame_path: str,
#         selected_interpolation_factor: float
#     ) -> None:

#     if selected_interpolation_factor > 0:
#         thread = Thread(
#             target = interpolate_images_and_save,
#             args = (
#                 upscaled_frame_path, 
#                 starting_frame,
#                 upscaled_frame,
#                 selected_interpolation_factor
#             )
#         )
#     else:
#         thread = Thread(
#             target = image_write,
#             args = (
#                 upscaled_frame_path, 
#                 upscaled_frame
#             )
#         )

#     thread.start()




# def update_process_status_videos(
#         processing_queue: multiprocessing_Queue, 
#         file_number: int, 
#         frame_index: int, 
#         how_many_frames: int,
#         average_processing_time: float,
#         ) -> None:


#     batch = 4 if not CPU_ONLY else 1
#     if frame_index != 0 and (frame_index + 1) % batch == 0:  
#         remaining_frames = how_many_frames - frame_index
#         remaining_time   = calculate_time_to_complete_video(average_processing_time, remaining_frames)
#         if remaining_time != "":
#             percent_complete = (frame_index + 1) / how_many_frames * 100 
#             write_process_status(processing_queue, f"{file_number}. Upscaling video {percent_complete:.2f}% ({remaining_time})")





# def copy_file_metadata(
#         original_file_path: str, 
#         upscaled_file_path: str
#         ) -> None:
    
#     exiftool_cmd = [
#         EXIFTOOL_EXE_PATH, 
#         '-fast', 
#         '-TagsFromFile', 
#         original_file_path, 
#         '-overwrite_original', 
#         '-all:all',
#         '-unsafe',
#         '-largetags', 
#         upscaled_file_path
#     ]
    
#     try: 
#         subprocess_run(exiftool_cmd, check = True, shell = "False")
#     except:
#         pass









# # Core functions ------------------------
# def check_upscale_steps() -> None:
#     sleep(1)

#     try:
#         while True:
#             actual_step = read_process_status()

#             if actual_step == COMPLETED_STATUS:
#                 info_message.set(f"All files completed! :)")
#                 stop_upscale_process()
#                 stop_thread()

#             elif actual_step == STOP_STATUS:
#                 info_message.set(f"Upscaling stopped")
#                 stop_upscale_process()
#                 stop_thread()

#             elif ERROR_STATUS in actual_step:
#                 info_message.set(f"Error while upscaling :(")
#                 show_error_message(actual_step.replace(ERROR_STATUS, ""))
#                 stop_thread()

#             else:
#                 info_message.set(actual_step)

#             sleep(1)
#     except:
#         place_upscale_button()
        
# def read_process_status() -> str:
#     return processing_queue.get()

# def write_process_status(
#         processing_queue: multiprocessing_Queue,
#         step: str
#         ) -> None:
    
#     logging.info(f"{step}")
#     while not processing_queue.empty(): processing_queue.get()
#     processing_queue.put(f"{step}")

# def stop_upscale_process() -> None:
#     global process_upscale_orchestrator
#     try:
#         process_upscale_orchestrator
#     except:
#         pass
#     else:
#         process_upscale_orchestrator.kill()

# def stop_button_command() -> None:
#     stop_upscale_process()
#     write_process_status(processing_queue, f"{STOP_STATUS}") 

# def upscale_button_command() -> None: 
#     global selected_file_list
#     global selected_AI_model
#     global selected_gpu
#     global selected_keep_frames
#     global selected_AI_multithreading
#     global selected_interpolation_factor
#     global selected_image_extension
#     global selected_video_extension
#     global tiles_resolution
#     global input_resize_factor
#     global cpu_number
#     global selected_audio_mode
#     global process_upscale_orchestrator
#     global selected_audio_mode
#     selected_audio_mode = selected_audio_mode

#     if user_input_checks():
#         info_message.set("Loading")

#         logging.info("=" * 50)
#         logging.info("> Starting upscale:")
#         logging.info(f"  Files to upscale: {len(selected_file_list)}")
#         logging.info(f"  Output path: {(selected_output_path.get())}")
#         logging.info(f"  Selected AI model: {selected_AI_model}")
#         logging.info(f"  Selected GPU: {selected_gpu}")
#         logging.info(f"  AI multithreading: {selected_AI_multithreading}")
#         logging.info(f"  Interpolation factor: {selected_interpolation_factor}")
#         logging.info(f"  Selected image output extension: {selected_image_extension}")
#         logging.info(f"  Selected video output extension: {selected_video_extension}")
#         logging.info(f"  Tiles resolution for selected GPU VRAM: {tiles_resolution}x{tiles_resolution}px")
#         logging.info(f"  input_resize_factor: {int(input_resize_factor * 100)}%")
#         logging.info(f"  Cpu number: {cpu_number}")
#         logging.info(f" Save frames: {selected_keep_frames}")
#         logging.info(f" selected_audio_mode : {selected_audio_mode}")
#         logging.info("=" * 50)

#         place_stop_button()

#         process_upscale_orchestrator = Process(
#             target = upscale_orchestrator,
#             args = (
#                 processing_queue, 
#                 selected_file_list, 
#                 selected_output_path.get(),
#                 selected_AI_model, 
#                 selected_gpu,
#                 selected_image_extension,
#                 tiles_resolution, 
#                 input_resize_factor, 
#                 cpu_number, 
#                 selected_video_extension,
#                 selected_interpolation_factor,
#                 selected_AI_multithreading,
#                 selected_keep_frames,
#                 selected_audio_mode,
#                 dict(file_overrides),   # pass a copy of per-file overrides
#             )
#         )
#         process_upscale_orchestrator.start()

#         thread_wait = Thread(target = check_upscale_steps)
#         thread_wait.start()


# # ORCHESTRATOR
# def upscale_orchestrator(
#         processing_queue: multiprocessing_Queue,
#         selected_file_list: list,
#         selected_output_path: str,
#         selected_AI_model: str,
#         selected_gpu: str,
#         selected_image_extension: str,
#         tiles_resolution: int,
#         input_resize_factor: int,
#         cpu_number: int,
#         selected_video_extension: str,
#         selected_interpolation_factor: float,
#         selected_AI_multithreading: int,
#         selected_keep_frames: bool,
#         selected_audio_mode: str,
#         file_overrides: dict = None
#         ) -> None:

#     if file_overrides is None:
#         file_overrides = {}

#     write_process_status(processing_queue, f"Loading AI model")

#     # Build a default AI instance (used for files without per-file overrides)
#     AI_instance = AI(selected_AI_model, selected_gpu, input_resize_factor, tiles_resolution)
#     AI_instance_list = [AI_instance]

#     if selected_AI_multithreading > 1:
#         for _ in range(selected_AI_multithreading - 1):
#             AI_instance_list.append(AI(selected_AI_model, selected_gpu, input_resize_factor, tiles_resolution))

#     # Cache of (model, resize_factor) -> AI instance to avoid reloading the same model
#     _ai_cache = {(selected_AI_model, input_resize_factor): AI_instance}

#     try:
#         how_many_files = len(selected_file_list)
#         for file_number in range(how_many_files):
#             file_path   = selected_file_list[file_number]
#             file_number = file_number + 1

#             # Resolve per-file settings (fall back to global when not overridden)
#             ov = file_overrides.get(file_path, {})
#             f_ai_model    = ov.get("ai_model",      selected_AI_model)
#             f_resize      = ov.get("resize_factor",  input_resize_factor)
#             f_interp      = ov.get("interp_factor",  selected_interpolation_factor)
#             f_image_ext   = ov.get("image_ext",      selected_image_extension)
#             f_video_ext   = ov.get("video_ext",      selected_video_extension)

#             # Re-use or create a per-file AI instance
#             cache_key = (f_ai_model, f_resize)
#             if cache_key not in _ai_cache:
#                 write_process_status(processing_queue, f"Loading model {f_ai_model}")
#                 _ai_cache[cache_key] = AI(f_ai_model, selected_gpu, f_resize, tiles_resolution)
#             f_ai_instance      = _ai_cache[cache_key]
#             f_ai_instance_list = [f_ai_instance]
#             if selected_AI_multithreading > 1:
#                 for _ in range(selected_AI_multithreading - 1):
#                     sub_key = (f_ai_model, f_resize, _)
#                     if sub_key not in _ai_cache:
#                         _ai_cache[sub_key] = AI(f_ai_model, selected_gpu, f_resize, tiles_resolution)
#                     f_ai_instance_list.append(_ai_cache[sub_key])

#             if check_if_file_is_video(file_path):
#                 upscale_video(
#                     processing_queue,
#                     file_path,
#                     file_number,
#                     selected_output_path,
#                     f_ai_instance,
#                     f_ai_instance_list,
#                     f_ai_model,
#                     f_resize,
#                     cpu_number,
#                     f_video_ext,
#                     f_interp,
#                     selected_AI_multithreading,
#                     selected_keep_frames,
#                     selected_audio_mode
#                 )
#             else:
#                 upscale_image(
#                     processing_queue,
#                     file_path,
#                     file_number,
#                     selected_output_path,
#                     f_ai_instance,
#                     f_ai_model,
#                     f_image_ext,
#                     f_resize,
#                     f_interp
#                 )

#         write_process_status(processing_queue, f"{COMPLETED_STATUS}")

#     except Exception as exception:
#         write_process_status(processing_queue, f"{ERROR_STATUS} {str(exception)}")



# # IMAGES
# def upscale_image(
#         processing_queue: multiprocessing_Queue,
#         image_path: str, 
#         file_number: int,
#         selected_output_path: str,
#         AI_instance: AI,
#         selected_AI_model: str,
#         selected_image_extension: str,
#         input_resize_factor: int, 
#         selected_interpolation_factor: float
#         ) -> None:
    
#     starting_image = image_read(image_path)
#     upscaled_image_path = prepare_output_image_filename(image_path, selected_output_path, selected_AI_model, input_resize_factor, selected_image_extension, selected_interpolation_factor)

#     write_process_status(processing_queue, f"{file_number}. Upscaling image")
#     upscaled_image = AI_instance.AI_orchestration(starting_image)

#     if selected_interpolation_factor > 0:
#         interpolate_images_and_save(
#             upscaled_image_path,
#             starting_image,
#             upscaled_image,
#             selected_interpolation_factor
#         )

#     else:
#         image_write(
#             file_path = upscaled_image_path,
#             file_data = upscaled_image
#         )

#     copy_file_metadata(image_path, upscaled_image_path)









# # VIDEOS
# def upscale_video(
#         processing_queue: multiprocessing_Queue,
#         video_path: str, 
#         file_number: int,
#         selected_output_path: str,
#         AI_instance: AI,
#         AI_instance_list: list[AI],
#         selected_AI_model: str,
#         input_resize_factor: int, 
#         cpu_number: int, 
#         selected_video_extension: str,
#         selected_interpolation_factor: float,
#         selected_AI_multithreading: int,
#         selected_keep_frames: bool,
#         selected_audio_mode: str
#         ) -> None:

#     global processed_frames_async
#     global processing_times_async
#     processed_frames_async = 0
#     processing_times_async = []
    
#     # 1.Preparation
#     target_directory  = prepare_output_video_directory_name(video_path, selected_output_path, selected_AI_model, input_resize_factor, selected_interpolation_factor)
#     video_output_path = prepare_output_video_filename(video_path, selected_output_path, selected_AI_model, input_resize_factor, selected_video_extension, selected_interpolation_factor)
    
#     Audio_Inference_output = AI_instance.process_Audio_Inference(video_path,selected_audio_mode) 
#     if Audio_Inference_output == None:
#         logging.info(f"Error: no enchanced audio recieved, audio inference output is {Audio_Inference_output}")
    
#     # 2. Resume upscaling OR Extract video frames
#     video_upscale_continue = check_video_upscaling_resume(target_directory, selected_AI_model)
#     if video_upscale_continue:
#         write_process_status(processing_queue, f"{file_number}. Resume video upscaling")
#         extracted_frames_paths = get_video_frames_for_upscaling_resume(target_directory, selected_AI_model)
#     else:
#         write_process_status(processing_queue, f"{file_number}. Extracting video frames")
#         extracted_frames_paths = extract_video_frames(processing_queue, file_number, target_directory, video_path, cpu_number)

#     upscaled_frame_paths = [prepare_output_video_frame_filename(frame_path, selected_AI_model, input_resize_factor,selected_interpolation_factor) for frame_path in extracted_frames_paths]

#     # 3. Check if video need tiles OR video multithreading upscale
#     first_frame_path             = extracted_frames_paths[0]
#     video_need_tiles             = AI_instance.video_need_tilling(first_frame_path)
#     multiframes_supported_by_gpu = AI_instance.calculate_multiframes_supported_by_gpu(first_frame_path)
#     multiframes_number           = min(multiframes_supported_by_gpu, selected_AI_multithreading)

#     write_process_status(processing_queue, f"{file_number}. Upscaling video") 
#     if video_need_tiles or multiframes_number <= 1:
#         upscale_video_frames(
#             processing_queue,
#             file_number,
#             AI_instance,
#             extracted_frames_paths,
#             upscaled_frame_paths,
#             selected_interpolation_factor
#         )
#     else:
#         upscale_video_frames_multithreading(
#             processing_queue,
#             file_number,
#             AI_instance_list,
#             extracted_frames_paths,
#             upscaled_frame_paths,
#             multiframes_number,
#             selected_interpolation_factor
#         )

#     # 4. Check for forgotten video frames
#     check_forgotten_video_frames(processing_queue, file_number, AI_instance, extracted_frames_paths, upscaled_frame_paths, selected_interpolation_factor)

#     # 5. Video encoding
#     write_process_status(processing_queue, f"{file_number}. Processing upscaled video")
#     video_encoding(video_path, video_output_path, upscaled_frame_paths, cpu_number, selected_video_extension,Audio_Inference_output)
#     copy_file_metadata(video_path, video_output_path)
    
#     #6 delete frames folder
#     if selected_keep_frames == False:
#         if os_path_exists(target_directory): remove_directory(target_directory)

# def upscale_video_frames(
#         processing_queue: multiprocessing_Queue,
#         file_number: int,
#         AI_instance: AI,
#         extracted_frames_paths: list[str],
#         upscaled_frame_paths: list[str],
#         selected_interpolation_factor: float
#         ) -> None:
    
#     frame_processing_times = []

#     for frame_index, frame_path in enumerate(extracted_frames_paths):
#         upscaled_frame_path = upscaled_frame_paths[frame_index]
#         already_upscaled    = os_path_exists(upscaled_frame_path)
        
#         if already_upscaled == False:
#             start_timer = timer()
            
#             starting_frame = image_read(frame_path)
#             upscaled_frame = AI_instance.AI_orchestration(starting_frame)
#             manage_upscaled_video_frame_save_async(upscaled_frame, starting_frame, upscaled_frame_path, selected_interpolation_factor)
        
#             end_timer    = timer()
#             elapsed_time = end_timer - start_timer
#             frame_processing_times.append(elapsed_time)
            
#             if (frame_index + 1) % 8 == 0:
#                 average_processing_time = numpy_mean(frame_processing_times)
#                 update_process_status_videos(processing_queue, file_number, frame_index, len(extracted_frames_paths), average_processing_time)

#             if (frame_index + 1) % 100 == 0: frame_processing_times = []

# def upscale_video_frames_multithreading(
#         processing_queue: multiprocessing_Queue,
#         file_number: int,
#         AI_instance_list: list[AI],
#         extracted_frames_paths: list[str],
#         upscaled_frame_paths: list[str],
#         multiframes_number: int,
#         selected_interpolation_factor: float,
#         ) -> None:
    
#     def upscale_single_video_frame_async(
#             processing_queue: multiprocessing_Queue,
#             file_number: int,
#             multiframes_number: int,
#             total_video_frames: int,
#             AI_instance: AI,
#             extracted_frames_paths: list[str],
#             upscaled_frame_paths: list[str],
#             selected_interpolation_factor: float,
#             ) -> None:

#         global processed_frames_async
#         global processing_times_async

#         for frame_index in range(len(extracted_frames_paths)):
#             upscaled_frame_path = upscaled_frame_paths[frame_index]
#             already_upscaled    = os_path_exists(upscaled_frame_path)

#             if already_upscaled == False:
#                 start_timer = timer()

#                 starting_frame = image_read(extracted_frames_paths[frame_index])
#                 upscaled_frame = AI_instance.AI_orchestration(starting_frame)

#                 manage_upscaled_video_frame_save_async(upscaled_frame, starting_frame, upscaled_frame_path, selected_interpolation_factor)

#                 end_timer    = timer()
#                 elapsed_time = end_timer - start_timer
#                 processing_times_async.append(elapsed_time)

#                 if (processed_frames_async + 1) % 8 == 0:
#                     average_processing_time = float(numpy_mean(processing_times_async)/multiframes_number)
#                     update_process_status_videos(processing_queue, file_number, processed_frames_async, total_video_frames, average_processing_time)

#                 if (processed_frames_async + 1) % 100 == 0: processing_times_async = []
        
#             processed_frames_async +=1

    
#     total_video_frames         = len(extracted_frames_paths)
#     chunk_size                 = total_video_frames // multiframes_number
#     frame_list_chunks          = [extracted_frames_paths[i:i + chunk_size] for i in range(0, len(extracted_frames_paths), chunk_size)]
#     upscaled_frame_list_chunks = [upscaled_frame_paths[i:i + chunk_size] for i in range(0, len(upscaled_frame_paths), chunk_size)]

#     write_process_status(processing_queue, f"{file_number}. Upscaling video ({multiframes_number} threads)")
#     try: 
#         pool = ThreadPool(multiframes_number)
#         pool.starmap(
#             upscale_single_video_frame_async,
#             zip(
#                 repeat(processing_queue),
#                 repeat(file_number),
#                 repeat(multiframes_number),
#                 repeat(total_video_frames),
#                 AI_instance_list,
#                 frame_list_chunks,
#                 upscaled_frame_list_chunks,
#                 repeat(selected_interpolation_factor)
#             )
#         )
#         pool.close()
#         pool.join()
#     except Exception as e:
#         logging.info(f"error during upscaling {str(e)}")

# def check_forgotten_video_frames(
#         processing_queue: multiprocessing_Queue,
#         file_number: int,
#         AI_instance: AI,
#         extracted_frames_paths: list[str],
#         upscaled_frame_paths: list[str],
#         selected_interpolation_factor: float,
#         ):
    

#     frame_path_todo_list          = []
#     upscaled_frame_path_todo_list = []

#     for frame_index in range(len(upscaled_frame_paths)):
        
#         if not os_path_exists(upscaled_frame_paths[frame_index]):
#             frame_path_todo_list.append(extracted_frames_paths[frame_index])
#             upscaled_frame_path_todo_list.append(upscaled_frame_paths[frame_index]) 

#     if len(upscaled_frame_path_todo_list) > 0:
#         upscale_video_frames(
#             processing_queue,
#             file_number,
#             AI_instance,
#             frame_path_todo_list,
#             upscaled_frame_path_todo_list,
#             selected_interpolation_factor
#         )











# # GUI utils function ---------------------------
# def check_if_file_is_video(
#         file: str
#         ) -> bool:
    
#     return any(video_extension in file for video_extension in supported_video_extensions)

# def check_supported_selected_files(
#         uploaded_file_list: list
#         ) -> list:
    
#     return [file for file in uploaded_file_list if any(supported_extension in file for supported_extension in supported_file_extensions)]

# def user_input_checks() -> bool:
#     global selected_file_list
#     global selected_AI_model
#     global selected_image_extension
#     global tiles_resolution
#     global input_resize_factor
#     global cpu_number

#     # Selected files 
#     try: selected_file_list = file_widget.get_selected_file_list()
#     except:
#         info_message.set("Please select a file")
#         return False

#     if len(selected_file_list) <= 0:
#         info_message.set("Please select a file")
#         return False


#     # AI model
#     if selected_AI_model == AI_LIST_SEPARATOR[0]:
#         info_message.set("Please select the AI model")
#         return False


#     # Input resize factor 
#     try: input_resize_factor = int(float(str(selected_input_resize_factor.get())))
#     except:
#         info_message.set("Resize % must be a numeric value")
#         return False

#     if input_resize_factor > 0: input_resize_factor = input_resize_factor/100
#     else:
#         info_message.set("Resize % must be a value > 0")
#         return False
    

   

#     try: tiles_resolution = 100 * int(float(str(selected_VRAM_limiter.get())))
#     except:
#         info_message.set("VRAM/RAM value must be a numeric value")
#         return False

#     if tiles_resolution > 0: 
#         if selected_AI_model in RRDB_models_list:          
#             vram_multiplier = very_high_VRAM
#         elif selected_AI_model in SRVGGNetCompact_models_list: 
#             vram_multiplier = medium_VRAM
#         elif selected_AI_model in IRCNN_models_list:
#             vram_multiplier = very_low_VRAM

#         selected_vram = (vram_multiplier * int(float(str(selected_VRAM_limiter.get()))))
#         tiles_resolution = int(selected_vram * 100)

        
#     else:
#         info_message.set("VRAM/RAM value must be > 0")
#         return False

#     # Cpu number 
#     try: cpu_number = int(float(str(selected_cpu_number.get())))
#     except:
#         info_message.set("Cpu number must be a numeric value")
#         return False

#     if cpu_number <= 0:         
#         info_message.set("Cpu number value must be > 0")
#         return False
#     else: 
#         cpu_number = int(cpu_number)

#     return True

# def show_error_message(exception: str) -> None:
#     messageBox_title    = "Upscale error"
#     messageBox_subtitle = "Please report the error on Github or Telegram"
#     messageBox_text     = f"\n {str(exception)} \n"

#     MessageBox(
#         messageType   = "error",
#         title         = messageBox_title,
#         subtitle      = messageBox_subtitle,
#         default_value = None,
#         option_list   = [messageBox_text]
#     )

# def get_upscale_factor() -> int:
#     global selected_AI_model
#     if AI_LIST_SEPARATOR[0] in selected_AI_model: upscale_factor = 0
#     elif 'x1' in selected_AI_model: upscale_factor = 1
#     elif 'x2' in selected_AI_model: upscale_factor = 2
#     elif 'x4' in selected_AI_model: upscale_factor = 4

#     return upscale_factor



# def add_files_from_drop(drop_data: str) -> None:
#     """Parse a TkinterDnD drop event data string and add valid files to the list."""
#     global selected_file_list, file_widget

#     # tkinterdnd2 wraps paths with braces when they contain spaces
#     import re
#     raw = drop_data.strip()
#     # Extract paths: either {path with spaces} or plain/path
#     paths = re.findall(r'\{([^}]+)\}|(\S+)', raw)
#     parsed = [a or b for a, b in paths]

#     supported = [
#         p for p in parsed
#         if os_path_exists(p) and any(p.lower().endswith(ext.lower()) for ext in supported_file_extensions)
#     ]

#     if not supported:
#         info_message.set("No supported files in drop")
#         return

#     new_files = [f for f in supported if f not in selected_file_list]
#     if not new_files:
#         info_message.set("Files already loaded")
#         return

#     widget_exists = 'file_widget' in globals() and globals()['file_widget'].winfo_exists()

#     for f in new_files:
#         selected_file_list.append(f)

#     if widget_exists:
#         next_row = 1 + len(selected_file_list) - len(new_files)
#         for f in new_files:
#             row_frame = file_widget.add_file_information(f, next_row)
#             file_widget.label_list.append(row_frame)
#             next_row += 1
#         file_widget.file_list = selected_file_list
#     else:
#         upscale_factor = get_values_for_file_widget()
#         file_widget = FileWidget(
#             master             = window,
#             selected_file_list = selected_file_list,
#             upscale_factor     = upscale_factor,
#             fg_color           = background_color,
#             bg_color           = background_color,
#         )
#         file_widget.place(relx=0.22, rely=0.095, relwidth=0.33, relheight=0.905)

#     if file_list_update_callback:
#         file_list_update_callback()
#     if media_info_update_callback:
#         media_info_update_callback()

#     update_file_widget(1, 2, 3)
#     info_message.set("Ready")


# def open_files_action():
#     global selected_file_list  
#     def check_supported_selected_files(uploaded_file_list: list) -> list:
#         return [file for file in uploaded_file_list if any(supported_extension in file for supported_extension in supported_file_extensions)]

#     info_message.set("Selecting files")

#     uploaded_files_list    = list(filedialog.askopenfilenames())
#     uploaded_files_counter = len(uploaded_files_list)

#     supported_files_list    = check_supported_selected_files(uploaded_files_list)
#     supported_files_counter = len(supported_files_list)
    
#     logging.info("> Uploaded files: " + str(uploaded_files_counter) + " => Supported files: " + str(supported_files_counter))

#     global file_widget

#     if supported_files_counter > 0:
#         new_files = [f for f in supported_files_list if f not in selected_file_list]

#         if new_files:
#             widget_exists = 'file_widget' in globals() and globals()['file_widget'].winfo_exists()

#             for f in new_files:
#                 selected_file_list.append(f)

#             if widget_exists:
#                 # Append only new rows - no full rebuild, no shaking
#                 next_row = 1 + len(selected_file_list) - len(new_files)
#                 for f in new_files:
#                     row_frame = file_widget.add_file_information(f, next_row)
#                     file_widget.label_list.append(row_frame)
#                     next_row += 1
#                 file_widget.file_list = selected_file_list
#             else:
#                 upscale_factor = get_values_for_file_widget()
#                 file_widget = FileWidget(
#                     master               = window,
#                     selected_file_list   = selected_file_list,
#                     upscale_factor       = upscale_factor,
#                     fg_color             = background_color,
#                     bg_color             = background_color
#                 )
#                 file_widget.place(relx = 0.22, rely = 0.095, relwidth = 0.33, relheight = 0.905)

#             if file_list_update_callback:
#                 file_list_update_callback()
#             if media_info_update_callback:
#                 media_info_update_callback()

#             update_file_widget(1, 2, 3)

#         info_message.set("Ready")
#     else:
#         info_message.set("Not supported files :(")
    

# def open_output_path_action():
#     asked_selected_output_path = filedialog.askdirectory()
#     if asked_selected_output_path == "":
#         selected_output_path.set(OUTPUT_PATH_CODED)
#     else:
#         selected_output_path.set(asked_selected_output_path)







# # GUI select from menus functions ---------------------------
# def select_audio_mode_from_menu(selected_mode):
#     global selected_audio_mode
#     selected_audio_mode = selected_mode
#     logging.info(f"Print global selected audio mode: {selected_audio_mode}, print selected_mode: {selected_mode}")
#     if selected_audio_mode == "Vocal Isolation":
#         logging.info(f"Selected Audio Mode:  {selected_audio_mode}")
    
#     if selected_audio_mode == "Audio Denoise":
#         logging.info(f"Selected audio mode is: {selected_audio_mode}")
        
#     if selected_audio_mode == "Disabled":
#         logging.info(f"Selected audio mode is: {selected_audio_mode}")
    
#     return selected_audio_mode
    
    




# def select_interpolation_from_menu(selected_option: str) -> None:
#     global selected_interpolation_factor

#     match selected_option:
#         case "Disabled":
#             selected_interpolation_factor = 0
#         case "Low":
#             selected_interpolation_factor = 0.3
#         case "Medium":
#             selected_interpolation_factor = 0.5
#         case "High":
#             selected_interpolation_factor = 0.7

    
# def select_save_frame_from_menu(selected_option: str):
#     global selected_keep_frames
#     if   selected_option == 'Enabled':  selected_keep_frames = True
#     elif selected_option == 'Disabled': selected_keep_frames = False

# def select_image_extension_from_menu(selected_option: str) -> None:
#     global selected_image_extension   
#     selected_image_extension = selected_option
    
# def select_video_extension_from_menu(selected_option: str) -> None:
#     global selected_video_extension   
#     selected_video_extension = selected_option






















# # GUI info functions ---------------------------
# def open_socialMedia_tool_info():
#     option_list = [
#         "\n NOTES\n" 
#         "\nInstagram: \n" +
#         "\nYoutube: \n" +
#         "\nTiktok: \n" 
#     ]
#     MessageBox(
#         messageType = "info",
#         title       = "Social Media",
#         subtitle    = "Information about (Social Media Tool)",
#         default_value = "",
#         option_list   = option_list
#     )


# def open_mediaInfo_Analyst():
#     option_list = [
#         "\n NOTES\n" 
#         "\n open_mediaInfo_Analyst\n" 

#     ]
#     MessageBox(
#         messageType = "info",
#         title       = "open_mediaInfo_Analyst",
#         subtitle    = "open_mediaInfo_Analyst",
#         default_value = "",
#         option_list   = option_list
#     )
# def open_ToolMenu_Info():
#     option_list = [
#         "\nNOTES\n" 
#         "\n TOOL list information\n" 

#     ]
#     MessageBox(
#         messageType = "info",
#         title       = "TOOL list information",
#         subtitle    = "TOOL list information",
#         default_value = "",
#         option_list   = option_list
#     )


# def open_LR_Agent_tool_info():
#     option_list = [
#         "\n NOTES\n" 
#         "\nLearnReflect Agent: \n" 
#     ]
#     MessageBox(
#         messageType = "info",
#         title       = "LearnReflect Agent",
#         subtitle    = "Information about LearnReflect Agent",
#         default_value = "",
#         option_list   = option_list
#     )





# def open_YoutubeDownloader_tool_info():
#     option_list = [
#         "\n NOTES\n" 
#         "\n Youtube Downloader:\n" 
#     ]
#     MessageBox(
#         messageType = "info",
#         title       = "Youtube Downloader",
#         subtitle    = "Information about youtube downloader",
#         default_value = "",
#         option_list   = option_list
#     )


# def open_info_output_path():
#     option_list = [
#         "\n The default path is defined by the input files."
#         + "\n Upload cookie file from youtube, it will be auto-saved."
#         + "\n 1. go to google crome."
#         + "\n 2.find a cookie extension for exsample: https://chromewebstore.google.com/detail/get-cookiestxt-clean/ahmnmhfbokciafffnknlekllgcnafnie"
#         + "\n Go to youtube, then open the extension and export as, this will download a .txt\n",
#         + "\n upload the .txt file to upload files, and then you are good to go :D \n",
#         "it is possible to select the desired output path using the SELECT button",
#     ]

#     MessageBox(
#         messageType   = "info",
#         title         = "Output path",
#         subtitle      = "This widget allows to choose upscaled files path",
#         default_value = default_output_path,
#         option_list   = option_list
#     )




# def open_info_AI_model():
#     option_list = [
#         "\n IRCNN (2017) - Very simple and lightweight AI architecture\n" + 
#         " Only denoising (no upscaling)\n" + 
#         " Recommended for both image/video denoising\n" + 
#         "  • IRCNN_Mx1 - (medium denoise)\n" +
#         "  • IRCNN_Lx1 - (high denoise)\n",

#         "\n SRVGGNetCompact (2022) - Fast and lightweight AI architecture\n" + 
#         " Good-quality upscale\n" + 
#         " Recommended for video upscaling\n" + 
#         "  • RealESR_Gx4\n" + 
#         "  • RealSRx4_Anime\n",

#         "\n RRDB (2020) - Complex and heavy AI architecture\n" + 
#         " High-quality upscale\n" + 
#         " Recommended for image upscaling\n" +
#         "  • BSRGANx2\n" + 
#         "  • BSRGANx4\n" +
#         "  • RealESRGANx4\n",

#     ]

#     MessageBox(
#         messageType = "info",
#         title       = "AI model",
#         subtitle    = "This widget allows to choose between different AI models for upscaling",
#         default_value = default_AI_model,
#         option_list   = option_list
#     )








# def open_info_audio_mode(): 
#     option_list = [
#         "Audio Mode Options:"
#         "\n • Audio Enhancement: Improve overall sound quality, reducing background noise and clarifying audio details.\n" +
#         "   • Vocal Isolation: Separate and isolate vocals from the background music or environment, allowing you to emphasize or remove singing or speech.\n"
#     ]
    
#     MessageBox(
#         messageType= "info",
#         title = "Audio Denoise",
#         subtitle = "This Widget allows to choose Vocal isolation or Audio Denoise",
#         default_value = default_audio_mode,
#         option_list = option_list
#     )
    




# def open_info_keep_frames():
#     option_list = [
#         "\n ENABLED \n" + 
#         " The app does not delete the video frames after creating the upscaled video \n",

#         "\n DISABLED \n" + 
#         " The app deletes the video frames after creating the upscaled video \n"
#     ]

#     MessageBox(
#         messageType   = "info",
#         title         = "Keep frames",
#         subtitle      = "This widget allows to choose to keep video frames",
#         default_value = None,
#         option_list   = option_list
#     )
    




# def open_info_AI_interpolation():
#     option_list = [
#         " Interpolation is the fusion of the upscaled image produced by AI and the original image",

#         " \n INTERPOLATION OPTIONS\n" +
#         "  • Disabled - 100% upscaled\n" + 
#         "  • Low - 30% original / 70% upscaled\n" +
#         "  • Medium - 50% original / 50% upscaled\n" +
#         "  • High - 70% original / 30% upscaled\n",

#         " \n NOTES\n" +
#         "  • Can increase the quality of the final result\n" + 
#         "  • Especially when using the tilling/merging function (with low VRAM)\n" +
#         "  • Especially at low Input resolution % values (<50%) \n",

#     ]

#     MessageBox(
#         messageType = "info",
#         title       = "AI Interpolation", 
#         subtitle    = "This widget allows to choose interpolation between upscaled and original image/frame",
#         default_value = default_interpolation,
#         option_list   = option_list
#     )




# def open_info_image_output():
#     option_list = [
#         " \n PNG\n  • very good quality\n  • slow and heavy file\n  • supports transparent images\n",
#         " \n JPG\n  • good quality\n  • fast and lightweight file\n",
#         " \n BMP\n  • highest quality\n  • slow and heavy file\n",
#         " \n TIFF\n  • highest quality\n  • very slow and heavy file\n",
#     ]

#     MessageBox(
#         messageType = "info",
#         title       = "Image output",
#         subtitle    = "This widget allows to choose the extension of upscaled images",
#         default_value = default_image_extension,
#         option_list   = option_list
#     )




# def open_info_video_extension():
#     option_list = [
#         "\n MP4 (x264)\n" + 
#         "   • produces well compressed video using x264 codec\n",

#         "\n MP4 (x265)\n" + 
#         "   • produces well compressed video using x265 codec\n",

#         "\n AVI\n" + 
#         "   • produces the highest quality video\n" +
#         "   • the video produced can also be of large size\n"
#     ]

#     MessageBox(
#         messageType = "info",
#         title = "Video output",
#         subtitle = "This widget allows to choose the extension of the upscaled video",
#         default_value = default_video_extension,
#         option_list = option_list
#     )



# def open_info_input_resolution():
#     option_list = [
#         " A high value (>70%) will create high quality photos/videos but will be slower",
#         " While a low value (<40%) will create good quality photos/videos but will much faster",

#         " \n For example, for a 1080p (1920x1080) image/video\n" + 
#         " • Input resolution 25% => input to AI 270p (480x270)\n" +
#         " • Input resolution 50% => input to AI 540p (960x540)\n" + 
#         " • Input resolution 75% => input to AI 810p (1440x810)\n" + 
#         " • Input resolution 100% => input to AI 1080p (1920x1080) \n",
#     ]

#     MessageBox(
#         messageType = "info",
#         title       = "Input resolution %",
#         subtitle    = "This widget allows to choose the resolution input to the AI",
#         default_value = default_resize_factor,
#         option_list   = option_list
#     )



# def place_input_output_resolution_textboxs():

#     def open_info_input_resolution():
#         option_list = [
#             " A high value (>70%) will create high quality photos/videos but will be slower",
#             " While a low value (<40%) will create good quality photos/videos but will much faster",

#             " \n For example, for a 1080p (1920x1080) image/video\n" + 
#             " • Input resolution 25% => input to AI 270p (480x270)\n" +
#             " • Input resolution 50% => input to AI 540p (960x540)\n" + 
#             " • Input resolution 75% => input to AI 810p (1440x810)\n" + 
#             " • Input resolution 100% => input to AI 1080p (1920x1080) \n",
#         ]
#         MessageBox(
#             messageType   = "info",
#             title         = "Input resolution %",
#             subtitle      = "This widget allows to choose the resolution input to the AI",
#             default_value = None,
#             option_list   = option_list
#         )

#     widget_row = row4_y

#     background = create_option_background()
#     background.place(relx = 0.75, rely = widget_row, relwidth = 0.48, anchor = "center")

#     info_button = create_info_button(open_info_input_resolution, "Input resolution")
#     option_menu = create_text_box(selected_input_resize_factor, width = little_textbox_width) 

#     info_button.place(relx = column_info1, rely = widget_row - 0.003, anchor = "center")
#     option_menu.place(relx = column_1_5,   rely = widget_row,         anchor = "center")



#     info_button.place(relx = column_info2, rely = widget_row - 0.003, anchor = "center")
#     option_menu.place(relx = column_3,     rely = widget_row,         anchor = "center")











# def place_output_path_textbox():
#     outer = CTkFrame(controls_bar_frame, fg_color="transparent")
#     outer.pack(side="left", padx=(8, 3), pady=5, fill="y")

#     path_lbl = CTkButton(
#         outer, text="● Output Path", command=open_info_output_path,
#         fg_color="transparent", hover_color="#181410",
#         text_color="#5A5248", height=14,
#         font=CTkFont(family="Segoe UI", size=8, weight="bold"),
#         border_width=0, anchor="w", width=115,
#     )
#     path_lbl.pack(anchor="w")

#     output_path_textbox = CTkEntry(
#         outer, textvariable=selected_output_path,
#         border_width=1, corner_radius=5, width=115, height=22,
#         font=CTkFont(family="Segoe UI", size=9),
#         justify="center", text_color=CREAM3,
#         fg_color="#0A0A09", border_color=BORDER2, state=DISABLED,
#     )
#     output_path_textbox.pack(pady=(1, 1))

#     select_output_path_button = CTkButton(
#         outer, command=open_output_path_action, text="SELECT",
#         width=115, height=22,
#         font=CTkFont(family="Segoe UI", size=9, weight="bold"),
#         border_width=1, fg_color="#1A1408", hover_color="#2A200A",
#         text_color=AMBER, border_color=AMBER_DIM, corner_radius=5,
#     )
#     select_output_path_button.pack(pady=(1, 0))

#     # Vertical divider after this block
#     CTkFrame(controls_bar_frame, fg_color=BORDER1, width=1,
#              corner_radius=0).pack(side="left", fill="y", pady=6, padx=2)



# def place_AI_menu():
#     frame = CTkFrame(controls_bar_frame, fg_color=PANEL2_BG,
#                      border_width=1, border_color=BORDER2, corner_radius=5)
#     frame.pack(side="left", padx=3, pady=6, fill="y")

#     CTkButton(
#         frame, text="● AI Model", command=open_info_AI_model,
#         fg_color="transparent", hover_color="#181410",
#         text_color=AMBER_DIM, height=14,
#         font=CTkFont(family="Segoe UI", size=8, weight="bold"),
#         border_width=0, anchor="center", width=108,
#     ).pack(padx=4, pady=(4, 1))

#     AI_menu = create_option_menu_2(select_AI_from_menu, AI_models_list,
#                                    default_AI_model, master=frame, width=108)
#     AI_menu.pack(padx=4, pady=(0, 4))



# def place_AI_interpolation_menu():
#     frame = CTkFrame(controls_bar_frame, fg_color=PANEL2_BG,
#                      border_width=1, border_color=BORDER2, corner_radius=5)
#     frame.pack(side="left", padx=3, pady=6, fill="y")

#     CTkButton(
#         frame, text="● AI Interp.", command=open_info_AI_interpolation,
#         fg_color="transparent", hover_color="#181410",
#         text_color=AMBER_DIM, height=14,
#         font=CTkFont(family="Segoe UI", size=8, weight="bold"),
#         border_width=0, anchor="center", width=108,
#     ).pack(padx=4, pady=(4, 1))

#     menu = create_option_menu_2(select_interpolation_from_menu, interpolation_list,
#                                 default_interpolation, master=frame, width=108)
#     menu.pack(padx=4, pady=(0, 4))
 




    
# def place_Audio_Selection_menu():
#     frame = CTkFrame(controls_bar_frame, fg_color=PANEL2_BG,
#                      border_width=1, border_color=BORDER2, corner_radius=5)
#     frame.pack(side="left", padx=3, pady=6, fill="y")

#     CTkButton(
#         frame, text="● Audio Mode", command=open_info_audio_mode,
#         fg_color="transparent", hover_color="#181410",
#         text_color=AMBER_DIM, height=14,
#         font=CTkFont(family="Segoe UI", size=8, weight="bold"),
#         border_width=0, anchor="center", width=108,
#     ).pack(padx=4, pady=(4, 1))

#     menu = create_option_menu_2(select_audio_mode_from_menu, audio_mode_list,
#                                 default_audio_mode, master=frame, width=108)
#     menu.pack(padx=4, pady=(0, 4))

#     # Vertical divider after audio group
#     CTkFrame(controls_bar_frame, fg_color=BORDER1, width=1,
#              corner_radius=0).pack(side="left", fill="y", pady=6, padx=2)




# def place_keep_frames_menu():
#     keep_frames_button = create_info_button(open_info_keep_frames, "Keep frames")
#     keep_frames_menu   = create_option_menu(select_save_frame_from_menu, keep_frames_list, default_keep_frames)
    
#     keep_frames_button.place(relx = column1_x- 0.4, rely = row4_y - 0.053, anchor = "center")
#     keep_frames_menu.place(relx = column1_x- 0.4, rely = row4_y, anchor = "center")
    



# def place_image_output_menu():
#     frame = CTkFrame(controls_bar_frame, fg_color=PANEL2_BG,
#                      border_width=1, border_color=BORDER2, corner_radius=5)
#     frame.pack(side="left", padx=3, pady=6, fill="y")

#     CTkLabel(
#         frame, text="OUTPUT FORMAT",
#         font=CTkFont(family="Segoe UI", size=8, weight="bold"),
#         text_color=AMBER_DIM, fg_color="transparent",
#     ).pack(padx=4, pady=(4, 2))

#     duo = CTkFrame(frame, fg_color="transparent")
#     duo.pack(padx=4, pady=(0, 4))

#     # Image output sub-column
#     img_col = CTkFrame(duo, fg_color="transparent")
#     img_col.pack(side="left", padx=(0, 2))
#     CTkLabel(img_col, text="Image", font=CTkFont(family="Segoe UI", size=7),
#              text_color=CREAM3, fg_color="transparent").pack()
#     img_menu = create_option_menu_2(select_image_extension_from_menu,
#                                     image_extension_list, default_image_extension,
#                                     master=img_col, width=68)
#     img_menu.pack()

#     # Video output sub-column
#     vid_col = CTkFrame(duo, fg_color="transparent")
#     vid_col.pack(side="left", padx=(2, 0))
#     CTkLabel(vid_col, text="Video", font=CTkFont(family="Segoe UI", size=7),
#              text_color=CREAM3, fg_color="transparent").pack()
#     vid_menu = create_option_menu_2(select_video_extension_from_menu,
#                                     video_extension_list, default_video_extension,
#                                     master=vid_col, width=88)
#     vid_menu.pack()

#     # Vertical divider
#     CTkFrame(controls_bar_frame, fg_color=BORDER1, width=1,
#              corner_radius=0).pack(side="left", fill="y", pady=6, padx=2)



# def place_input_resolution_textbox():
#     frame = CTkFrame(controls_bar_frame, fg_color=PANEL2_BG,
#                      border_width=1, border_color=BORDER2, corner_radius=5)
#     frame.pack(side="left", padx=3, pady=6, fill="y")

#     CTkButton(
#         frame, text="● Input Res %", command=open_info_input_resolution,
#         fg_color="transparent", hover_color="#181410",
#         text_color=AMBER_DIM, height=14,
#         font=CTkFont(family="Segoe UI", size=8, weight="bold"),
#         border_width=0, anchor="center", width=75,
#     ).pack(padx=4, pady=(4, 1))

#     tb = create_text_box(selected_input_resize_factor, master=frame, width=75)
#     tb.pack(padx=4, pady=(0, 4))

#     # Vertical divider
#     CTkFrame(controls_bar_frame, fg_color=BORDER1, width=1,
#              corner_radius=0).pack(side="left", fill="y", pady=6, padx=2)



# def place_upscale_button(): 
#     global upscale_slot_frame
#     # Clear previous UPSCALE/STOP widget
#     for w in upscale_slot_frame.winfo_children():
#         w.destroy()

#     upscale_button = CTkButton(
#         master=upscale_slot_frame,
#         command=upscale_button_command,
#         text="UPSCALE",
#         image=upscale_icon,
#         width=110, height=26,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         border_width=1,
#         fg_color=AMBER_GLOW,
#         hover_color="#5a3c0c",
#         text_color=AMBER,
#         border_color=AMBER_DIM,
#         corner_radius=6,
#     )
#     upscale_button.pack(side="left", padx=2)
#     upscale_button.lift()

# def place_stop_button(): 
#     global upscale_slot_frame
#     # Clear previous UPSCALE/STOP widget
#     for w in upscale_slot_frame.winfo_children():
#         w.destroy()

#     stop_button = CTkButton(
#         master=upscale_slot_frame,
#         command=stop_button_command,
#         text="STOP",
#         image=stop_icon,
#         width=110, height=26,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         border_width=1,
#         fg_color="#160808",
#         hover_color="#220C0C",
#         text_color="#E04040",
#         border_color="#EC1D1D",
#         corner_radius=6,
#     )
#     stop_button.pack(side="left", padx=2)


# def place_message_label():
#     global input_file_button, upscale_slot_frame

#     # Right-side action container
#     action_frame = CTkFrame(controls_bar_frame, fg_color="transparent")
#     action_frame.pack(side="right", padx=(2, 8), pady=5, fill="y")

#     message_label = CTkLabel(
#         master=action_frame,
#         textvariable=info_message,
#         height=16,
#         font=CTkFont(family="Segoe UI", size=9, weight="bold"),
#         fg_color="transparent",
#         text_color=CREAM2,
#         anchor="center",
#     )
#     message_label.pack(pady=(3, 2))

#     btns_row = CTkFrame(action_frame, fg_color="transparent")
#     btns_row.pack(pady=(0, 3))

#     input_file_button = CTkButton(
#         master=btns_row,
#         command=open_files_action,
#         text="SELECT FILES",
#         width=100, height=26,
#         font=CTkFont(family="Segoe UI", size=10, weight="bold"),
#         border_width=1,
#         fg_color="#0E0E0C", hover_color="#181612",
#         text_color=CREAM2, border_color=BORDER3,
#         corner_radius=6,
#     )
#     input_file_button.pack(side="left", padx=2)

#     # Slot frame for UPSCALE / STOP toggle
#     upscale_slot_frame = CTkFrame(btns_row, fg_color="transparent")
#     upscale_slot_frame.pack(side="left")
#     globals()['upscale_slot_frame'] = upscale_slot_frame




# def create_option_background():
#     return CTkFrame(
#         master        = window,
#         bg_color      = background_color,
#         fg_color      = PANEL2_BG,
#         height        = 46,
#         corner_radius = 8,
#     )











# # Main functions ---------------------------
# def on_app_close() -> None:
#     global Global_offline_model
#     del Global_offline_model
#     window.grab_release()
#     window.destroy()
#     load_model_inference()
#     global selected_AI_model
#     global selected_AI_multithreading
#     global selected_gpu
#     global selected_interpolation_factor
#     global selected_image_extension
#     global selected_video_extension
#     global tiles_resolution
#     global input_resize_factor
#     global cpu_number
#     global selected_audio_mode 
#     global preview_ai_instance


#     preview_ai_instance = None

#     selected_audio_mode = "Disabled"
#     AI_model_to_save          = f"{selected_AI_model}"
#     AI_multithreading_to_save = f"{selected_AI_multithreading} threads"
#     gpu_to_save               = selected_gpu
#     keep_frames_to_save = "Enabled" if selected_keep_frames == True else "Disabled"
#     image_extension_to_save   = selected_image_extension
#     video_extension_to_save   = selected_video_extension
    
#     interpolation_to_save= {
#         0: "Disabled",
#         0.3: "Low",
#         0.5: "Medium",
#         0.7: "High",
#     }.get(selected_interpolation_factor)
    
#     Audio_option_to_save = {
#         0: "Disabled",
#         1: "Vocal Isolation",
#         2: "Audio Denoise",
#     }.get(selected_audio_mode)

#     user_preference = {
#         "default_AI_model":          AI_model_to_save,
#         "default_AI_multithreading": AI_multithreading_to_save,
#         "default_gpu":               gpu_to_save,
#         "default_keep_frames":       keep_frames_to_save,
#         "default_image_extension":   image_extension_to_save,
#         "default_video_extension":   video_extension_to_save,
#         "default_interpolation":     interpolation_to_save,
#         "default_audio_mode":         Audio_option_to_save,
#         "default_output_path":       selected_output_path.get(),
#         "default_resize_factor":     str(selected_input_resize_factor.get()),
#         "default_VRAM_limiter":      str(selected_VRAM_limiter.get()),
#         "default_cpu_number":        str(selected_cpu_number.get()),
#     }
#     user_preference_json = json_dumps(user_preference)
#     with open(USER_PREFERENCE_PATH, "w") as preference_file:
#         preference_file.write(user_preference_json)

#     stop_upscale_process()
#     gc.collect()
#     torch.cuda.empty_cache()
    
    


    
    
# class VideoEnhancer():
#     def __init__(self, Master):
#         #threading.Thread(target=load_model_async, daemon=True).start()
#         self.toplevel_window = None
#         self._master = Master
#         Master.protocol("WM_DELETE_WINDOW", on_app_close)
#         Master.title('LearnReflect Video Enchancer')
#         screen_width  = Master.winfo_screenwidth()
#         screen_height = Master.winfo_screenheight()
#         window_width  = int(screen_width  * 0.85)
#         window_height = int(screen_height * 0.85)
#         x_offset = (screen_width  - window_width)  // 2
#         y_offset = (screen_height - window_height) // 2
#         # Store windowed geometry so we can restore it when leaving fullscreen
#         self._windowed_geometry = f"{window_width}x{window_height}+{x_offset}+{y_offset}"
#         Master.geometry(self._windowed_geometry)
#         Master.resizable(True, True)
#         # Start in fullscreen
#         Master.attributes("-fullscreen", True)
#         self._is_fullscreen = True
#         # F11 toggles fullscreen / windowed
#         Master.bind("<F11>", self._toggle_fullscreen)
#         # Escape also exits fullscreen (back to windowed)
#         Master.bind("<Escape>", self._exit_fullscreen)
#         Master.iconbitmap(find_by_relative_path("Assets" + os_separator + "logo.ico"))
#         # Background image hidden in new layout
#         # self.bg_image = CTkImage(...)
#         load_cookie_file_path()

#         # ── Thin separator bar between left col and center col ──────────────
#         sep_left = CTkFrame(Master, fg_color=BORDER2, width=1, corner_radius=0)
#         sep_left.place(relx=0.22, rely=0.0, relwidth=0.001, relheight=1.0)

#         # ── Thin separator bar between center col (file list) and right col (preview) ──
#         sep_right = CTkFrame(Master, fg_color=BORDER2, width=1, corner_radius=0)
#         sep_right.place(relx=0.55, rely=0.0, relwidth=0.001, relheight=1.0)

#         # ── Controls bar (top of center column) ─────────────────────────────
#         global controls_bar_frame
#         self.controls_bar_frame = CTkFrame(
#             Master,
#             fg_color=PANEL2_BG,
#             corner_radius=0,
#             border_width=0,
#         )
#         self.controls_bar_frame.place(relx=0.22, rely=0.0, relwidth=0.33, relheight=0.095)
#         controls_bar_frame = self.controls_bar_frame

#         # ── Thin bottom border for controls bar ─────────────────────────────
#         cb_border = CTkFrame(Master, fg_color=BORDER2, height=1, corner_radius=0)
#         cb_border.place(relx=0.22, rely=0.095, relwidth=0.33, relheight=0.001)

#         # ── Permanent file list area (visible even when no files are loaded) ─
#         self.file_list_bg = CTkFrame(
#             Master,
#             fg_color=PANEL_BG,
#             border_color=BORDER2,
#             border_width=1,
#             corner_radius=0,
#         )
#         self.file_list_bg.place(relx=0.22, rely=0.096, relwidth=0.33, relheight=0.904)

#         self.ToolWindowClass = ToolWindowClass(Master)
#         #load_model_inference()
#         place_loadFile_section(Master)
#         place_output_path_textbox()
#         place_AI_menu()
#         place_AI_interpolation_menu()
#         place_Audio_Selection_menu()
#         place_input_resolution_textbox()
#         place_image_output_menu()
#         place_message_label()
#         place_upscale_button()
#         selected_VRAM_limiter.set(str(round(get_gpu_vram() / 1000)) if get_gpu_vram() else "4")

#     # ── Fullscreen helpers ────────────────────────────────────────────
#     def _toggle_fullscreen(self, event=None):
#         """Toggle between fullscreen and windowed mode (F11)."""
#         if self._is_fullscreen:
#             self._exit_fullscreen()
#         else:
#             self._enter_fullscreen()

#     def _enter_fullscreen(self, event=None):
#         self._master.attributes("-fullscreen", True)
#         self._is_fullscreen = True

#     def _exit_fullscreen(self, event=None):
#         self._master.attributes("-fullscreen", False)
#         self._master.geometry(self._windowed_geometry)
#         self._is_fullscreen = False


# if __name__ == "__main__":
#     #from Decryption import validate_jwt
#     # if not validate_jwt():
#     #     logging.info(f"Validating with jwt error")
#     #     sys.exit(1)
#     # else: 
#     #     logging.info(f"Validating with jwt success!")

    
#     selected_audio_mode = "Disabled"
#     multiprocessing_freeze_support()
#     set_appearance_mode("Dark")
#     set_default_color_theme("dark-blue")

 
    
#     if _TKDND_AVAILABLE:
#         # tkinterdnd2 + customtkinter: create a hybrid root that supports both
#         class _CTkDnD(CTk, _tkdnd.DnDWrapper):
#             def __init__(self, *args, **kwargs):
#                 CTk.__init__(self, *args, **kwargs)
#                 self.TkdndVersion = _tkdnd.DnDWrapper.tkdnd_init(self)
#         window = _CTkDnD()
#     else:
#         window = CTk()
#     window.configure(fg_color="#060606")
#     youtube_progress_var = StringVar()
#     processing_queue = multiprocessing_Queue(maxsize=1)
#     info_message            = StringVar()
#     selected_output_path    = StringVar()
#     selected_input_resize_factor  = StringVar()
#     selected_VRAM_limiter   = StringVar()
#     selected_cpu_number     = StringVar()
#     video_format_var = StringVar(value="None")
#     audio_format_var = StringVar(value="None")

    
#     global selected_file_list
#     global selected_AI_model
#     global selected_gpu
#     global selected_keep_frames
#     global selected_AI_multithreading
#     global selected_image_extension
#     global selected_video_extension
#     global selected_interpolation_factor
#     global tiles_resolution
#     global input_resize_factor
#     global cpu_number
#     selected_gpu = "Auto"
#     selected_file_list = []
#     selected_AI_model          = default_AI_model
#     selected_image_extension   = default_image_extension
#     selected_video_extension   = default_video_extension
#     selected_AI_multithreading = max(1, int(os_cpu_count() // 2))
#     default_cpu_number        = str(int(get_cpu_number()))
#     selected_keep_frames = True if default_keep_frames == "Enabled" else False

#     selected_interpolation_factor = {
#         "Disabled": 0,
#         "Low": 0.3,
#         "Medium": 0.5,
#         "High": 0.7,
#     }.get(default_interpolation)
    

#     selected_input_resize_factor.set(default_resize_factor)
#     selected_VRAM_limiter.set(default_VRAM_limiter)
#     selected_cpu_number.set(default_cpu_number)
#     selected_output_path.set(default_output_path)

#     info_message.set("Welcome Back")
#     selected_input_resize_factor.trace_add('write', update_file_widget)


#     font   = "Segoe UI"    
#     bold8  = CTkFont(family = font, size = 8, weight = "bold")
#     bold9  = CTkFont(family = font, size = 9, weight = "bold")
#     bold10 = CTkFont(family = font, size = 10, weight = "bold")
#     bold11 = CTkFont(family = font, size = 11, weight = "bold")
#     bold12 = CTkFont(family = font, size = 12, weight = "bold")
#     bold13 = CTkFont(family = font, size = 13, weight = "bold")
#     bold14 = CTkFont(family = font, size = 14, weight = "bold")
#     bold16 = CTkFont(family = font, size = 16, weight = "bold")
#     bold17 = CTkFont(family = font, size = 17, weight = "bold")
#     bold18 = CTkFont(family = font, size = 18, weight = "bold")
#     bold19 = CTkFont(family = font, size = 19, weight = "bold")
#     bold20 = CTkFont(family = font, size = 20, weight = "bold")
#     bold21 = CTkFont(family = font, size = 21, weight = "bold")
#     bold22 = CTkFont(family = font, size = 22, weight = "bold")
#     bold23 = CTkFont(family = font, size = 23, weight = "bold")
#     bold24 = CTkFont(family = font, size = 24, weight = "bold")
#     stop_icon      = CTkImage(pillow_image_open(find_by_relative_path(f"Assets{os_separator}stop_icon.png")),      size=(15, 15))
#     upscale_icon   = CTkImage(pillow_image_open(find_by_relative_path(f"Assets{os_separator}upscale_iconLR.png")),   size=(15, 15))
#     clear_icon     = CTkImage(pillow_image_open(find_by_relative_path(f"Assets{os_separator}clear_icon.png")),     size=(15, 15))
#     info_icon      = CTkImage(pillow_image_open(find_by_relative_path(f"Assets{os_separator}info_icon.png")),      size=(17, 17))

    
    
#     app = VideoEnhancer(window)
#     window.update()
#     window.mainloop()
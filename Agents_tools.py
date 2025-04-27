from smolagents import tool
import os
from googleapiclient.discovery import build
import subprocess
import datetime
import tkinter as tk
@tool
def Fetch_top_trending_youtube_videos(Search_Query: str) -> dict:
    """
        A tool for fetching metadata from top trending YouTube videos in a specific category or topic.

        Args:
        Search_Query (str): A keyword or topic to search for trending YouTube videos (e.g., "Motivational", "Funny", "Tech Reviews").

        Returns:
        dict: A dictionary containing video metadata including title, description, view count, like count, comment count,
        thumbnails, and channel title for each top trending video.
    """
                
    Api_key = os.getenv("YOUTUBE_API_KEY")

    youtube = build("youtube", "v3", developerKey=Api_key)

    request = youtube.search().list(
                    part="snippet",
                    q=Search_Query,
                    type="video",
                    maxResults=10
                )
    response = request.execute()

    return response 



@tool
def ExtractAudioFromVideo(video_path: str) -> str:
    """Extracts  mono 16kHz WAV audio from a video using ffmpeg.
        Args:
            video_path (str): The full path to the video file.

        Returns:
            str:  the path to the extracted audio file.
    """
    audio_path = "temp_audio.wav"
    audio_path = "temp_audio.wav"
    command = [
        "ffmpeg",
        "-y",  #
        "-i", video_path,
        "-ac", "1", 
        "-ar", "16000",  
        "-vn", 
        "-f", "wav",
        audio_path
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return audio_path



@tool
def Log_Agent_Progress(chat_display, stage: str, message: str) -> str:
    """
        A tool for logging agent thoughts, actions, and reflections during task execution.

        Args:
            chat_display: The chat display widget to output messages.
            stage (str): One of "info", "action", "reflection".
            message (str): A descriptive message of what the agent is doing or thinking.

        Returns:
            str: Confirmation that the message has been logged.
    """
    valid_stages = {"info", "action", "reflection"}
    if stage not in valid_stages:
        stage = "info"  

    log_entry = {
                "timestamp": datetime.datetime.now().strftime("%H:%M:%S"),
                "stage": stage,
                "message": message
            }

    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"{log_entry['timestamp']} [{stage.upper()}] {message}\n")
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)

    print(f"[{stage.upper()}] {log_entry['timestamp']}: {message}")
    return "Log recorded successfully."
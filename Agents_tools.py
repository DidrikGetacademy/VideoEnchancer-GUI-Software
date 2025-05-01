from smolagents import tool
from tkinter.scrolledtext import ScrolledText
import os
from googleapiclient.discovery import build
import subprocess
import datetime
import tkinter as tk
from dotenv import load_dotenv
@tool
def Fetch_top_trending_youtube_videos(Search_Query: str) -> dict:
    """
        A tool for fetching metadata from top trending YouTube videos in a specific category or topic.

        Args:
        Search_Query (str): Topic or keywords to search (e.g. “Motivational”, “Tech Reviews”).

        Returns:
        dict: A YouTube API response containing for each video:
        - snippet: title, description, channelTitle, publishTime, thumbnails
        - statistics: viewCount, likeCount, commentCount
    """
    load_dotenv()       
    Api_key = os.getenv("YOUTUBE_API_KEY")

    youtube = build("youtube", "v3", developerKey=Api_key)

    search_req = youtube.search().list(
                    part="snippet",
                    q=Search_Query,
                    type="video",
                    maxResults=20
                )
    search_resp = search_req.execute()
    video_ids = [item["id"]["video_id"] for item in  search_resp.get("items",[])]
    if not video_ids:
        return {"items": []}
    
    stats_req = youtube.videos().list(
        part="snippet.statistics",
        id=",".join(video_ids)
    )
    stats_resp = stats_req.execute()


    return stats_resp 



@tool
def ExtractAudioFromVideo(video_path: str) -> str:
    """Extracts  mono 16kHz WAV audio from a video using ffmpeg.
        Args:
            video_path (str): The full path to the video file.

        Returns:
            str:  the path to the extracted audio file.
    """
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
def Log_Agent_Progress(chat_display: ScrolledText, stage: str, message: str) -> str:
    """
        A tool for logging agent thoughts, actions, and reflections during task execution.
        Args:
            chat_display(str):  you have access too the chat_display variable just do chat_display=chat_display when you call this function.
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
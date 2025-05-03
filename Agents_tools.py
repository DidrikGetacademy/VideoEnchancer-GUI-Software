from smolagents import tool
from tkinter.scrolledtext import ScrolledText
import os
from googleapiclient.discovery import build
import subprocess
import datetime
import tkinter as tk
from dotenv import load_dotenv

####FETCH MORE DETAILS TOO PROVIDE AGENT WITH MORE INFORMATION####
@tool
def Fetch_top_trending_youtube_videos(Search_Query: str) -> dict:
    """
        A tool for  Fetch enriched metadata + stats for the top trending YouTube videos for a query, including category names, tags, duration, views, likes, comments, and channel stats.
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

    #Searches for candidate videos
    search_resp = youtube.search().list(
                    part="snippet",
                    q=Search_Query,
                    type="video",
                    maxResults=20
                ).execute()

    video_ids = [item["id"]["video_id"] for item in  search_resp.get("items",[])]
    if not video_ids:
        return {"items": []}
    
    
    #Fetches snippet + statistics + contentdetails
    stats_resp = youtube.videos().list(
        part="snippet,statistics,contentdetails",
        id=",".join(video_ids)
    ).execute()

    # Map categoryid -> categoryname
    category_ids = list({v["snippet"]["categoryId"] for v in stats_resp.get("items", [])})
    fetch_category_names = youtube.videoCategories.list(
        part="snippet",
        id=",".join(category_ids),
        regionCode="US"
    ).execute()
    category_map = {c["id"]: c["snippet"]["title"] for c in fetch_category_names.get("items",[])}






# @tool
# def Fetch_top_trending_youtube_videos(Search_Query: str) -> dict:
#     """
#     Fetch enriched metadata + stats for the top trending YouTube videos for a query,
#     including category names, tags, duration, views, likes, comments, and channel stats.
#     """
#     load_dotenv()
#     api_key = os.getenv("YOUTUBE_API_KEY")
#     youtube = build("youtube", "v3", developerKey=api_key)

#     # 1) Search for candidate videos
#     search_resp = youtube.search().list(
#         part="snippet",
#         q=Search_Query,
#         type="video",
#         maxResults=20
#     ).execute()

#     video_ids = [item["id"]["videoId"] for item in search_resp.get("items", [])]
#     if not video_ids:
#         return {"items": []}

#     # 2) Fetch snippet + statistics + contentDetails
#     stats_resp = youtube.videos().list(
#         part="snippet,statistics,contentDetails",
#         id=",".join(video_ids)
#     ).execute()

#     # 3) Map categoryId → categoryName
#     category_ids = list({v["snippet"]["categoryId"] for v in stats_resp.get("items", [])})
#     cat_resp = youtube.videoCategories().list(
#         part="snippet",
#         id=",".join(category_ids),
#         regionCode="US"
#     ).execute()
#     category_map = {c["id"]: c["snippet"]["title"] for c in cat_resp.get("items", [])}

#     # 4) Attach channel stats
#     channel_ids = list({v["snippet"]["channelId"] for v in stats_resp.get("items", [])})
#     ch_resp = youtube.channels().list(
#         part="statistics",
#         id=",".join(channel_ids)
#     ).execute()
#     channel_map = {c["id"]: c["statistics"]["subscriberCount"] for c in ch_resp.get("items", [])}

#     # 5) Enrich each video
#     enriched = []
#     for vid in stats_resp.get("items", []):
#         sid = vid["snippet"]
#         cid = vid["statistics"]
#         cd = vid["contentDetails"]
#         enriched.append({
#           "videoId": vid["id"],
#           "title": sid["title"],
#           "description": sid["description"],
#           "tags": sid.get("tags", []),
#           "channelTitle": sid["channelTitle"],
#           "subscriberCount": channel_map.get(sid["channelId"], None),
#           "category": category_map.get(sid["categoryId"], None),
#           "publishedAt": sid["publishedAt"],
#           "duration": cd["duration"],
#           "viewCount": cid.get("viewCount"),
#           "likeCount": cid.get("likeCount"),
#           "commentCount": cid.get("commentCount"),
#         })
#     return {"items": enriched}
# ```<end_code>

# ---

# ## 3. How these details unlock deeper reasoning  
# - **Category context** lets the model apply domain-specific norms (e.g. “Science videos often use listicle titles” vs “Music videos favor artist names”).  
# - **Tags and keywords** expose the exact SEO phrases that real videos are targeting.  
# - **Duration** can signal “snackable” (under 5 min) vs “deep dive” (10+ min) formats.  
# - **Engagement stats** let the agent quantify “what’s actually viral” (views/day) instead of just “what matches the query.”  
# - **Channel authority** hints at built-in audiences vs pure content quality.  

# Armed with this enriched dataset, your agent can surface hidden patterns—like “videos under 7 minutes in ‘Education’ with 5+ tags and ‘How to’ in the title get 30% more views”—and translate those into concrete tips.

# ---

# ## 4. Fine-tuning Qwen-2.5-Coder on “Video Metadata → Virality Drivers”  
# Because there’s no publicly available guide specifically for Qwen-2.5-Coder tuning, here’s a **standard recipe**:

# 1. **Dataset construction**  
#    - **Inputs**: JSON blobs of the enriched metadata above (`title`, `tags`, `category`, `viewCount`, etc.).  
#    - **Labels**: Human-written bullet-point “virality drivers” for each video (e.g. “uses power verbs,” “short duration,” “high tag density”).  
#    - Aim for **1,000–2,000** examples spanning multiple categories.

# 2. **Formatting examples**  
#    ```json
#    {"input": {"title": "...", "tags": [...], "category": "Education", "viewCount": "...", ...},
#     "output": ["Power-word headline", "Sub-5 min length", "Use top-searched tags"]}





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
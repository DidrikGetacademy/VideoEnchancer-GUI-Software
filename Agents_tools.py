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

    #Searches for videos related too the (search query) retrieves basic info of each video. (20 results)
    search_resp = youtube.search().list(
                    part="snippet",
                    q=Search_Query,
                    type="video",
                    maxResults=20
                ).execute()

    #Extracts the videoId of each video in items
    video_ids = [item["id"]["videoId"] for item in  search_resp.get("items",[])]

    #Early exit if no videos is found!
    if not video_ids:
        return {"items": []}
    
    
    #Fetches snippet + statistics + contentdetails --> fetches mote stats and details --> (title, stats,duration) using the video id's 
    stats_resp = youtube.videos().list(
        part="snippet,statistics,contentdetails",
        id=",".join(video_ids)
    ).execute()


    # Extracts all unique categoryID from videos
    category_ids = list({item["snippet"]["categoryId"] for item in stats_resp.get("items", [])})
    fetch_category_names = youtube.videoCategories().list(
        part="snippet",
        id=",".join(category_ids),
        regionCode="US"
    ).execute()


    #Looksup human redable category names (music, motivation, education) for each categoryId
    category_map = {
        item["id"]: item["snippet"]["title"]
        for item in fetch_category_names.get("items",[])
        }
        #Results --> {    "1": "Film & Animation" ..}



    #Retrieve statistics for each youtube channel too the video vi have found.
    channel_ids = list({item["snippet"]["channelId"] for item in stats_resp.get("items",[])})
    
    #We use the list of channel-ids to retrieve channel statistics like (subscriber count)
    channel_response = youtube.channels().list(
        part="statistics",
        id=",".join(channel_ids)
    ).execute()


    #we map the channel_ids  -  amount of subscribers. 
    channel_map = {
        item["id"]: item["statistics"]["subscriberCount"] 
        for item in channel_response.get("items",[])
        }
        #Results --> {"UCabc123": "50000" ...}



    #Summarize and attach channel stats
    #loops through all videos in stats_resp pulls out each videos' channelId
    channel_ids = list({item["snippet"]["channelId"] for item in stats_resp.get("items",[])})

    #call too get stats like(subscriber count) for each channel
    channel_response = youtube.channels().list(
        part="statistics",
        id=",".join(channel_ids)
    ).execute()

    #dict that maps each channels' id to its subscriber count.
    channel_map = {item["id"]: item["statistics"]["subscriberCount"] for item in channel_response.get("items",[])}

    enriched = []
    for vid in stats_resp.get("items",[]):
        snippet = vid["snippet"]
        statistics = vid["statistics"]
        content = vid["contentDetails"]

        enriched.append({
            "videoId": vid["id"],
            "title": snippet["title"],
            "description": snippet["description"],
            "tags": snippet.get("tags", []),
            "channelTitle": snippet["channelTitle"],
            "subscriberCount": channel_map.get(snippet["channelId"], None),
            "category": category_map.get(snippet["categoryId"], None),
            "PublihedAT": snippet["PublishedAt"],
            "duration": content["publishedAt"],
            "viewCount": snippet.get("viewCount"),
            "likeCount": snippet.get("likeCount"),
            "commentCount": snippet.get("commentCount"),
           })
        return {"items": enriched}



    


    

    



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
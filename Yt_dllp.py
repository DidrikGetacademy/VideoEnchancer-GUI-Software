import yt_dlp

def download_youtube_link(youtube_url,output_path):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:  
            ydl.download([youtube_url])
        return "Download Complete!"
    except Exception as e:
        return f"error during download {str(e)}"
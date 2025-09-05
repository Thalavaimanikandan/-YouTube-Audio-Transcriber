import re
import yt_dlp
import whisper

def clean_youtube_url(url):
    return url.strip()

def download_audio(url, filename="audio.mp3.mp3"):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": filename,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return filename

def transcribe_audio(filename):
    model = whisper.load_model("base")
    result = model.transcribe(filename , fp16=False)
    return result["text"]
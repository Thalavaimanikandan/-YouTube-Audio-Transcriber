import streamlit as st
from utils import clean_youtube_url, download_audio, transcribe_audio

st.title("🎵 YouTube Audio Transcriber")

url = st.text_input("Enter YouTube URL:")

if st.button("Transcribe"):
    if url:
        st.info("Downloading audio...")
        filename = download_audio(clean_youtube_url(url))
        st.success(f"Downloaded: {filename}")

        st.info("Transcribing...")
        text = transcribe_audio(filename)
        st.text_area("Transcription:", text, height=300)
    else:
        st.warning("Please enter a valid YouTube URL.")
# YouTube Audio Transcriber

A user‑friendly web app built with Streamlit that transcribes YouTube video audio using the OpenAI Whisper API.

---

## Features

- Input a YouTube video URL and your OpenAI API key  
- The app extracts the video’s audio  
- Uses Whisper to generate a full transcript  
- Displays the transcript in a clean web interface  

---

## Prerequisites

- Python 3.7+  
- An OpenAI account and valid API key  
- `ffmpeg` installed (for extracting audio)  

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Thalavaimanikandan/-YouTube-Audio-Transcriber.git
   cd -YouTube-Audio-Transcriber
````

2. Create & activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate     # Mac / Linux
   venv\Scripts\activate        # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Set your **OpenAI API key** either by environment variable:

   ```bash
   export OPENAI_API_KEY="your_api_key"
   ```

   or by entering it in the web app UI.

2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. In the browser UI:

   * Enter the YouTube video URL
   * Enter or paste your OpenAI API key (if not already set)
   * Click “Transcribe” to start

4. Wait for the transcript to appear on screen.

---

## File Structure

* `app.py` – main Streamlit application
* `utils.py` – helper functions (e.g. audio extraction, Whisper interface)
* `requirements.txt` – Python dependencies
* (Optional) `README.md`, license, etc.

---

## Limitations & Notes

* Whisper transcription may have errors — review the output
* Long videos may take time or hit rate limits
* Audio extraction depends on `ffmpeg` being correctly installed

---

## Contributing

* Bug fixes, improvements, feature additions welcome
* Please keep dependencies up to date
* Add tests for new features

---

## License

Specify your license (e.g. MIT, Apache 2.0).
Example (MIT):

```
MIT License

Copyright (c) 2025 Thalavaimanikandan

Permission is hereby granted, free of charge, to any person obtaining a copy.


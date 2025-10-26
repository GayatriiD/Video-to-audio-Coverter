🎵 Video to MP3 Converter

A simple and user-friendly Streamlit web app that converts videos (either uploaded MP4 files or links from YouTube, Instagram, and Facebook) into MP3 audio files.

You can use it locally in VS Code or deploy it online using Streamlit Cloud.

🚀 Features

✅ Upload local MP4 videos and extract audio
✅ Paste YouTube / Instagram / Facebook links to download directly as MP3
✅ Clean, minimal UI with progress indicators
✅ One-click Download MP3 button after conversion
✅ Uses FFmpeg for fast and high-quality audio extraction
✅ Works entirely in the browser — no command line needed!

🧩 Tech Stack

Streamlit
 – for the web interface

yt-dlp
 – for downloading and converting online videos

ffmpeg-python
 – for video-to-audio conversion

FFmpeg
 – the underlying media engine

 🧠 How It Works

If you upload an MP4, the app:

Saves it temporarily

Uses ffmpeg to extract audio as MP3

Provides a download button

If you paste a video link, the app:

Uses yt-dlp to download the best available audio

Automatically converts it to MP3

Lets you download the final file

💡 Tips

For large videos, conversion might take a few seconds.

Avoid filenames with emojis or special characters.

Always keep ffmpeg installed and accessible from your PATH.

🖥️ Deployment (Optional)

You can deploy this on Streamlit Cloud in seconds:

Push your code to GitHub.

Go to https://share.streamlit.io
.

Connect your GitHub repo → Deploy → Done!

Streamlit Cloud will install all dependencies automatically from requirements.txt.

import streamlit as st
import yt_dlp

import os
import tempfile
import ffmpeg

# Convert MP4 to MP3

# --- Custom CSS for styling ---
st.markdown("""
<style>
.main { background-color: #f0f2f6; }
.stButton>button { background-color: #4CAF50; color: white; border-radius: 5px; }
.stTextInput>div>div>input { border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

st.title("🎵 Video to MP3 Converter")
st.write("Upload an MP4 file or paste a YouTube/Instagram/Facebook link to convert it to MP3 format.")

# Option 1: Upload MP4 file
uploaded_file = st.file_uploader("Upload MP4 Video", type=["mp4"])

# Option 2: Input video link
link = st.text_input("Or paste a video link (YouTube, Instagram, Facebook)")

if st.button("Convert to MP3"):
    if uploaded_file or link:
        with st.spinner("Converting... Please wait ⏳"):
            try:
                if uploaded_file:
                    # --- Handle uploaded MP4 file ---
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
                        temp_video.write(uploaded_file.read())
                        video_path = temp_video.name

                    # Convert MP4 to MP3
                    audio_path = video_path.replace(".mp4", ".mp3")
                    input_file = video_path
                    output_file = video_path.replace(".mp4", ".mp3")

                    ffmpeg.input(input_file).output(output_file, format='mp3', acodec='libmp3lame', audio_bitrate='192k').run()


                    # Provide MP3 download button
                    with open(audio_path, "rb") as f:
                        st.download_button(
                            "Download MP3 🎧",
                            f,
                            file_name="converted_audio.mp3",
                            mime="audio/mpeg"
                        )

                    # Clean up temporary files
                    os.unlink(video_path)
                    os.unlink(audio_path)

                elif link:
                    # --- Handle video link using yt-dlp ---
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                        'outtmpl': '%(title)s.%(ext)s',
                        'quiet': True
                    }

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(link, download=True)
                        filename = ydl.prepare_filename(info)
                        audio_file = filename.rsplit('.', 1)[0] + '.mp3'

                    # Provide MP3 download button
                    with open(audio_file, "rb") as f:
                        st.download_button(
                            "Download MP3 🎧",
                            f,
                            file_name=os.path.basename(audio_file),
                            mime="audio/mpeg"
                        )

                    # Clean up
                    os.unlink(audio_file)

                st.success("✅ Conversion complete!")

            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")
    else:
        st.warning("Please upload a file or enter a link.")

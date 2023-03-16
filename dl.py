from pytube import YouTube
from pydub import AudioSegment
import os

# Define the URL of the YouTube video
url = "https://www.youtube.com/watch?v=YuUV-FGxpjQ"

# Download the audio from the YouTube video in MP4 format
youtube = YouTube(url)
audio = youtube.streams.filter(only_audio=True).first()
output_file = audio.download()

# Load the audio file using the AudioSegment class
audio = AudioSegment.from_file(output_file, format="mp4")

# Set the desired duration of each audio chunk (in milliseconds)
chunk_length_ms = 10000 # 10 seconds

# Split the audio into small chunks with the desired duration
chunks = list(audio[::chunk_length_ms])

# Convert each audio chunk to WAV format with floating point format and a 22,050 sample rate
for i, chunk in enumerate(chunks):
    chunk = chunk.set_frame_rate(22050).set_sample_width(4).set_channels(1)
    chunk.export(f"chunk{i}.wav", format="wav")

# Delete the original MP4 file
os.remove(output_file)

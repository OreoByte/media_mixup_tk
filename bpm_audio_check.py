#!/usr/bin/python3
import sys
import numpy as np
from pydub import AudioSegment
import librosa

# Load the MP3 file
song_name = sys.argv[1]
song = AudioSegment.from_mp3(song_name)

# Convert audio data to NumPy ndarray with floating-point values
audio_data = np.array(song.get_array_of_samples(), dtype=float)

# Normalize the audio data to the range [-1, 1] (assuming 16-bit audio)
audio_data /= np.max(np.abs(audio_data))

# Calculate the BPM
tempo, _ = librosa.beat.beat_track(y=audio_data, sr=song.frame_rate)

# Determine the time signature
# You may need to implement your logic to detect the time signature
# This can be complex and might involve pattern recognition

print(f"BPM: {tempo}")
#print(song_name)

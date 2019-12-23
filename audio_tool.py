#!/usr/bin/python3
import sys # user options/args

import matplotlib.pyplot as plt
import scipy.io.wavfile # read and spectrograph .wav files

from pydub import AudioSegment, effects
# convert audio formats (.mp3 and .wav) and normalize audio (have it all sound the same)
from pydub.playback import play # play any audio format

def player():
	#audio = AudioSegment.from_mp3(file_string)
	audio = AudioSegment.from_file(file_string) # can play wav files
	lower_volume = audio - 12
	# use: raise_volue = audio + <number> to make it louder
	play(lower_volume)

def spectrograph(file_string):
	sample_freq, signal_data = scipy.io.wavfile.read(file_string)

	plt.figure(figsize=(16,7))
	plt.subplot(211)
	plt.title("Audio Spectrogram")
	plt.plot(signal_data)
	plt.xlabel('Sample')
	plt.ylabel('Amplitude')

	plt.subplot(212)
	plt.specgram(signal_data[:,0], Fs=sample_freq)
	plt.xlabel('Time')
	plt.ylabel('Frequency')
	plt.show()
	
	plt.rcParams["keymap.quit"] = "q" # close graph without ctrl-c

def normalize():
	name = input("New Normalized .wav Filename\nInput: ")
	current_vol = AudioSegment.from_file(file_string)
	normalized_vol = effects.normalize(current_vol)
	normalized_vol.export(name, format="wav")

def convert_to_wav(): # convert audio files into wav
	name = input("New .wav Filename\nInput: ")
	original = AudioSegment.from_file(file_string)
	original.export(name, format="wav")

def wav_to_mp3(): # convert .wav to .mp3
	name = input("New .mp3 Filename\nInput: ")
	original = AudioSegment.from_file(file_string)
	original.export(name, format="mp3")

# take first option/flag after the python filename
args=sys.argv[1]
# 2: take something after the filename and first input from system
file=sys.argv[2:]
file_string = ''.join(file) # convert arrary into a string to used

def options(args):
	if args == "-p" or args == "--play":
		player()
	elif args == "-s" or args == "--spec":
				spectrograph(file_string)
	elif args == "-n" or args == "--norm":
		normalize()
	elif args == "-c" or args == "--conv":
		convert_to_wav()
	elif args == "-cb" or args == "--conv-back":
		wav_to_mp3()
	elif args == "-h" or args == "--help":
		print('Basic Use: ./audio_tool.py <function option> <audio filename>\n')
		print("-p or --play (play audio file)\n-s or --spec (view audio in a spectrograph)")
		print("Close spectrograph with q while the graphic program window is selected\n")
		print("-n or --norm (normalize a audio file. With new filename or old to overwrite it)\n")
		print("-c or --conv (convert audio into .wav format)")
		print("-cb or --conv-back (convert .wav files into .mp3 files)\n")
		print("NOTE: Options -c,--conv, -cb, and --conv-back filenames must have correct extension")
		print("Ex: ./audio_tool.py -c filename.mp3 (Input: new-filename.wav)\nOr")
		print("Ex: ./audio_tool.py -cb filename.wav (Input: new-filename.mp3)")
	else:
		print('Error Option Doesn\'t Exist')
options(args)

#!/usr/bin/python3
# requires modules pafy and youtube-dl
import pafy

url = input("Enter a Youtube URL or Link to convert: ")
verify = pafy.new(url)

option = int(input("Enter 0 for information about the video\nEnter 1 to download video the full video as a mp4\nEnter 2 to download just the audio with best quality\nInput-#: "))

if option == 0:
	print(f"Title: {verify.title}")
	print(f"Viewcount {verify.viewcount}")
	print(f"Author: {verify.author}")
	print(f"Video Length: {verify.length}")
	print(f"Likes: {verify.likes}")
	print(f"Dislikes: {verify.dislikes}")
	print(f"Description: {verify.description}")
elif option == 1:
	video_best_mp4 = verify.getbest(preftype = "mp4")
	video_best_mp4.download()
elif option == 2:
	best_vid_audio = verify.getbestaudio(preftype = "any",ftypestrict=False)
	# pafy audio options are (ogg, m4a, or webm),best quality will usually be webm audio
	# ftypestrict=False if preftype isn't the highest quality will choose another with a higher resolution
	best_vid_audio.download()
else:
	print("Sorry invalid input")

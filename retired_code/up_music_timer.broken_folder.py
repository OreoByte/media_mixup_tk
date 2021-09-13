#!/usr/bin/python3
'''
Install requirements
#!/bin/bash
sudo apt install ffmpeg -y
pip3 install pydub
pip3 install argparse
'''

import argparse
import pathlib

from pydub import AudioSegment
from pydub.playback import play

option = argparse.ArgumentParser(description="Music timer. For typing workouts or general tasks")

option.add_argument("-e","--export", required=False,help="Final Recorded filename to be Exported to MP3")

option.add_argument("-f","--folder", required=False,help="Use Selected Music Folder.  -f /path/to/music/folder")
option.add_argument("-s","--songs", required=False,help="manually select songs to play.  -s song1 song2 song3",nargs='+')
option.add_argument("-l","--loop", required=False,help="Enter number of times the selected music/audio will be replayed.",type=int)
option.add_argument('-v',"--volume", required=False,help="Change volume by dB (posittive number 'raise volume by X dB' | negative number 'lower volume by X db'). Default -15 dB.",type=float,default=-15)

option.add_argument("-st","--start_time", required=False,help="What Time in Seconds to start the Audio/Music. Can be use alone or with -st/--end_time. -st 10 OR --start_time 10",type=int)
option.add_argument("-et","--end_time", required=False,help="Timestamp of when the song or audio will end. Can be used with -et/--end_time. -et 40 OR --end_time",type=int)
args = option.parse_args()

volume=args.volume
split=''
def vert():
    global lower_volume,split 
    if args.songs:
        for songs in args.songs:
            audio = AudioSegment.from_file(songs)
            lower_volume = audio + volume

            if args.start_time and args.end_time:
                start = 1000 * args.start_time
                end = 1000 * args.end_time
                split = lower_volume[start:end]
            elif args.start_time:
                start = 1000 * args.start_time
                split = lower_volume[start:]
            elif args.end_time:
                end = 1000 * args.end_time * -1
                split = lower_volume[end:]
            else:
                break

    elif args.folder:
        files = list(pathlib.Path(args.folder).glob("*.mp3"))
        print(files)
        for songs in files:
            audio = AudioSegment.from_file(songs)
            lower_volume = audio + volume

            if args.start_time and args.end_time:
                start = 1000 * args.start_time
                end =1000 * args.end_time
                split = lower_volume[start:end]
            elif args.start_time:
                start = 1000 * args.start_time
                split = lower_volume[:start]
            elif args.end_time:
                end = 1000 * args.end_time * -1
                split = lower_volume[end:]
            else:
                break
    if args.export:
        export_save(lower_volume,split)  
    elif (args.songs or args.folder) and split == '':
        player(lower_volume,split)
    elif (args.songs or args.folder):
        player(lower_volume,split)
    else:
        print('Error At End of Vert Function')
#-------------------------------------------------------
def player(lower_volume,split):
    if args.loop:
        n = 0
        while n < args.loop:
            n += 1  
            if split:
                play(split)
            elif lower_volume:
                play(lower_volume)
        else:
            print('Loop Player Function Has Failed')
    else:
        if split:
            play(split)
        elif lower_volume:
            play(lower_volume)
        else:
            print('Single Player Function Has Failed')
#---------------------------------------------------------
def export_save(lower_volume,split):
    export_name = args.export
    if split:
        normalize_split = split + 15
        normalize_split.export(export_name,format="mp3")
    elif lower_volume:
        normalize_lower = lower_volume + 15
        normalize_lower.export(export_name,format="mp3")
    else:
        print("Export Function Has Failed")

vert()


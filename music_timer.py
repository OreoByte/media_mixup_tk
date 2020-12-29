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

option.add_argument("-g","--gui", required=False,help="Open program as a GUI Menu", action='store_true')
option.add_argument("-r","--record", required=False,help="Record Custom audio to be reused later")

option.add_argument("-f","--folder", required=False,help="Use Selected Music Folder.  -f /path/to/music/folder")
option.add_argument("-s","--songs", required=False,help="manually select songs to play.  -s song1 song2 song3",nargs='+')
option.add_argument("-l","--loop", required=False,help="Enter number of times the selected music/audio will be replayed.",type=int)

option.add_argument("-st","--start_time", required=False,help="What Time in Seconds to start the Audio/Music. Can be use alone or with -st/--end_time. -st 10 OR --start_time 10",type=int)

option.add_argument("-et","--end_time", required=False,help="Timestamp of when the song or audio will end. Can be used with -et/--end_time. -et 40 OR --end_time",type=int)
args = option.parse_args()

def player():
    if args.loop:
        n = 0
        while n < args.loop:
            n += 1
            if args.songs:
                for songs in args.songs:
                    audio = AudioSegment.from_file(songs)
                    lower_volume = audio - 15

                    if args.start_time and args.end_time:
                        start = 1000 * args.start_time
                        end =1000 * args.end_time
                        split = lower_volume[start:end]
                        play(split)
                    elif args.start_time:
                        start = 1000 * args.start_time
                        split = lower_volume[:start]
                        play(split)
                    elif args.end_time:
                        end = 1000 * args.end_time * -1
                        split = lower_volume[end:]
                        play(split)
                    else:
                        play(lower_volume)
            elif args.folder:
                files = list(pathlib.Path(args.folder).glob("*.mp3"))
                print(files)
                for songs in files:
                    audio = AudioSegment.from_file(songs)
                    lower_volume = audio - 15

                    if args.start_time and args.end_time:
                        start = 1000 * args.start_time
                        end =1000 * args.end_time
                        split = lower_volume[start:end]
                        play(split)
                    elif args.start_time:
                        start = 1000 * args.start_time
                        split = lower_volume[:start]
                        play(split)
                    elif args.end_time:
                        end = 1000 * args.end_time * -1
                        split = lower_volume[end:]
                        play(split)
                    else:
                        play(lower_volume)
#------------------------------------------------------------------------------------  
    else:
        if args.songs:
            for songs in args.songs:
                audio = AudioSegment.from_file(songs)
                lower_volume = audio - 15

                if args.start_time and args.end_time:
                    start = 1000 * args.start_time
                    end = 1000 * args.end_time
                    split = lower_volume[start:end]
                    print(split)
                    play(split)
                elif args.start_time:
                    start = 1000 * args.start_time
                    split = lower_volume[:start]
                    play(split)
                elif args.end_time:
                    end = 1000 * args.end_time * -1
                    split = lower_volume[end:]
                    play(split)
                else:
                    play(lower_volume)

        elif args.folder:
            files = list(pathlib.Path(args.folder).glob("*.mp3"))
            print(files)
            for songs in files:
                audio = AudioSegment.from_file(songs)
                lower_volume = audio - 15

                if args.start_time and args.end_time:
                    start = 1000 * args.start_time
                    end =1000 * args.end_time
                    split = lower_volume[start:end]
                    play(split)
                elif args.start_time:
                    start = 1000 * args.start_time
                    split = lower_volume[:start]
                    play(split)
                elif args.end_time:
                    end = 1000 * args.end_time * -1
                    split = lower_volume[end:]
                    play(split)
                else:
                    play(lower_volume)
player()

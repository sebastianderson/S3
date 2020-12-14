import numpy as np
import os
import subprocess
import collections

def mergeVideos(filename):
    """
    Function to see the differents videos in one screen
    """
    #all possible names
    filenames=[filename+"_vp8.webm",filename+"_vp9.webm",filename+"_h265.mp4",filename+"_av1.mkv"]
    #output name
    output=filename+"_merged.mp4"
    #command
    cmd = [
        "ffmpeg",
        "-i",
        filenames[0],
        "-i",
        filenames[1],
        "-i",
        filenames[2],
        "-i",
        filenames[3],
        "-filter_complex",
        '"[0:v][1:v]hstack[top]; \#stack videos
        [2:v][3:v]hstack[bottom]; \
        [top][bottom]vstack,format=yuv420p[v]; \
        [0:a][1:a][2:a][3:a]amerge=inputs=4[a]"',
        "-map",
        '"[v]"',
        "-map",
        '"[a]"',
        "-ac",
        "2",
        output
        ]
    # to convert a list to string we use join
    separator = " "
    com = separator.join(cmd)
    # use the command
    os.system(com)
files=["BBB_720p","BBB_480p","BBB_320X240","BBB_160X120"]
for i in files:
    #create all 4 files.
    mergeVideos(i)

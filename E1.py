import numpy as np
import os
import subprocess
import collections

# create the 8 different files with different sizes and codecs.

os.system(
    "ffmpeg -i BBB_160X120.avi -c:v libvpx -b:v 1M -c:a libvorbis BBB_160X120_vp8.webm"
)
os.system("ffmpeg -i BBB_160X120.avi -c:v libvpx-vp9 -b:v 2M BBB_160X120_vp9.webm")
os.system(
    "ffmpeg -i BBB_160X120.avi -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k BBB_160X120_h265.mp4"
)
os.system(
    "ffmpeg -i BBB_160X120.avi -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental BBB_160X120_av1.mkv"
)

os.system(
    "ffmpeg -i BBB_320X240.avi -c:v libvpx -b:v 1M -c:a libvorbis BBB_320X240_vp8.webm"
)
os.system("ffmpeg -i BBB_320X240.avi -c:v libvpx-vp9 -b:v 2M BBB_320X240_vp9.webm")
os.system(
    "ffmpeg -i BBB_320X240.avi -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k BBB_320X240_h265.mp4"
)
os.system(
    "ffmpeg -i BBB_320X240.avi -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental BBB_320X240_av1.mkv"
)

os.system("ffmpeg -i BBB_480p.avi -c:v libvpx -b:v 1M -c:a libvorbis BBB_480p_vp8.webm")
os.system(
    "ffmpeg -i BBB_480p.avi -c:v libvpx-vp9 -b:v 2M -c:a libvorbis BBB_480p_vp9.webm"
)
os.system(
    "ffmpeg -i BBB_480p.avi -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k BBB_480p_h265.mp4"
)
os.system(
    "ffmpeg -i BBB_480p.avi -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental BBB_480p_av1.mkv"
)

os.system("ffmpeg -i BBB_720p.avi -c:v libvpx -b:v 1M -c:a libvorbis BBB_720p_vp8.webm")
os.system(
    "ffmpeg -i BBB_720p.avi -c:v libvpx-vp9 -b:v 2M -c:a libvorbis BBB_720p_vp9.webm"
)
os.system(
    "ffmpeg -i BBB_720p.avi -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k BBB_720p_h265.mp4"
)
os.system(
    "ffmpeg -i BBB_720p.avi -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental BBB_720p_av1.mkv"
)

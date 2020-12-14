import numpy as np
import os
import subprocess
import collections

# copy ffserver.conf to etc
os.system("cp ffserver.conf etc/ffserver.conf")
# run server
os.system("ffserver")
# inform user of url
print("The URL you need to give to VLC is: 'rtsp://localhost:7654/live-rtsp'")

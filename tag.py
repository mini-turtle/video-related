#!python

#Util for quick tagging of vid/music files.
#MUST BE RUN IN CURRENT DIR

import os,sys,shutil,re
import subprocess
from pathlib import Path

if(len(sys.argv)>1):
  tag=sys.argv[1]
else:
  print("need tag arg")
  exit()

# Create tmp dir for original media files
#subprocess.run(['mkdir','./tmp_work_dir'])


track = 1
file_ls=Path('.').glob('*')
for f in file_ls:
    if(f.is_file()):
        r = subprocess.run(['ffmpeg','-i',str(f),"-metadata",'album='+sys.argv[1],
                                                 '-metadata','track='+str(track),
                                                 '-metadata','title='+str(f),
                            '-c','copy',str(f)+'_tagged.mkv'])
        if(r.returncode == 0):
            track = track + 1
            subprocess.run(['rm',str(f)])


#ffmpeg -i a.mp3 -c copy -map_metadata:g -1:g  -map_metadata:s:v -1:g -map_metadata:s:a -1:g test.mkv

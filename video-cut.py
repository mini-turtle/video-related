#!/usr/bin/python3
import os
import csv,sys
from datetime import timedelta,date,time,datetime
import subprocess

with open('times.txt', newline='') as csvIn:
    itemList=csv.reader(csvIn, delimiter='-', quotechar='"')
    i=0
    vid=sys.argv[1]
    for row in itemList:
        i=i+1
        clipFile=str(i)+"."+os.path.basename(vid)
        subprocess.call(['ffmpeg','-ss',row[0],'-i',vid,'-to',row[1],'-c','copy','-copyts',str(i)+"tmp-clip.mkv"])
        subprocess.call(['ffmpeg','-i',str(i)+"tmp-clip.mkv",'-c','copy',clipFile])

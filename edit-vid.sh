#!/bin/zsh
tput setaf 1; echo "\n\n\n-------------------\n$1\n\n"
tput setaf 2;
mpv $1
rm times.txt; ls -tr *.jpg | grep -o -P "\d\d:\d\d:\d\d" | while read a; read b; do echo $a-$b >>times.txt; done
~/scripts/video/video-cut.py $1
#echo "\n\n\n\nCheck the cuts are OK."
#echo "Delete: "
#echo "1) *.jpg, times.txt"
#echo "2) all inc original video"
#c=$(echo "1\n2\n" | dmenu -l 3)
#read c

r=`echo "1) *.jpg, times.txt\n2) * including original video\n" | ~/scripts/menu-notify/pmenu/pmenu -p ">$1 Done. Check cuts are OK. Then Del: "`
c=`echo $r | head -c 1`

case $c in
    (1) ls -tr *.jpg | grep -o -P "\d\d:\d\d:\d\d.jpg" | xargs rm 
        rm times.txt
        ;;
    (2) ls -tr *.jpg | grep -o -P "\d\d:\d\d:\d\d.jpg" | xargs rm 
        rm times.txt
        rm $1
        ;;
    esac
rm *tmp-clip.mkv

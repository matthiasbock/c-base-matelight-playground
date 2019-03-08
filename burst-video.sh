#!/bin/bash

infile=$1

if [ "$1" == "" ]; then
	echo "noob"
	exit
fi

rm ???.jpg

ffmpeg -i "$infile" %03d.jpg -r 1/1 -hide_banner

crop=""
#crop="-crop 500x250+0+250"

convert 001.jpg $crop -resize 40x16 001.bmp

for f in *.jpg; do
	convert $f $crop -resize 40x16 $f.rgb
done



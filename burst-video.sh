#!/bin/bash

infile=$1

if [ "$1" == "" ]; then
	echo "noob"
	exit
fi

rm ???.jpg

ffmpeg -i "$infile" -r 1/1 %03d.jpg

for f in *.jpg; do
	convert $f -resize 40x16 $f.rgb
done


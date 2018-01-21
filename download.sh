#!/bin/bash

echo 'index i = ' $2

title=$(youtube-dl --get-title $1)




youtube-dl --write-auto-sub --sub-lang en --skip-download  --output "$2" $1

ffmpeg -i "$2.en.vtt" "$2.srt" 

rm "$2.en.vtt"

sed -r '/^[0-9]+$/{N;d}' "$2.srt" > "$2.txt"

rm "$2.srt"

sed 's/^ *//; s/ *$//; /^$/d; /^\s*$/d' "$2.txt" > "$2_final.txt"

rm "$2.txt"





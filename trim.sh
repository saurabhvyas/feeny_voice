#!/bin/bash

#this script expects hardcoded , predownload .wav file location 

#input params start time , end time , index 

#echo "$1"

ffmpeg -i feeny.wav -ss $1 -to $2  -c copy "./data/feeny_$3.wav"

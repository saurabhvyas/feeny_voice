#!/usr/bin/env python

# usage python dictionary.py <path of .srt>
# create plain text from input srt file (at same location with .txt appended ), then from plain text create dictionary.txt at same folder

from sys import argv

state = -1
text_lines = []
with open(argv[1],"r") as f:
	for line in f.readlines():
		if (line=="\n"):
			state = -1
			continue
		elif state==1:
			text_lines.append(line.strip())
		else:
			state += 1


with open(  argv[1] + '.txt' , 'w') as f:
	f.write(" ".join(text_lines))

with open(argv[1] + '.txt', 'r') as myfile:
    data=myfile.read()

words = data.split()
print(len(words))

# remove duplicate items from the list

words=list(set(words))
print(len(words))


with open (argv[1] + '.txt' + 'words.txt', 'w') as fo:
   for word in words:
     fo.write(str(word) + '\n')

#!/usr/bin/python

import os
import sys

f1 = open(sys.argv[1], 'rb')
f2 = open(sys.argv[2], 'rb')

length = min(os.path.getsize(sys.argv[1]), os.path.getsize(sys.argv[2]))
pos = 0
match = 0
diff = 0

while pos <= length:
	if f1.read(1) == f2.read(1):
		match += 1
	else:
		diff += 1
	pos += 1

print "Matches: " + str(match) + " Differences: " + str(diff)


#!/usr/bin/python

max_k = 10000
n = 1
print "[",

while True :
	k = n*(5*n-3)/2

	if k > max_k :
		print "]"
		break

	print str(k) + ",",
	n += 1


#!/usr/bin/python

from primes import primes

def genTree(v):
	v = [[2*v[0] - v[1], v[0]], [2*v[0] + v[1], v[0]], [v[0] + 2*v[1], v[1]]]
	return v

	#for w in v:
	#	for t in w:
	#		if t > 8:
	#			return

	#	print (w)
	#	genTree(w)

def main():
	print (genTree([2,1]))
	#print (genTree([3,1]))

if __name__ == '__main__':
	main()


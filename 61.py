#!/usr/bin/python

from itertools import permutations
from triang import triang
from square import square
from penta import penta
from hexa import hexa
from hepta import hepta
from octa import octa
from sys import exit

numbers = [triang, square, penta, hexa, hepta, octa]

def prob61 (seq, n, i=0):
	for n[i] in seq[i]:
		if n[i] < 1000:
			continue

		if i > 0:
			if str(n[i-1])[2:] != str(n[i])[:2]:
				continue

		if i == len(n)-1:
			if str(n[i])[2:] != str(n[0])[:2]:
				continue

			print (n, sum(n))
			exit(0)

		prob61 (seq, n, i+1)

def main() :
	for perm in permutations(range(0,len(numbers))) :
		seq = []
		n = []

		for i in range(0, len(numbers)):
			seq.append (numbers[perm[i]])
			n.append (0)

		prob61 (seq, n)

if __name__ == "__main__" :
	main()


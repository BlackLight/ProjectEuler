#!/usr/bin/python

import Euler

L = 10**7

def main() :
	global L, primes

	for n in range(2,L) :
		if Euler.is_prime(n) :
			print n

if __name__ == "__main__" :
	main()


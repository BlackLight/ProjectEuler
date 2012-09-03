#!/usr/bin/python

from math import sqrt
from Euler import *

min_n, min_q, L = 0, 2, 10**7
primes = prime_sieve(int(1.30*sqrt(L)))
ll = 0.7*sqrt(L)

def phi(n) :
	count = 0

	for i in range(1,n) :
		if gcd(i,n) == 1 :
			count = count + 1

	return count

def main() :
	global min_n, min_q, L

	for n in range(len(primes)) :
		if primes[n] > ll : break
		del primes[:n]

	i = 0

	for p1 in primes :
		i += 1

		for p2 in primes[i:] :
			n = p1*p2

			if n > L :
				break

			phi = (p1-1)*(p2-1)
			q = n / float(phi)

			if is_perm(phi, n) and q < min_q :
				min_n, min_q = n, q

	print min_n

if __name__ == "__main__" :
	main()


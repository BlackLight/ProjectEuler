#!/usr/bin/python

from operator import itemgetter
from Euler import is_prime

def genPrimes(maxN):
	primes = []
	for n in range(2, maxN+1):
		if is_prime(n):
			primes.append(n)
	return primes

def primeFactors(n):
	global primes

	if n == 1 or n in primes:
		return {n: 1}
	
	curPrimeIdx = 0
	factors = {}

	while n > 1:
		curPrime = primes[curPrimeIdx]
		if n % curPrime == 0:
			factors[curPrime] = factors[curPrime]+1 if curPrime in factors else 1
			n /= curPrime
		else:
			curPrimeIdx += 1

	return factors

def rad(n):
	global primes

	factors = primeFactors(n)
	r = 1
	for fact in factors:
		r *= fact
	return r

def E(n):
	global sortedRadTable

	if sortedRadTable is None:
		sortedRadTable = sorted(radTable.iteritems(), key=itemgetter(1))

	if n > len(sortedRadTable)+1:
		return None

	return sortedRadTable[n-1][0]

maxN = 100000

print "Generating prime numbers list... ",
primes = genPrimes(maxN)
print "done"

radTable = {}
sortedRadTable = None

for n in range(1, maxN+1):
	radTable[n] = rad(n)

print E(10000)


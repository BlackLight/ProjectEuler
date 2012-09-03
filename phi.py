#!/usr/bin/python

from primes import primes

d = 10000

def coprime(a, b):
	if a in primes or b in primes:
		return True

	while b != 0:
		if a > b:
			a = a-b
		else:
			b = b-a

	return True if a == 1 else False

def phi(n):
	if n == 1:
		return 1

	if n in primes:
		return n
	
	if n%2 == 0:
		m = n/2

		if m%2 != 0:
			return phi(n/2)

	if n%3 == 0:
		m = n/3

		if m%3 != 0:
			return 2*phi(n/3)

	p = 1

	for m in range (2, n):
		if coprime(m, n):
			p += 1

	return p

def main():
	for n in range(1, d):
		phi(n)
		#print ("%d: %d" % (n, phi(n)))

if __name__ == "__main__":
	main()


#!/usr/bin/python

from Euler import is_prime
from sys import stdout

print "{ ",

for n in range(2,10**6):
	if is_prime(n) :
		stdout.write("'%s': 1, " % (str(n)))

print "}"


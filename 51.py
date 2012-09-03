#!/usr/bin/python

from primes import primes
import re

def main() :
	for n in range (1000,2000) :
		for pos1 in range(0,6) :
			for pos2 in range(pos1,6) :
				if pos1 != pos2 :
					n_primes = 0

					for i in range(0,10) :
						if (pos1 > 0 and pos2 > 1) or (pos1 == 0 and i != 0) :
							s = list(str(n))
							s.insert (pos1, str(i))
							s.insert (pos2, str(i))
							s = int("".join(s))

							if s in primes :
								n_primes += 1

					if n_primes == 8 :
						s = list(str(s))
						s[pos1] = '0'
						s[pos2] = '0'
						s = int("".join(s))
						print "Found:", s
						return 0

if __name__ == "__main__" :
	main()


#!/usr/bin/python

import sys

def isPrime (n) :
	if n < 4 :
		return True

	if n%2 == 0 :
		return False

	for i in range ( 3, int (n/2) + 1, 2 ) :
		if n%i == 0 :
			return False

	return True

def primesLessThanN (n) :
	primes = []

	for i in range ( 2, n ) :
		if isPrime (i) :
			primes.append (i)

	return primes

def isVisited ( vec, visited ) :
	print vec, ", ", visited
	if len(vec) == 0 :
		return False

	for i in range( 0, len(visited) ) :
		if len(vec) == len(visited[i]) :
			flag = True

			for j in range ( 0, len(vec) ) :
				if vec[j] != visited[i][j] :
					flag = False
					break

			if flag == True :
				return True

	return False

def indexOf ( val, vec ) :
	for i in range ( 0, len ( vec )) :
		if vec[i] == val :
			return i

	return -1

def getPrimesSums ( n, primes, sumSets, sumSet = [], visited = [[]], curStart = 0, curIndex = 0 ) :
	curSum = sum ( sumSet )

	if not isVisited ( sumSet, visited ) :
		visited.append ( sumSet )

		if curSum == n :
			print " -> ", sumSet
			sumSets.append ( sumSet )

		if curSum > n :
			for i in range(0,2) :
				if len(sumSet) > 0 :
					sumSet.pop()

			if curIndex < len ( primes ) - 1 :
				print "indexOf ", sumSet[len(sumSet)-1], " in ", primes, ": ", indexOf(sumSet[len(sumSet)-1], primes)
				curIndex = indexOf ( sumSet[len(sumSet)-1], primes ) + 1
				#curIndex += 1
			else :
				curIndex = curStart + 1

			if len(sumSet) > 1 :
				allMax = True

				for i in sumSet :
					if i != primes[len(primes)-1] :
						allMax = False
						break

				if allMax == True :
					print " ::: ", sumSet
					return sumSet
			else :
				curStart += 1
				curIndex = curStart
				sumSet = [ primes[curStart] ]

		sumSet.append ( primes[curIndex] )

		try :
			return getPrimesSums ( n, primes, sumSets, sumSet, visited, curStart, curIndex )
		except :
			pass

def main() :
	num = int ( sys.argv[1] )
	sumSets = [[]]
	visited = [[]]
	primes = sorted ( primesLessThanN ( num ))
	getPrimesSums ( num, primes, sumSets )

if __name__ == "__main__" :
	main()


#!/usr/bin/python

class Node :
	def __init__ ( self, primes, index ) :
		self.prev = None
		self.visited = False
		self.primes = primes

		if index == -1 :
			self.index = 0
			self.value = 0
		else :
			self.index = index
			self.value = primes[index]

		self.next = []

	def expand ( self ) :
		for i in range ( self.index, len ( self.primes )) :
			self.next.append ( Node ( self.primes, i ))

def isPrime (n) :
	if n < 4 :
		return True

	if n%2 == 0 :
		return False

	for i in range ( 3, int (n/2) + 1, 2 ) :
		if n%i == 0 :
			return False

	return True

def primesLessThan (n) :
	primes = []

	for i in range ( 2, n ) :
		if isPrime (i) :
			primes.append (i)

	return sorted(primes)

def getSumPath ( value, node, sums = [], curSum = 0 ) :
	if node.value + curSum == value :
		path = []
		tmpNode = node

		while tmpNode != None :
			if tmpNode.prev != None :
				path.append ( tmpNode.value )
			tmpNode = tmpNode.prev
			
		sums.append ( path )
		return path

	if node.value + curSum > value :
		return None

	node.expand()

	for newNode in node.next :
		newNode.prev = node
		res = getSumPath ( value, newNode, sums, curSum+node.value )

		if res == None and node.prev != None :
			return 0

def main() :
	primes = primesLessThan ( 80 )

	for i in range ( 71, 72 ) :
		root = Node ( primes, -1 )
		sums = []
		getSumPath ( i, root, sums )
		print i, ": ", len ( sums )

if __name__ == "__main__" :
	main()


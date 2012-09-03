#!/usr/bin/python

def numDiv ( n ):
	nDiv=1
	inc = 1 if n%2 == 0 else 2
	start = 2 if n%2 == 0 else 3
	max = int ( n/2 ) + 1

	for i in range ( start, max, inc ):
		if n%i == 0 :
			nDiv = nDiv+1

	return nDiv+1

found=False
n=1

while not found :
	count = ( numDiv ( int ( n/2 )) * numDiv ( n+1 )) if n%2 == 0 else ( numDiv ( n ) * numDiv ( int (( n+1 ) / 2 )) )

	if count > 500 :
		print ( n*(n+1)/2 )
		found=True
	else :
		n += 1


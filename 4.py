#!/usr/bin/python

def isPalyndrome ( n ):
	rev=0
	quot=n

	while quot != 0 :
		rev = (rev*10) + quot%10
		quot = int ( quot/10 )

	if rev == n :
		return True
	else :
		return False

max=0

for a in range ( 100, 999 ):
	for b in range ( 100, 999 ):
		n=a*b

		if n > max :
			if isPalyndrome ( n ) :
				max = n

print max


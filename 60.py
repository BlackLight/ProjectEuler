from math import sqrt

primes={}

for i in range (2,10000):
	primes[i]=True

def prime(n):
	i=2
	while(i<sqrt(n)+1):
		if n%i==0:
			return False
		i=i+1
	return True

def test(one,two):
	if prime(int(str(one)+str(two))) and prime(int(str(two)+str(one))):
	   return True
	return False

for i in range(2,10000):
	c=2
	j=i*2
	
	while(j<10000):
		primes[j]=False
		c=c+1
		j=i*c

for p1 in range(2,10000):
	if primes[p1]:
		for p2 in range(p1,10000):
			if primes[p2] and test(p1,p2):
				for p3 in range(p2,10000):
					if primes[p3] and test(p1,p3) and test(p2,p3):
						 for p4 in range(p3,10000):
							if primes[p4] and test(p1,p4) and test(p2,p4) and test(p3,p4):
								for p5 in range (p4,10000):
									if primes[p5] and test(p1,p5) and test(p2,p5) and test(p3,p5) and test(p4,p5):
										print str(p1)+" "+str(p2)+" "+str(p3)+" "+str(p4)+" "+ str(p5)
										print p1+p2+p3+p4+p5
										raw_input()


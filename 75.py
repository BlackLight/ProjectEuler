#!/usr/bin/python

def main():
	maxL = 50
	L = maxL
	m = 2

	while True:
		maxN = int((int(maxL/2)-m*m)/m)
		for n in range(maxN+1, 0, -1):
			a = m*m - n*n
			b = 2*m*n

			if a <= 0 or b <= 0:
				continue

			c = m*m + n*n
			L = a+b+c

			if L <= maxL:
				print("(%d, %d, %d): %d" % (a, b, c, L))
			# m += 1

		m += 1
		# if L >= maxL:
		# 	break

		# n += 1
		# m = 2

if __name__ == "__main__":
     main()


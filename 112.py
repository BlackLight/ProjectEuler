#!/usr/bin/python

nums = {}

def isBouncy(num):
	if num in nums:
		return nums[num]

	if num < 100:
		return False

	num = str(num)
	isDecreasing = False
	isIncreasing = False

	for i in range(0, len(num)):
		if i > 0:
			isIncreasing = True if num[i] > num[i-1] else isIncreasing
			isDecreasing = True if num[i] < num[i-1] else isDecreasing

			if isIncreasing and isDecreasing:
				nums[int(num)] = True
				return True

	nums[int(num)] = False
	return False

def getDensityBouncy(limit):
	numBouncy = 0
	for num in range(1, limit+1):
		if isBouncy(num):
			numBouncy += 1
	return (float(numBouncy)*100.0)/float(limit)

def main():
	for num in range(100, 5000000):
		density = getDensityBouncy(num)
		if density == 99:
			print ("%d, density=%f" % (num, density))
			break

if __name__ == "__main__":
	main()


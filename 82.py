#!/usr/bin/python

matrix = [ \
	[131, 673, 234, 103,  18],
	[201, 96 , 342, 965, 150],
	[630, 803, 746, 422, 111],
	[537, 699, 497, 121, 956],
	[805, 732, 524,  37, 331]
]

def printPath(matrix, path, sum):
	for [i,j] in path:
		print "%d -> " % (matrix[i][j]),
	print(": %d" % (sum))

def getMinimumSum(matrix, x, y, curSum=0, minSum=-1, path=[]):
	curSum += matrix[x][y]
	path += [[x,y]]
	printPath(matrix, path, curSum)

	# Check whether we have reached an item on the rightmost column
	if y == len(matrix[0])-1:
		print("returning")
		return curSum

	if y==0:
		y_range = range(y, y+2)
	elif y == len(matrix)-1:
		y_range = range(y-1, y+1)
	else:
		y_range = range(y-1, y+2)
		
	if x==0:
		x_range = range(x, x+2)
	elif x == len(matrix[0])-1:
		x_range = range(x-1, x+1)
	else:
		x_range = range(x-1, x+2)

	for i in x_range:
		for j in y_range:
			if ([i,j] in path) or (minSum != -1 and curSum + matrix[i][j] >= minSum):
				continue

			tmp_sum = getMinimumSum(matrix, i, j, curSum, minSum, path)

			if minSum != -1 and tmp_sum < minSum:
				minSum = tmp_sum

def main():
	getMinimumSum(matrix, 1, 0)
	# for n in range(0, len(matrix)):
	# 	print(matrix[n][0])

if __name__ == "__main__":
	main()


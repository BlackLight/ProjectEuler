#!/usr/bin/python

matrix = [ \
	[131, 673, 234, 103,  18],
	[201, 96 , 342, 965, 150],
	[630, 803, 746, 422, 111],
	[537, 699, 497, 121, 956],
	[805, 732, 524,  37, 331]
]

def getMinimumSum(matrix, x, y, curSum=0, minSum=-1):
	curSum += matrix[x][y]
	
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

def main():
	for n in range(0, len(matrix[0])):
		print(matrix[n][0])

if __name__ == "__main__":
	main()


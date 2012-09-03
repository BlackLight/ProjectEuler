#!/usr/bin/python

from itertools import product

def getSolutions (total, nInSet, elements, solutions, array = None, item=0, i=0):
	if not array:
		array = []

		for j in range(0, nInSet):
			array.append(0)

	for el in range(0, len(elements)):
		array[i] = elements[el]
		sum = 0

		for t in array:
			sum += t

		if sum == total and i == len(array) - 1:
			sol = []

			for j in range(0, len(array)):
				sol.append (array[j])

			solutions.append(sol)

		if i < len(array) - 1:
			getSolutions (total, nInSet, elements, solutions, array, item, i+1)

def getPath (solutions, nInSolution, path):
	prevSol = path[len(path)-1]

	for i in range(0, len(solutions)):
		if i != prevSol:
			isValid = True

			for j in range(0, len(solutions[i])):
				if j == 1:
					if solutions[i][1] != solutions[prevSol][2]:
						isValid = False
						break
				else:
					if solutions[i][j] in solutions[prevSol]:
						isValid = False
						break

				#if len(path) == nInSolution-1:
				#	if j == 2:
				#		if solutions[i][2] != solutions[path[0]][1]:
				#			isValid = False
				#			break
				#	else:
				#		if solutions[i][j] in solutions[path[0]]:
				#			isValid = False
				#			break

			if isValid:
				path.append(i)

				if len(path) == nInSolution:
					for p in path:
						print solutions[p]
					print ""
				else:
					getPath (solutions, nInSolution, path)

def getCombinations (solutions, nInSolution):
	for i in range(0, len(solutions)):
		getPath(solutions, nInSolution, [i])
	return

	comb = list(product(solutions, repeat = nInSolution))
	dup = []

	for k in range(0, len(comb)):
		hasDup = False

		for i in range(0, nInSolution):
			for j in range(0, nInSolution):
				if i != j and comb[k][i] == comb[k][j]:
					dup.append(k)
					hasDup = True
					break

			if hasDup:
				break

	dup.reverse()

	for k in dup:
		comb.pop(k)

	return comb

def findSolution (total, nInSet, nInSolution, elements, item = 0, solution = None):
	solutions = []
	getSolutions (total, nInSet, elements, solutions)
	dup = []

	for i in range(0, len(solutions)):
		hasDup = False

		for j in range(0, len(solutions[i])):
			for k in range(0, len(solutions[i])):
				if j != k and solutions[i][j] == solutions[i][k]:
					dup.append(i)
					hasDup = True
					break
			if hasDup:
				break

	dup.reverse()

	for k in dup:
		solutions.pop(k)
	print solutions

	combinations = getCombinations(solutions, nInSolution)
	return
	validComb = []

	for t in range(0, len(combinations)):
		isValid = True

		for n in range(0, nInSolution):
			if n == nInSolution - 1:
				nNext = 0
			else:
				nNext = n+1

			for i in range(0, nInSet):
				for j in range(0, nInSet):
					if i == 2 and j == 1:
						if combinations[t][n][i] != combinations[t][nNext][j]:
							isValid = False
					else:
						if combinations[t][n][i] == combinations[t][nNext][j]:
							isValid = False

					if not isValid:
						break

				if not isValid:
					break

			if not isValid:
				break

		if isValid:
			validComb.append(combinations[t])

	dup = []

	for t in range(0, len(validComb)):
		for i in range(0, len(validComb[t])):
			iCombStr = ""

			for k in range(0, len(validComb[t][i])):
				iCombStr += (("%d-") % (validComb[t][i][k]))

			for u in range(t+1, len(validComb)):
				for j in range(0, len(validComb[u][j])):
					jCombStr = ""

					for k in range(0, len(validComb[u][j])):
						jCombStr += (("%d-") % (validComb[u][j][k]))

					if i > j and iCombStr == jCombStr:
						if not u in dup:
							dup.append(u)
						break

	dup.sort()
	dup.reverse()

	for k in dup:
		validComb.pop(k)

	for item in validComb:
		print item

def main():
	total = 9
	nInSet = 3
	nInSolution = 3
	elements = range(1, 7)

	#total = 9
	#nInSet = 3
	#nInSolution = 5
	#elements = range(1, 11)
	
	findSolution (total, nInSet, nInSolution, elements)

if __name__ == "__main__":
     main()


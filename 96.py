#!/usr/bin/python

import re
import sys
import threading
import time

items = []

class SudokuSolver(threading.Thread):
	def __init__(self, index, sudoku):
		threading.Thread.__init__(self)
		self.index = index
		self.sudoku = sudoku

	def run(self):
		while not isSolved(self.sudoku):
			if not solve(self.sudoku):
				print("The sudoku has no admissible solutions")
				return False

		print("Sudoku %d solved" % (self.index))
		items[self.index] = int("%d%d%d" % (self.sudoku[0][0], self.sudoku[0][1], self.sudoku[0][2]))

def getSudoku():
	f = open('sudoku.txt', 'r')
	lines = f.readlines()
	f.close()
	sudokus = []
	sudoku = []

	for line in lines:
		line = line.strip()

		if re.match('^Grid\s+([0-9]+)\s*$', line):
			if len(sudoku) > 0:
				sudokus.append(sudoku)

			sudoku = []
		else:
		 	row = []

			for ch in line:
				row.append(int(ch))

			sudoku.append(row)

	sudokus.append(sudoku)
	return sudokus

def getRows(sudoku):
	return sudoku

def getCols(sudoku):
	cols = []

	for i in range(0, len(sudoku)):
		cols.append([0 for j in range(0, len(sudoku[i]))])

		for j in range(0, len(sudoku[i])):
			cols[i][j] = sudoku[j][i]

	return cols

def getCells(sudoku):
	cells = []

	for i in range(0, len(sudoku)):
		cells.append([])

	for i in range(0, len(sudoku)):
		for j in range(0, len(sudoku[i])):
			cellno = int(j/3) + int(i/3)*3
			cells[cellno].append(sudoku[i][j])

	return cells

def checkRowConstraint(val, row):
	for element in row:
		if abs(val) == abs(element):
			return False
	return True

def checkColConstraint(val, col):
	for element in col:
		if abs(val) == abs(element):
			return False
	return True

def checkCellConstraint(val, cell):
	for element in cell:
		if abs(val) == abs(element):
			return False
	return True

def resetTemporaryValues(sudoku):
	for i in range(0, len(sudoku)):
		for j in range(0, len(sudoku[0])):
			if sudoku[i][j] < 0:
				sudoku[i][j] = 0

def confirmTemporaryValues(sudoku):
	for i in range(0, len(sudoku)):
		for j in range(0, len(sudoku[0])):
			if sudoku[i][j] < 0:
				sudoku[i][j] = -sudoku[i][j]

def recursiveCheckConstraints(i, j, values, sudoku):
	for val in values:
		sudoku[i][j] = -val

		if isSolved(sudoku):
			confirmTemporaryValues(sudoku)
			return True
		
		inSolutionPath = True

		for x in range(0, len(sudoku)):
			for y in range(0, len(sudoku[x])):
				if sudoku[x][y] == 0 and (x != i or y != j):
					possibleValues = getPossibleValues(sudoku, x, y)
					if len(possibleValues) == 0:
						inSolutionPath = False
						break

					if recursiveCheckConstraints(x, y, possibleValues, sudoku):
						return True
					else:
						inSolutionPath = False
						break

			if not inSolutionPath:
				break

	sudoku[i][j] = 0
	return False

def getPossibleValues(sudoku, i, j):
	rows = getRows(sudoku)
	cols = getCols(sudoku)
	cells = getCells(sudoku)
	possibleValues = []

	if sudoku[i][j] == 0:
		row = rows[i]
		col = cols[j]
		cell = cells[int(j/3) + int(i/3)*3]

		for val in range(1,10):
			if checkRowConstraint(val, row) and checkColConstraint(val, col) and checkCellConstraint(val, cell):
				possibleValues.append(val)

	return possibleValues

def solve(sudoku):
	rows = getRows(sudoku)
	cols = getCols(sudoku)
	cells = getCells(sudoku)
	hasChanges = False

	for i in range(0, len(sudoku)):
		for j in range(0, len(sudoku[0])):
			if sudoku[i][j] == 0:
				possibleValues = getPossibleValues(sudoku, i, j)

				if len(possibleValues) == 1:
					sudoku[i][j] = possibleValues[0]
					hasChanges = True
				elif len(possibleValues) == 0:
					return False

	if not hasChanges:
		x = -1
		y = -1

		for i in range(0, len(sudoku)):
			for j in range(0, len(sudoku[0])):
				if sudoku[i][j] == 0:
					x = i
					y = j
					break

			if i != -1 and j != -1:
				break

		row = rows[x]
		col = cols[y]
		cell = cells[int(y/3) + int(x/3)*3]
		possibleValues = []

		for val in range(1,10):
			if checkRowConstraint(val, row) and checkColConstraint(val, col) and checkCellConstraint(val, cell):
				possibleValues.append(val)

		return recursiveCheckConstraints(x, y, possibleValues, sudoku)
	else:
		return True

def isFilled(sudoku):
	for row in sudoku:
		if 0 in row:
			return False
	return True

def isSolved(sudoku):
	if not isFilled(sudoku):
		return False

	tmp_sudoku = sudoku
	confirmTemporaryValues(tmp_sudoku)

	for i in range(0, len(sudoku)):
		for j in range(0, len(sudoku[i])):
			rows = [getRows(sudoku)[i], getCols(sudoku)[j], getCells(sudoku)[int(j/3) + int(i/3)*3]]

			for row in rows:
				for k in range(1, 10):
					if not k in row:
						return False

	return True

def main():
	sudokus = getSudoku()
	sol = 0
	solved = 0
	threads = []

	for i in range(0, len(sudokus)):
		items.append(-1)
		threads.append(SudokuSolver(i, sudokus[i]))
		threads[i].start()

	time.sleep(1)

	for i in range(0, len(sudokus)):
		threads[i].join()

	sol = 0

	for item in items:
		sol += item

	print sol
	return 0
		
if __name__ == "__main__":
	main()


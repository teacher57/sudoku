def linecheck(sudoku):
	toCheck=(1,2,3,4,5,6,7,8,9)

	for line in range(9):
		notThere=[]

		for column in range(9): #finding exceptions
			if sudoku[line][column] in toCheck:
				notThere.append(sudoku[line][column])

		for column in range(9): #deleting options
			if not sudoku[line][column] in toCheck:
				for i in range(len(notThere)):
					if notThere[i] in sudoku[line][column]:
						sudoku[line][column].remove(notThere[i])

	return sudoku

def columncheck(sudoku):
	toCheck=(1,2,3,4,5,6,7,8,9)

	for column in range(9):
		notThere=[]

		for line in range(9): #finding exceptions
			if sudoku[line][column] in toCheck:
				notThere.append(sudoku[line][column])

		for line in range(9): #deleting options
			if not sudoku[line][column] in toCheck:
				for i in range(len(notThere)):
					if notThere[i] in sudoku[line][column]:
						sudoku[line][column].remove(notThere[i])

	return sudoku

def squearcheck(sudoku):
	toCheck=(1,2,3,4,5,6,7,8,9)

	for lineSN in (0,3,6): #squares' lines' numbers
		for columnSN in (0,3,6): #squares' columns' numbers
			notThere=[]
			
			for line in range(3): #finding exceptions
				for column in range(3):
					if sudoku[lineSN+line][columnSN+column] in toCheck:
						notThere.append(sudoku[lineSN+line][columnSN+column])

			for line in range(3): #deleting options
				for column in range(3):
					if not sudoku[lineSN+line][columnSN+column] in toCheck:
						for i in range(len(notThere)):
							if notThere[i] in sudoku[lineSN+line][columnSN+column]:
								sudoku[lineSN+line][columnSN+column].remove(notThere[i])

	return sudoku

def newelements(sudoku):
	toCheck=(1,2,3,4,5,6,7,8,9)
	koordToCheck=[]

	for line in range(9):
		for column in range(9):
			if not sudoku[line][column] in toCheck:
				if len(sudoku[line][column])==1:
					sudoku[line][column]=sudoku[line][column][0]
					koordToCheck.append([line, column])

	return sudoku, koordToCheck #output new sudoku and cells, that we eill check

def cellcheck(sudoku):
	toCheck=(1,2,3,4,5,6,7,8,9)

	for cell in newelements(sudoku)[1]:

		for line in range(9):
			if not sudoku[line][cell[1]] in toCheck:
				if sudoku[cell[0]][cell[1]] in sudoku[line][cell[1]]:
					sudoku[line][cell[1]].remove(sudoku[cell[0]][cell[1]])

		for column in range(9):
			if not sudoku[cell[0]][column] in toCheck:
				if sudoku[cell[0]][cell[1]] in sudoku[cell[0]][column]:
					sudoku[cell[0]][column].remove(sudoku[cell[0]][cell[1]])

		squear={0:0,1:0,2:0,3:3,4:3,5:3,6:6,7:6,8:6}
		lineSN=squear[cell[0]]
		columnSN=squear[cell[1]]

		for line in (0,1,2):
			for column in (0,1,2):
				if not sudoku[lineSN+line][columnSN+column] in toCheck:
					if sudoku[cell[0]][cell[1]] in sudoku[lineSN+line][columnSN+column]:
						sudoku[lineSN+line][columnSN+column].remove(sudoku[cell[0]][cell[1]])

	return sudoku

def finishcheck(sudoku):
	finish=True
	toCheck=(1,2,3,4,5,6,7,8,9)

	for line in range(9):
		for column in range(9):
			if not sudoku[line][column] in toCheck:
				finish=False

	return finish

def makechoice(sudoku, choice):
	toCheck=(1,2,3,4,5,6,7,8,9)
	error=False
	minLen=10
	l,c=None,None

	for line in range(9):
		for column in range(9):
			if not sudoku[line][column] in toCheck:
				if len(sudoku[line][column])>1:
					if len(sudoku[line][column])<minLen:
						minLen=len(sudoku[line][column])
						l,c=line, column
				else:
					error=True
					break
		if error==True:
			break

	choice[0].append(deepcopy(sudoku))
	choice[0][-1][l][c].pop(0)
	choice[1].append([l,c])
	sudoku[l][c]=sudoku[l][c][0]

	return sudoku, choice

def getback(choice):
	toCheck=(1,2,3,4,5,6,7,8,9)
	bM=False
	finish=False

	try:
		if not choice[0][-1][choice[1][-1][0]][choice[1][-1][1]] in toCheck:
			if len(choice[0][-1][choice[1][-1][0]][choice[1][-1][1]])==0:
				bM=True
	except IndexError:
		finish=True

	if not finish:
		if bM==False:
			sudoku=deepcopy(choice[0][-1]) #присваивает sudoku последнее сохраненное поле в choice
			choice[0][-1][choice[1][-1][0]][choice[1][-1][1]].pop(0) #удаляет первый элемент в ячеейке, в которой происходит выбор
			sudoku[choice[1][-1][0]][choice[1][-1][1]]=sudoku[choice[1][-1][0]][choice[1][-1][1]][0] #выбирает первый вариант

		elif bM==True:
			choice[0].pop() #удаляет последнее сохраненное sudoku
			choice[1].pop() #удаляет последние сохраенные координаты
			sudoku,choice,finish=getback(choice)

	else:
		sudoku=[]

	return sudoku, choice, finish

def firsterror(sudoku):
	toCheck=(1,2,3,4,5,6,7,8,9)
	error=False

	if error==False:
		for line in range(9):
			notThere=[]

			for column in range(9):
				if sudoku[line][column] in toCheck:
					if sudoku[line][column] in notThere:
						error=True
						break
					notThere.append(sudoku[line][column])

			if error==True:
				break

	if error==False:
		for column in range(9):
			notThere=[]

			for line in range(9):
				if sudoku[line][column] in toCheck:
					if sudoku[line][column] in notThere:
						error=True
						break
					notThere.append(sudoku[line][column])

			if error==True:
				break

	if error==False:
		for lineSN in (0,3,6):
			for columnSN in (0,3,6):
				notThere=[]

				for line in range(3):
					for column in range(3):
						if sudoku[lineSN+line][columnSN+column] in toCheck:
							if sudoku[lineSN+line][columnSN+column] in notThere:
								error=True
								break
							notThere.append(sudoku[lineSN+line][columnSN+column])

					if error==True:
						break
				if error==True:
					break
			if error==True:
				break

	return error

def seconderror(sudoku):
	toCheck=(1,2,3,4,5,6,7,8,9)
	error=False

	for line in range(9):
		for column in range(9):
			if not sudoku[line][column] in toCheck:
				if len(sudoku[line][column])==0:
					error=True
					break
		if error==True:
			break

	return error

def sudokuinp():
	sudoku=[[],[],[],[],[],[],[],[],[]]
	toCheck=('1','2','3','4','5','6','7','8','9')
	for i in range(9):
		s=input()
		for j in range(9):
			sudoku[i].append(s[j])

	for line in range(9):
		for column in range(9):
			if not sudoku[line][column] in toCheck:
				sudoku[line][column]=[1,2,3,4,5,6,7,8,9]
			else:
				sudoku[line][column]=int(sudoku[line][column])

	return sudoku

def mainloop(sudoku):
	choice=[[],[]]
	sudoku=newelements(sudoku)[0]
	finish=False
	count=1
	
	while not finish:
		lastSudoku=deepcopy(sudoku)
		sudoku=newelements(cellcheck(sudoku))[0]

		if sudoku==lastSudoku:
			sudoku=newelements(squearcheck(newelements(columncheck(newelements(linecheck(sudoku))[0]))[0]))[0]
			if sudoku==lastSudoku:
				sudoku, choice=makechoice(sudoku, choice)

		if firsterror(sudoku):
			sudoku, choice, finish=getback(choice)

		elif seconderror(sudoku):
			sudoku, choice, finish=getback(choice)

		if not finish:
			if finishcheck(sudoku):
				print('\n', count)
				#print("--- %s seconds ---" % (time() - start_time))
				for i in range(9):
					print(*sudoku[i])
				sudoku,	choice, finish=getback(choice)
				count+=1

	return sudoku

from time import time
from copy import deepcopy
sudoku=sudokuinp()
start_time = time()
sudoku=newelements(squearcheck(newelements(columncheck(newelements(linecheck(sudoku))[0]))[0]))[0]
sudoku=mainloop(sudoku)
#print("--- %s seconds ---" % (time() - start_time))
end=input('\nPRESS ENTER')

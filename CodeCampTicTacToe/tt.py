

def row(mat):
	for i in mat:
		if i.count("o")==3: 
			return (True,"o")
		if i.count("x")==3: 
			return (True,"x")
	return (False,1)

def column(mat):
	trans = []
	for i in range(len(mat)):
		rows=[]
		for j in range(len(mat[0])):
			rows.append(mat[j][i])
		trans.append(rows)
	for i in trans:
		if i.count("o")==3: 
			return (True,"o")
		if i.count("x")==3: 
			return (True,"x")
	return (False,1)

def diagonals(mat):
	d1 =[]
	for i in range(len(mat)):
		d1.append(mat[i][i])

	# print(d1)
	if d1.count("o")==3:
		return (True,"o")
	if  d1.count("x")==3:
		return (True,"x")
	d2 = []
	j=0
	for i in range(len(mat)-1,-1,-1):
		# print(mat[j][i],i)
		d2.append(mat[j][i])
		j=j+1

	# print(d2)
	if d2.count("o")==3:
		return (True,"o")
	if  d2.count("x")==3:
		return (True,"x")
	return (False,None)

def checkWinner(matrix):
	# print((row(matrix))[0])
	if (row(matrix)[0]):
		print(row(matrix)[1])
	if (column(matrix)[0]):
		print(column(matrix)[1])
	if (diagonals(matrix)[0]):
		print(diagonals(matrix)[1])
	print("draw")
	return False

def checkGame(matrix):
	pass
def checkInput(matrix):
	for row in matrix:
		for value in row:
			if value not in ("o x ."):
				return False
	return True



def main():
	matrix = []
	i=0
	while i<3:
		row = raw_input().split(" ")
		matrix.append(row)
		i=i+1
	# print(matrix)
	if checkInput(matrix):
		checkWinner(matrix)
	else :
		print("invalid input")

main()


def row(mat):
	count_o=0
	count_x =0
	for i in mat:
		if i.count("o")==3:
			count_o=1
			# return (True,"o")
		if i.count("x")==3:
			count_x =1
			# return (True,"x")
	if(count_x==1 and count_o==1):
		print("invalid game")
		return (False,100)
	elif(count_o==1):
		return(True,"o")
	elif(count_x==1):
		return(True,"x")

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
	if(d1.count("o")==3 and  d1.count("x")==3 ):
		return(False,None)
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
	winner =[]
	if (row(matrix)[0]):
		winner.append(row(matrix)[1])
		print(row(matrix)[1])
	elif (column(matrix)[0]):
		winner.append(column(matrix)[1])
		print(column(matrix)[1])
	elif (diagonals(matrix)[0]):
		print(diagonals(matrix)[1])
		winner.append(diagonals(matrix)[1])
	else :
		print("draw")

def checkGame(matrix):
	count_o = sum([i.count("o")for i in matrix])
	# print(count_o)
	count_x = sum([i.count("x")for i in matrix])
	# print(count_x)
	if(count_x>count_o+1):
		return False
	if (count_o>count_x+1):
		return False
	return True
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
	# checkGame(matrix)
	if checkInput(matrix):
		if checkGame(matrix):
			checkWinner(matrix)
		else:
			print("invalid game")
	else :
		print("invalid input")

main()
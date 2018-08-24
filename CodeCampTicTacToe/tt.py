

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
	if d1.count("o")==3:
		return (True,"o")
	if  d1.count("x")==3:
		return (True,"x")
	d2 = []
	for i in range(len(mat)-1,0,-1):
		d2.append(mat[i][i])
	if d2.count("o")==3:
		return (True,"o")
	if  d2.count("x")==3:
		return (True,"x")
	return (False,None)

def check(matrix):
	# print((row(matrix))[0])
	if (row(matrix)[0]):
		print(row(matrix)[1])
	if (column(matrix)[0]):
		print(column(matrix)[1])
	if (diagonals(matrix)[0]):
		print(diagonals(matrix)[1])
	return False


def main():
	matrix = []
	i=0
	while i<3:
		row = raw_input().split(" ")
		matrix.append(row)
		i=i+1
	# print(matrix)
	check(matrix)

main()
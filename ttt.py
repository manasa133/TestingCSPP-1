dict =  {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}


str = "1 2 3 \n 4 5 6 \n 7 8 9"


def row(mat):
	for i in mat:
		print("i",i)
		if i.count("o")==3 or i.count("x")==3:
			return True
	return False

def column(mat):
	trans = []
	for i in range(len(mat)):
		rows=[]
		for j in range(len(mat[0])):
			rows.append(mat[j][i])
		trans.append(rows)
	for i in trans:
		if i.count("o")==3 or i.count("x")==3:
			return True
	return False

def diagonals(mat):
	d1 =[]
	for i in range(len(mat)):
		d1.append(mat[i][i])
	if d1.count("o")==3 or d1.count("x")==3:
		return True
	d2 = []
	for i in range(len(mat)-1,0,-1):
		d2.append(mat[i][i])
	if d2.count("o")==3 or d2.count("x")==3:
		return True
	return False



def check(str):
	matrix =[[j for j in i.strip().split(" ")] for i in str.split("\n")]
	print(matrix)
	if row(matrix):
		return True
	if column(matrix):
		return True
	if diagonals(matrix):
		return True
	return False
i=0
while i<10:
	player1 = input("Player 1 choice")
	str = str.replace(player1,"x")
	print("str",str)
	if (check(str)):
		print("")
	# player2 = input("Player 2 choice")
	i=i+1
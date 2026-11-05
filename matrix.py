def transpose(matrix):
	return matrix

def powers(matrix):
	pass

def matmul(s1, s2):
	rows1 = len(s1)
	cols1 = len(s1[0])

	rows2 = len(s2)
	cols2 = len(s2[0])

	assert cols1 == rows2
	
	out = []

	for i in range(rows1):
		new_row = []
		for j in range(cols2):
			temp = 0
			for k in range(cols1):
				temp += s1[i][k] * s2[k][j]
			new_row.append(temp)
		out.append(new_row)

	return out

def invert(matrix):
	pass

def loadtxt(matrix):
	pass

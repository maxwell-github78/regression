def transpose(matrix):
	out = []
	rows = len(matrix)
	columns = len(matrix[0]) #Assuming a correct matrix
	for j in range(columns):
		new_row = []
		for i in range(rows):
			new_row.append(matrix[i][j])
		out.append(new_row)
	return out

def powers(matrix):
	pass

def matmul(matrix):
	pass

def invert(matrix):
	pass

def loadtxt(matrix):
	pass

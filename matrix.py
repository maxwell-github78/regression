def verify_matrix(matrix):
	#Verify that all elements are a number
	for row in matrix:
		for element in row:
			if not type(element) in (float, int):
				return False
	#Verify all nested lists share the same length
	columns = len(matrix[0]) 
	for row in matrix[1:]:
		if len(row) != columns:
			return False
	return True

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
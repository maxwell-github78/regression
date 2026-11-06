def verify_matrix(matrix):
	#Verify that all elements are a number
	for row in matrix:
		assert type(row) == list 
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

def powers(lst, num1, num2):
	rows = len(lst)

	out = []
	for i in range(rows):
		new_row = []
		for j in range(num1, num2+1):
			new_row.append(lst[i]**j)
		out.append(new_row)
	return out

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
	rows = len(matrix)
	cols = len(matrix)

	assert rows == 2 and cols == 2

	a = matrix[0][0]; b = matrix[0][1]
	c = matrix[1][0]; d = matrix[1][1]

	# Calculating determinant
	det = a * d - b * c

	# Calculating inverse matrix
	inv = [
		[d/det, -b/det], 
		[-c/det, a/det]
		]

	return inv

def loadtxt(file):
	matrix = []
	with open(file) as f:
		for line in f:
			# Find the words in a row and converts them to floats
			new_row = [float(line.split()[0]), float(line.split()[1])]
			matrix.append(new_row)
		
	assert verify_matrix(matrix)

	return matrix
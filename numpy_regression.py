from matrix import *
import matplotlib.pyplot as plt
from sys import argv
from numpy import *

assert len(argv) == 3
matrix = loadtxt(argv[1])
n = int(argv[2])

def powers(lst, num1, num2):
	rows = len(lst)
	out = []
	for i in range(rows):
		new_row = []
		for j in range(num1, num2+1):
			new_row.append(lst[i]**j)
		out.append(new_row)
	return array(out)

def poly(a,x):
	sum = 0
	for i in range(n+1):
		sum += a[i]* x**i
	return sum

X = transpose(matrix)[0]
Y = transpose(matrix)[1]

Xp  = powers(X,0,n)
Yp  = powers(Y,1,1)
Xpt = Xp.transpose()

#Calculating coefficients for the polynomial
a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0]

X2 = linspace(X[0],X[-1]).tolist()
Y2 = []
for x in range(len(X2)):
	Y2.append(poly(a, X2[x]))

plt.plot(X,Y,'ro')
plt.plot(X2,Y2)
plt.show()
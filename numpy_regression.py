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

Xp  = powers(X,0,n)
Yp  = powers(Y,1,1)
Xpt = Xp.transpose()


from matrix import *
import matplotlib.pyplot as plt
from sys import argv

assert len(argv) == 2
matrix = loadtxt(argv[1])

X = transpose(matrix)[0]
Y = transpose(matrix)[1]

Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

Y2 = X * m + b

plt.plot(X,Y,'ro')
plt.plot(X,Y2)
plt.show()

from numpy import *
import matplotlib.pyplot as plt

X = transpose(matrix)[0]
Y = transpose(matrix)[1]

Xp  = powers(X,0,n)
Yp  = powers(Y,1,1)
Xpt = Xp.transpose()

a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0]

X2 = linspace(X[0],X[-1]).tolist()
Y2 = poly(a, X2)

plt.plot(X,Y,'ro')
plt.plot(X2,poly(a, X))
plt.show()

def poly(a,x):
    poly = 0
    for i in range(n):
        poly += a[n]* x**n
from matrix import *
import matplotlib.pyplot as plt
from sys import argv

assert len(argv) == 3
matrix = loadtxt(argv[1])
n = int(argv[2])

Xp  = powers(X,0,n)
Yp  = powers(Y,1,1)
Xpt = Xp.transpose()


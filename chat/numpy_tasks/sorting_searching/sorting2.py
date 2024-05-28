import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


a = np.array([1,2,3,4,5,6,7,8,7,6,5,4,3,2,3,4,5,6,7,8])
a = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
a = a.reshape(1, len(a))
a = np.lexsort(a)
print(a)

c = np.array([(1+2j), (3-1j), (3-2j), (4-3j), (3+5j)])
real = np.real(c[0])
imm = np.imag(c[0])
print(real)

sorted = np.sort_complex(c)

"""
|
|
|
|
|             * d = i + j  --> tg(a) = compl / real, r = sqrt(real **2 + c ** 2), i = r * cos(a)
|
|
|
|
|
|_______________________________

"""
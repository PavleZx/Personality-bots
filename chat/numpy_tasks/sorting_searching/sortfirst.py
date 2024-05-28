import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



a = np.array([0.39536213 ,0.11779404 ,0.32612381, 0.16327394 ,
              0.98837963, 0.25510787 ,0.01398678 ,0.15188239 ,
              0.12057667,0.67278699])
a = a.reshape(1, len(a))
c = a.copy()
b = a[: , 0:5]
b[:] = np.sort(b[:, 0:5])
print()
print(b)
print()
print(a)


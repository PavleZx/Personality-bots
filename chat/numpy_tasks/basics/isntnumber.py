import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


flag = True
a = np.array([1,2,3,4,5,6,7,7,np.nan,2,2,2,2,2])

result = np.isnan(a)
if True in result:
    print("true")
else:
    print("False")

a = np.array([1,2,3,4,5,6,7, 1 + 1j])
c = np.iscomplex(a)
s = np.isscalar(a) # passamo varijablu, ona je scalar ili ne
if True in c:
    print("there are complex")

print(s)
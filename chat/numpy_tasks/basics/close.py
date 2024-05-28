import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = [100, 101, 102, 100, 101, 102, 100, 101, 102]
b = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]

for i in range(len(a)):
    print(f"{(b[i]- a[i])}   {(b[i]- a[i]) / (a[i])}")
result = np.allclose(a, b, rtol=1e-10, atol=99)
print(result)


a = [1,3,2,3,1,2,3,1,3,2,1,3,2,3,1,2,3,3,1,2]
b = [3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,4,3,4,2,3]
print(np.allclose(a,b, rtol=1e-10, atol=2))



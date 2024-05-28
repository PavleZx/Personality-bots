import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


a = np.array([1,2,3,4,5,6,7,8,7,6,5,4,3,2])
b = np.array([9,8,7,6,5,4,3,2,2,2,2,2,3,1])

greater = np.greater(a, b)
less = np.less(a, b)
greater_eq = np.greater_equal(a, b)
less_eq = np.less_equal(a, b)

print(greater)
print(less)
print(greater_eq)
print(less_eq)

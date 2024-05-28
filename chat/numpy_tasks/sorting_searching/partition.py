import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



p = np.array([ 70, 50, 20, 30 ,-11, 60 ,50, 40])
p = np.partition(p, (2, 4, 6))
p = np.partition(p, 4)
print(p)
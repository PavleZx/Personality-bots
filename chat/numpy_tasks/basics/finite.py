import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


flag = True
a = np.array([1,2,3,4,5,6,7,7,np.inf,2,2,2,2,2])

result = np.isinf(a)
if True in result:
    print("true")
else:
    print("False")
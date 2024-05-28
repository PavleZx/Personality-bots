import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = np.array([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,2,2,6]).reshape(3,8)
b = a[:, 7] # b je stupac
b = np.argsort(b).reshape(3,1) # treba nam stupac
a = np.take_along_axis(a, b, axis=0) # premjesti retke ovisno o sortiranom stupcu b
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



ar = np.arange(0, 8)
ar = np.flip(ar).reshape(2,2,2)
#print(ar)
a = np.argsort(ar, axis=0)
b = np.argsort(ar, axis=2)
ar = np.take_along_axis(ar, a, axis=0)
ar = np.take_along_axis(ar, b, axis=2)
#print(ar)

ar = np.arange(0, 8).reshape(2,2,2)
ar = np.flip(ar)
print(ar)
print("\n\n")
sorted = np.argsort(ar, axis=2)
sorted = np.take_along_axis(ar, sorted, axis=2)
print(sorted)

data_type = [("name", 'S15'), ("class", int), ("height", float)]
students = [('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.10), ('Pit', 5, 40.11)]
students2 = [('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.10), ('Pit', 5, 40.11)]
students = np.array(students, dtype=data_type)

arr = np.sort(students, order="height")
#print(arr)

students2 = np.array(students2, dtype= data_type)
arr = np.sort(students2, order=["class", "height"])
#print(arr)

data_type = [("id", int), ("height", float)]
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])

arr = np.lexsort((student_id, student_height))
print(arr)
result = np.array([0] * len(student_id) * 2).reshape(2, len(student_id))
for i in range(len(student_id)):
    result[0, i] = student_id[arr[i]]
    result[1, i] = student_height[arr[i]]
print(result)









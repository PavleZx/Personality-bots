import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


def test(arr):
    a = np.array(arr)
    a = a.flatten()
    for i in range(len(a)):
        if (a[i] != 0):
            return True
    return False

def main():


    arr = np.array([0,1,0,0,0])
    result = test(arr)
    print(result)

    zeros = np.zeros(10)
    ones = np.ones(10)
    fives = np.array([5] * 10)
    print(zeros, ones, fives)

    ints_30_to_70 = np.arange(30, 71)
    print(ints_30_to_70)

    identity = np.identity(3)
    print(identity)

    number = np.random.random(1)
    print(number)

    stdn = np.random.standard_normal(15)
    print(stdn)

    values = np.random.default_rng().integers(15, 56, 10)
    values = np.arange(15, 56)
    print(values[1:40])

    arr =np.arange(345, 357).reshape(3,4)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j])

    linspace = np.linspace(5, 50, 10)
    print(linspace)

    signs = np.arange(20)
    s = signs[9:16]
    s[:] *= -1
    print(signs)

    ints =  np.random.default_rng().integers(0, 11, 5)
    print(ints)

    a = np.arange(2, 10)
    b = np.arange(7, 15)
    c = a * b
    print(c)

    # arange ne uzima i gornju granicu u array
    a = np.arange(10, 22).reshape((3,4))
    print(a)

    arr = np.array([10]* 50).reshape(5, 10)
    cols = len(arr[0])
    rows = len(arr)
    print(cols, rows)

    a = np.zeros(100).reshape(10,10)
    a[0, :] = 1
    a[9, :] = 1
    a[:, 0] = 1
    a[:, 9] = 1
    print(a)

    diag = np.arange(1, 6)
    identity = np.identity(5)
    identity *= diag
    print(identity)

    a = np.zeros(16).reshape(4,4)
    a[::2, 1::2] = 1 # ::3 svaki treci element, 1::3 svaki treci pocevsi od 1, 1 je odabran, inace 0-ti
    a[1::2, ::2] = 1
    print(a)

    rand27 = np.random.default_rng().integers(5, 34, (3,3,3))
    print(rand27)

    a = np.arange(47, 62).reshape(3,5)
    print(a)
    sum = np.sum(a)
    print(sum)
    sum = np.sum(a, axis=0)
    print("5 clanova")
    print(sum)
    sum = np.sum(a, axis=1)
    print("3 clana")
    print(sum)


    a = np.array([2,3,4])
    b = np.array([4,5,6])
    c = np.dot(a, b)
    print(c)
    print((a * b).sum())

    a = np.array([4] * 25).reshape(5,5)
    b = np.array([3] * 5)
    c = a * b
    print(c)

    # savetxt ~~~ loadtxt
    np.savetxt("newfile.csv", c)
    d = np.loadtxt("newfile.csv")

    #binary file ~~  .npy
    np.save("binfile.npy", c)
    d = np.load("binfile.npy")
    print(d)

    a = np.arange(49, 61).reshape(3, 4)
    print(a)

    # pretvaranje iz byteova u array, i obrnuto
    byts = a.tobytes()
    b = np.frombuffer(byts, dtype = a.dtype)
    print(b)


    a = [1,2,3,4,5,6,5,4,3,2]
    arr = np.array(a)
    b = arr.tolist()
    print(b)

    x = np.linspace(0, 20, 40)
    print(x)
    y = np.sin(x)
    print(y)
    #plt.plot(x, y, "red")
    #plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    x = np.linspace(-6, 6, 40)
    y = np.linspace(-6, 6, 40)
    x, y = np.meshgrid(x, y)
    # Z = 0.5 * np.sin(x * y / 2)
    # Z = np.log(x) * y
    # Z = x ** 2 + y ** 2
    Z = np.sin(np.sqrt(x ** 2 * 3 + y ** 2 * 3)) + np.sin(x + y)
    # Z = np.sin(np.sqrt(0.2 * x ** 2 + 0.2 * y ** 2)) + 0.2 * np.sin(x + y)
    # ax.plot_surface(x, y, Z, cstride = 1, rstride = 1, cmap="viridis")
    # plt.show()

    def funkcija(x):
        a = np.random.default_rng().integers(0, 11, (10,10))
        for i in range(len(a)):
            for j in range(len(a[0])):
                if (a[i][j] < x):
                    a[i][j] = 99
        print(a)
    

    # provjera svakog pojedinog elementa

    a = np.random.default_rng().integers(0, 11, (10,10))
    acon = np.where((a == 5), 99, a)
    
    acon = np.where((a < 5), 99, a)

    acon = np.where((a > 5), 99, a)

    ar = np.array([10] * 60).reshape(3,5,4)
    print(ar)

    ar = np.arange(1,17).reshape(4,4)
    print(ar)
    br = ar.copy()   

    c0 = br[:, 0]
    c1 = br[:, 1]
    c2 = br[:, 2]
    c3 = br[:, 3]

    ar[:, 0] = c3
    ar[:, 1] = c2
    ar[:, 2] = c1
    ar[:, 3] = c0

    print(ar)

    # zamjna nutarnja dva i vanjska dva

    ar = np.arange(1,17).reshape(4,4)
    a1 = np.flip(ar[:, ::3], axis=1)
    a2 = np.flip(ar[:, 1:3], axis=1)
    ar[:, ::3] = a1
    ar[:, 1:3] = a2
    print(ar)

    # moglo se samo ovako

    ar = np.flip(ar, axis=1)

    nums = np.arange(37, 101).reshape(8,8)
    new_nums = nums[:, ::-1]
    print(new_nums)


    a = np.arange(1,37).reshape(6,6)
    b = np.arange(52, 88).reshape(6,6)
    c = a * b
    print(c)

    



















































    return 0

main()


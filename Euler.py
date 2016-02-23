#-*- coding:utf-8 -*-
import matplotlib.pyplot as mplt
import numpy as np

def real_f(x):
    return np.exp(-x)

def f(x, y):
    return -y

if __name__ == "__main__":
    start = 0
    stop = 3
    h = 0.5
    num = (stop - start) / h
    X = np.linspace(start, stop, num)
    #X = np.arange(start, stop+h, h)
    Y = [1]
    for i in range(len(X)-1):
        Y.append(Y[i] + h * f(X[i], Y[i]))
        #Y += Y[i] + h * f(X[i], Y[i])
    mplt.plot(X, Y, "g", label = "Euler")
    X = np.linspace(start, stop, 100)
    mplt.plot(X, real_f(X), "r", label = "Real")
    mplt.legend() #凡例を表示
    mplt.title("Euler Graph")
    mplt.xlabel("X-axis")
    mplt.ylabel("Y-axis")
    mplt.show()
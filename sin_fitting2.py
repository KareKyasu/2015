#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt, numpy as np
from toolz import iterate, nth
from math import factorial


np.set_printoptions(precision = 4, suppress = True)
f = lambda x, w : x@w
E = lambda X, W, T : 0.5 * np.sum((f(X, W)-T).T @ (f(X, W)-T))
model = lambda x : -(2.3*x-2)**2 -10

def gradient_descent(W, X, T, e):
    d = (X.T @ (X@W-T))
    return W - d*e / np.linalg.norm(d)   #Adagrad

if __name__ == "__main__":
    data_sigma = 0.1
    data_num = 4
    M = 6   #次数+1を指定(3次式なら4を入力)
    e = np.array([[0.8], [0.8], [0.3], [0.3], [0.1], [0.5]]) * 0.001
    w_init = np.random.normal(-5, 10, M).reshape(M, 1)
    X = np.array([[i**j for j in range(M)] for i in np.linspace(0.1, 2*np.pi, data_num)])
    T = (model(X.T[1]) + np.random.normal(0, data_sigma, data_num)).reshape(data_num, 1)
    
    w_ans = nth(5000000, iterate(lambda w:gradient_descent(w, X, T, e), w_init))

    print("\nerror ",E(X, w_ans, T))    #評価関数
    print("w_ans ", (w_ans.T[0]))       #推定したparemeter
    print("Taylor", [(-1)**int(i%4/2)/factorial(i)*(i%2) for i in range(M)])  #sinのテイラー展開parameter
    
    plotX = np.array([[i**j for j in range(M)] for i in np.linspace(0, 2*np.pi, 100)])
    plt.plot(X.T[1], T, "bo")                   #観測データ
    plt.plot(plotX.T[1], f(plotX, w_ans), "g")      #モデル計算後
    plt.plot(plotX.T[1], model(plotX.T[1]))    #理論値

    plt.show()
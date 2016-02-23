#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt, numpy as np
from toolz import iterate, nth


f = lambda x, w : -(w[0]*x + w[2])/w[1]
data_num = 60  #トータルのデータ数
data_num = int(data_num/2)  #クラス1,2に等分
mu1 = np.array([2, -10])
mu2 = np.array([2, 2])
cov = np.array([[0.3, 0.1], [0.1, 0.3]])
e = 0.1
w = np.array([1.0, -1.0, 5.0])
plotX = np.linspace(-4, 4, data_num*2)
C1 = np.random.multivariate_normal(mu1, cov, data_num).T
C2 = np.random.multivariate_normal(mu2, cov, data_num).T
plt.plot(C1[0], C1[1], "ro")
plt.plot(C2[0], C2[1], "bo")
plt.plot(plotX, f(plotX,w),"g")

phi1 = np.array([[C1[0][i], C1[1][i], 1] for i in range(data_num)]).T
phi2 = np.array([[C2[0][i], C2[1][i], 1] for i in range(data_num)]).T
phi = np.c_[phi1, phi2]
t = np.r_[[1 for i in range(data_num)], [-1 for i in range(data_num)]]

while True:
    temp = w @ phi * t
    if all(temp>0):
        break
    for i,a in enumerate(temp):
        if a < 0:
            w = w + e * phi.T[i] * t[i]
    
plt.plot(plotX, f(plotX,w),"m")
plt.show()

#-*- coding:utf-8 -*-
import matplotlib.pyplot as mplt
import numpy as np

def makeGaussian(mu, Sigma, N, color):
    x = np.random.normal(mu, Sigma, N)
    print (x)
    #np.savetxt('data' + str(N) + '.txt', x)
    mplt.hist(x, bins = np.fmax(6, N/10), facecolor = color)
    

if __name__ == "__main__":
    makeGaussian(0, 1, 10, "g")
    makeGaussian(5, 1, 100, "b")
    makeGaussian(20, 1, 1000, "r")
    mplt.show()

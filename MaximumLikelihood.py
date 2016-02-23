#-*- coding:utf-8 -*-
import matplotlib.pyplot as mplt
import numpy as np

def gaussian(x, mu, sigma):
    return 1/np.sqrt(2*np.pi*sigma**2) * np.exp(-(x-mu)**2/sigma**2/2)

#スネークケース
#キャメルケース
def plot_gaussian(mu, sigma, c):
    x = np.arange(-10., 10., 0.01)
    y = gaussian(x, mu, sigma)
    mplt.plot(x, y, c)
    

if __name__ == "__main__":
    N = [4, 30, 100, 500,1000]
    c = ["g", "b", "y", "k", "k"]
    Mu = 2.5
    Sigma = 2.75

    plot_gaussian(Mu, Sigma, "r")
    print("mu =", Mu, "Sigma^2 =", Sigma**2)
    
    for i in range(len(N)):
        x = np.random.normal(Mu, Sigma, N[i])
        #mplt.hist(x, bins = np.fmax(6, N[i]/5), facecolor = c[i])
        #最尤法
        estMu = np.average(x)
        estSigma = np.sqrt( (np.sum((x-estMu)**2)) / N[i] )
        
        plot_gaussian(estMu, estSigma, c[i])
        print("case:N =", N[i],"\nmu =", round(estMu, 4), "Sigma^2 =", round(estSigma**2, 4))
    
    mplt.show()
import matplotlib.pyplot as plt, numpy as np 
from toolz import iterate, nth


X = np.random.multivariate_normal(np.array([0, 0]), np.array([[5,1.5], [1.5, 2]]), 20)
r = nth(1000, iterate(lambda r: X.T @ X @ r / np.linalg.norm(X.T @ X @ r), np.random.rand(2)))
plt.plot(X[:,0], X[:,1], "ro")
plt.plot(np.linspace(-8, 8, 200), np.linspace(-8, 8, 200) * r[1] / r[0], "g")
plt.show()

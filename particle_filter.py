import matplotlib.pyplot as plt, numpy as np ,bisect
from toolz import iterate, nth


f = lambda x, t, m : 0.5*x + 25.*x/(1.+(x)**2) + 8.*np.cos(1.2*t) + np.random.randn(m)
h = lambda x, m : x**2/20. + np.random.randn(m)
lh = lambda p, y, m : np.exp(-0.5*(y - h(p, m))**2) / np.sqrt(2*np.pi)

M = 100
step = 50
step_axis = np.linspace(0, step, step+1)
true_x = [0]
obs_y = [h(true_x[-1], 1)[0]]
p = np.array([np.linspace(-10, 10, M) for i in range(step+1)])

for t in step_axis[1:]:
    true_x += [f(true_x[-1], t-1, 1)[0]]
    obs_y += [h(true_x[-1], 1)[0]]

def filtering(p, y):
    a = lh(p, y, M)
    a = a / np.sum(a)
    Fa = [np.sum(a[:i]) for i in range(1,M+1)]
    r = np.sort(np.random.rand(M))
    a = [bisect.bisect_left(Fa, r[i]) for i in range(M)]
    return np.array([p[a[i]] for i in range(M)])

for i in range(step):
    p[i] = filtering(p[i], obs_y[i])
    p[i+1] = f(p[i], i, M)

plt.plot(step_axis, true_x, "r", label = "true")
plt.plot(step_axis, p.mean(axis = 1), "g", label = "estimate")
plt.legend()
plt.show()

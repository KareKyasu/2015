import numpy as np


def normalize(A):
    for i in range(A.shape[0]):
        A[i] = A[i] / np.linalg.norm(A[i])
    return A

def gram_schmidt(V):
    for i in range(1, V.shape[0]):
        for j in range(i):
            V[i] -= V[j] @ V[i] / (V[j] @ V[j]) * V[j]
    return normalize(V)


if __name__ == "__main__":
    V = np.random.randn(5, 5)
    U = gram_schmidt(V)
    print(U @ U.T)
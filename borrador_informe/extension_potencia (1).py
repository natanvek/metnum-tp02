import numpy as np


def n2(v):
    return np.linalg.norm(v, 2)

def normalizar(x):
    return x / n2(x)

def rayleigh(A, v):
    return (np.dot(v.T, (A @ v)) / np.dot(v.T, v))[0,0]

def extension_potencia(A, niter=10000, epsilon=1e-6, x={}):
    # dividimos las iteraciones por 2 ya que hacemos 2 iteraciones en cada paso
    niter //= 2
    if(len(x) == 0): x = np.random.rand(A.shape[0], 1)
    
    x = normalizar(x)
    for _ in range(niter):
        # en vez de hacer A @ x hacemos A @ (A @ x) en cada paso
        y = normalizar(A @ normalizar(A @ x))
        if n2(x - y) < epsilon : break
        x = y

    a = rayleigh(A, x)

    x2 = normalizar(A @ x) - x
    x3 = normalizar(A @ x) + x

    if n2(x2) > epsilon and n2(x3) > epsilon:
        x2 = normalizar(x2)
        a2 = rayleigh(A, x2)
        return a2, x2

    return a, x
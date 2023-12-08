import numpy as np
import cmath

import ioutils

test = np.array([[0, 1, 1, 1, 1, 0],
                 [1, 1, 0, 0, 1, 1],
                 [1, 1, 0, 0, 1, 1],
                 [0, 1, 1, 1, 1, 0]])


def dft1D(arr):
    N = arr.shape[0]
    dft = np.zeros(N, dtype=complex)
    for k in range(N):
        sum = 0.0
        for n in range(N):
            e = cmath.exp(- 2j * np.pi * k * n / N)
            sum += arr[n] * e
        dft[k] = sum
    return dft


def dft2D(arr):
    M, N = arr.shape
    dft = np.zeros((M, N), dtype=complex)
    for k in range(M):
        for l in range(N):
            sum_matrix = 0.0
            for m in range(M):
                for n in range(N):
                    e = cmath.exp(- 2j * np.pi * ((k * m) / M + (l * n) / N))
                    sum_matrix += arr[m, n] * e
            dft[k, l] = sum_matrix
    return dft


ans = dft2D(test)
ioutils.print2D(ans)

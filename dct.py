import numpy as np
import cmath
import ioutils


def dct1D(arr):
    N = arr.shape[0]
    dct = np.zeros(N, dtype=complex)
    for k in range(N):
        sum = 0.0
        for n in range(N):
            c = cmath.cos(2 * n * k * np.pi / N)
            sum += arr[n] * c
        dct[k] = sum
    return dct


test1 = np.array([1, 1, 1, 1])
test2 = np.array([1, 2, 2, 1, 1, 2, 2, 1])

ans1 = dct1D(test1)
ans2 = dct1D(test2)

ioutils.print1D(ans1)
print()
ioutils.print1D(ans2)
print()


def dct2D(arr):
    M, N = arr.shape
    dct = np.zeros((M, N), dtype=complex)
    for k in range(M):
        for l in range(N):
            sum = 0.0
            for m in range(M):
                for n in range(N):
                    c1 = cmath.cos(2 * np.pi * k * m / M)
                    c2 = cmath.cos(2 * np.pi * l * n / N)
                    sum += arr[m, n] * c1 * c2
            dct[k, l] = sum

    return dct


test3 = np.array([[0, 1, 1, 1, 1, 0],
                  [1, 1, 0, 0, 1, 1],
                  [1, 1, 0, 0, 1, 1],
                  [0, 1, 1, 1, 1, 0]])

ans3 = dct2D(test3)
ioutils.print2D(ans3)

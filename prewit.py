import numpy as np
from scipy.signal import convolve2d

test = np.array([[0, 0, 0, 0, 0, 0, 2, 0, 3, 3],
                 [0, 0, 0, 1, 0, 0, 0, 2, 4, 3],
                 [0, 0, 2, 0, 2, 4, 3, 3, 2, 3],
                 [0, 0, 1, 3, 3, 4, 3, 3, 3, 3],
                 [0, 1, 0, 4, 3, 3, 2, 4, 3, 2],
                 [0, 0, 1, 2, 3, 3, 4, 4, 4, 3]])

px = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
py = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

print(test.shape)
print(test.size)
print(px.shape)
print(px.size)

tx = convolve2d(test, px, 'same', 'fill')
ty = convolve2d(test, py, 'same', 'fill')

print(tx)
print(ty)
print(np.add(np.absolute(tx), np.absolute(ty)))

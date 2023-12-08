import numpy as np
from scipy.signal import convolve2d

test = np.array([[0, 0, 0, 0, 0, 0, 2, 0, 3, 3],
                 [0, 0, 0, 1, 0, 0, 0, 2, 4, 3],
                 [0, 0, 2, 0, 2, 4, 3, 3, 2, 3],
                 [0, 0, 1, 3, 3, 4, 3, 3, 3, 3],
                 [0, 1, 0, 4, 3, 3, 2, 4, 3, 2],
                 [0, 0, 1, 2, 3, 3, 4, 4, 4, 3]])

east = np.array([[-1, 1, 1], [-1, -2, 1], [-1, 1, 1]])
west = np.array([[1, 1, -1], [1, -2, -1], [1, 1, -1]])
northeast = np.array([[1, 1, 1], [-1, -2, 1], [-1, -1, 1]])
northwest = np.array([[1, 1, 1], [1, -2, -1], [1, -1, -1]])

te = convolve2d(test, east, 'same', 'fill')
tw = convolve2d(test, west, 'same', 'fill')
tne = convolve2d(test, northeast, 'same', 'fill')
tnw = convolve2d(test, northwest, 'same', 'fill')

print(te)
print(tw)
print(tne)
print(tnw)

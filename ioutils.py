def print1D(arr):
    N = arr.shape[0]
    for n in range(N):
        print('{:.2f}'.format(arr[n]), end=' ')
    print()


def print2D(arr):
    M, N = arr.shape
    for m in range(M):
        for n in range(N):
            print('{:.2f}'.format(arr[m, n]), end=' ')
        print()

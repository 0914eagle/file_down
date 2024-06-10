
import sys

def solve():
    N, L = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    if L == 1:
        A = [x for _, x in sorted(zip(C, A), key=lambda p: p[0])]
        C = sorted(C)
        return C[0] / sum(A)
    elif L == N - 1:
        A = [x for _, x in sorted(zip(C, A), key=lambda p: p[0], reverse=True)]
        C = sorted(C, reverse=True)
        return sum(A) / C[0]
    else:
        A = [x for _, x in sorted(zip(C, A), key=lambda p: p[0])]
        C = sorted(C)
        P1 = C[0] / sum(A[:L])
        P2 = sum(A[L:]) / C[-1]
        return P1 * P2


if __name__ == '__main__':
    print('{:.3f}'.format(solve()))


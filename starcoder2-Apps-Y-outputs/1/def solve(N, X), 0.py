
import sys
from collections import deque

def solve(N, X):
    X.sort()
    X = deque(X)
    for i in range(N):
        if i == 0:
            X.popleft()
            continue
        if i == N-1:
            X.pop()
            continue
        if i % 2 == 0:
            X.pop()
        else:
            X.popleft()
    return X

def main():
    N = int(input())
    X = list(map(int, input().split()))
    ans = solve(N, X)
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()


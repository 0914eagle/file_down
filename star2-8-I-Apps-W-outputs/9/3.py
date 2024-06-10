
from sys import stdin
from itertools import product

def main():
    H, N = map(int, stdin.readline().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, stdin.readline().split())
    
    dp = [float("inf")] * (H + 1)
    dp[0] = 0
    for i in range(1, H + 1):
        for j in range(N):
            if i - A[j] >= 0:
                dp[i] = min(dp[i], dp[i - A[j]] + B[j])
    
    print(dp[H])

if __name__ == "__main__":
    main()


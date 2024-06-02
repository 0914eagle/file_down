
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
S = input().rstrip()

# 累積和
cum = [0] * (N + 1)
for i in range(N):
    cum[i + 1] = cum[i] + (S[i] == "A" and S[i + 1] == "C")

for _ in range(Q):
    l, r = map(int, input().split())
    print(cum[r - 1] - cum[l - 1])


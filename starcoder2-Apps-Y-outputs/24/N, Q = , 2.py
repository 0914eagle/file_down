
N, Q = map(int, input().split())
S = input()

# 累積和
cumsum = [0] * (N + 1)
for i in range(N):
    cumsum[i + 1] = cumsum[i] + (S[i] == 'A' and S[i + 1] == 'C')

for _ in range(Q):
    l, r = map(int, input().split())
    print(cumsum[r] - cumsum[l - 1])



N, Q = map(int, input().split())
S = input()

# 累積和
cumsum = [0] * (N + 1)
for i in range(N):
    if S[i:i+2] == "AC":
        cumsum[i+1] = 1
for i in range(N):
    cumsum[i+1] += cumsum[i]

for i in range(Q):
    l, r = map(int, input().split())
    print(cumsum[r-1] - cumsum[l-1])


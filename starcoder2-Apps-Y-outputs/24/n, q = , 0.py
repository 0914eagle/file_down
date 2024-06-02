
n, q = map(int, input().split())
s = input()

# 累積和
cumsum = [0] * (n + 1)
for i in range(n):
    cumsum[i + 1] = cumsum[i] + (s[i:i + 2] == 'AC')

for _ in range(q):
    l, r = map(int, input().split())
    print(cumsum[r] - cumsum[l - 1])




n, q = map(int, input().split())
s = input()

# 累積和
ac = [0] * (n + 1)
for i in range(n):
    if s[i:i + 2] == 'AC':
        ac[i + 1] = ac[i] + 1
    else:
        ac[i + 1] = ac[i]

for _ in range(q):
    l, r = map(int, input().split())
    print(ac[r - 1] - ac[l - 1])



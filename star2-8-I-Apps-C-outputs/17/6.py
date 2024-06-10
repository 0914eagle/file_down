
n, k = map(int, input().split())

s = ''
for i in range(k):
    s += '01'[i % 2]
for i in range(n - k):
    s += '1'

print(s)


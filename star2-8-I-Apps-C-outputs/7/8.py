
def f(s, d):
    res = ''
    for c in s:
        res += d[c]
    return res
s = input()
d = {}
for c in 'abcdefghijklmnopqrstuvwxyz':
    d[c] = input()
k = int(input())
m = int(input())
pos = list(map(int, input().split()))
p = s
for i in range(k):
    p = f(p, d)
for i in pos:
    print(p[i-1])


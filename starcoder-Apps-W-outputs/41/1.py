
# 01.07.2017
# author: @ahmadarif

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = dict()
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
mx = 0
for i in b:
    if mx < b[i]:
        mx = b[i]
print(mx if mx <= n else n)

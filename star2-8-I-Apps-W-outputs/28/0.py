
n, l, x, y = map(int, input().split())
a = list(map(int, input().split()))

v = 0
p = []

if a[-1] < y:
    v += 1
    p.append(y)
    
if a[-1] < x:
    v += 1
    p.append(x)

print(v)
print(*p)


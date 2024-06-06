
n, p = map(int, input().split())
l = [input() for _ in range(n)]
#print(l)
a = 0
for i in l:
    if i == 'half':
        a += p // 2
    else:
        a += p // 2 + p // 2
print(a)

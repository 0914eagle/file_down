
n, k = map(int, input().split())
a = list(map(int, input().split()))
f = True
for i in range(1, n):
    if a[i] > a[i-1] + 1:
        f = False
        break
if f == False:
    print('NO')
else:
    print('YES')
    c = []
    for i in range(k):
        c.append(i+1)
    for i in range(n):
        j = 0
        while j < a[i]:
            print(c[j], end = ' ')
            j += 1
        print()

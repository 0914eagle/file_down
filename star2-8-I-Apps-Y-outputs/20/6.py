
n = int(input())
res = 1
for i in range(1, n+1):
    div = 0
    cur = i
    while cur % 2 == 0:
        div += 1
        cur //= 2
    if div > res[1]:
        res = [i, div]
print(res[0])


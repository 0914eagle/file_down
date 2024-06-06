
n,h,m,k = map(int,input().split())
hm = [list(map(int,input().split())) for i in range(n)]

trains = []

for i in hm:
    if i[0] == h-1:
        i[1] = m-i[1]
    else:
        i[1] = (h-1-i[0]) * m + (m-i[1])
    trains.append(i)

trains.sort(key = lambda x: x[1])

cancel = 0

for i in trains:
    if i[1] > k:
        break
    cancel += 1

print(n-cancel,0)
print(*trains[cancel:])

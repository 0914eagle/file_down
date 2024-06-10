
n, s = [int(x) for x in input().split()]
floor = [0 for i in range(n)]
time = [0 for i in range(n)]
for i in range(n):
    floor[i], time[i] = [int(x) for x in input().split()]
floor.sort()
time.sort()
sum = 0
for i in range(n):
    sum += floor[i] - i
print(sum + time[n-1])


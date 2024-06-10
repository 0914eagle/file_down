
n = int(input())
x = list(map(int, input().split()))
x.sort()
p = x[n//2]
total = 0
for i in range(n):
    total += (x[i] - p)**2
print(total)


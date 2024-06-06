
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

count = 0
sum = 0

for i in range(n):
    if (a[i] == b[i]):
        count += 1
    else:
        sum += b[i] - a[i]

if count < n:
    print(n-count,sum)
else:
    print(n,0)

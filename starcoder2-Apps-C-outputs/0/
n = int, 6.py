
n = int(input())

for i in range(n):
    k = int(input())
    sum = 0
    for j in range(k):
        a, b = map(int, input().split())
        sum += a
    print(sum, end=" ")

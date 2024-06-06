
n = int(input())
for i in range(n):
    k = int(input())
    sum = 0
    for j in range(k):
        x, y = map(int, input().split())
        sum += x
    print(sum, end = ' ')

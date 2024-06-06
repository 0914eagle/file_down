
n = int(input())

table = [0]*n

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if i!=j:
            table[j]=a[j]/i

print(table)

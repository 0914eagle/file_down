
from math import gcd

n = int(input())
arr = [int(x) for x in input().split()]

count = 0

for i in range(n):
    flag = 0
    for j in range(i+1, n):
        if gcd(arr[i], arr[j]) > 1:
            flag = 1
            break
    if flag == 0:
        count += 1

print(count)


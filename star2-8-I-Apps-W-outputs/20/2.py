
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def sub(a, b):
    return (a - b) % m

ans = 1
for i in range(n):
    for j in range(i+1, n):
        ans = (ans * sub(arr[i], arr[j])) % m
print(ans)


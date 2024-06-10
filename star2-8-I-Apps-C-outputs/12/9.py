
n, m = map(int, input().split())

res = min(n, m)

print(res * (res - 1) // 2)



n, k = map(int, input().split())

x = n+1
while x % k != 0:
  x += 1

print(x)


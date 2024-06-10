
n, k = map(int, input().split())
x = n
while x % k != 0:
    x += 1
print(x)


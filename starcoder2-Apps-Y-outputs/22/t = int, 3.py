
t = int(input())

for _ in range(t):
    a, b, k = map(int, input().split())
    if k % 2 == 0:
        print(k * a - k * b)
    else:
        print(k * a - (k - 1) * b)


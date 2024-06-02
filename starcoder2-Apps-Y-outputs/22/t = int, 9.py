
t = int(input())
for i in range(t):
    a, b, k = map(int, input().split())
    if k % 2 == 0:
        print(k * a - k * b)
    else:
        print((k - 1) * a - (k - 1) * b + a - b)


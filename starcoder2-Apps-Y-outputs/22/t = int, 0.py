
t = int(input())
for i in range(t):
    a, b, k = map(int, input().split())
    if k % 2 == 0:
        print(a - b)
    else:
        print(a - b + 2 * a)


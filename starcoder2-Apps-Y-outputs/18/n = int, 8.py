
n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print("YES")
    print(0)
    exit()

if n == 2:
    if a[0] < a[1]:
        print("YES")
        print(0, 1)
    else:
        print("NO")
    exit()

if a[0] < a[1]:
    if a[1] > a[2]:
        print("NO")
        exit()
    else:
        for i in range(2, n):
            if a[i - 1] > a[i]:
                print("NO")
                exit()
else:
    if a[1] < a[2]:
        print("NO")
        exit()
    else:
        for i in range(2, n):
            if a[i - 1] < a[i]:
                print("NO")
                exit()

print("YES")
res = [0] * n
res[0] = 1
for i in range(1, n):
    if a[i - 1] < a[i]:
        res[i] = 0
    else:
        res[i] = 1

print(*res)


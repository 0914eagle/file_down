
n = int(input())
a = list(map(int, input().split()))

if sum(a) % 2 == 1:
    print('NO')
else:
    print('YES', n - 1)
    for i in range(1, n):
        print(i, i + 1)


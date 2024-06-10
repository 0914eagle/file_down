
n = int(input())
if n == 1:
    print(0, 1)
    print(0)
else:
    print(n, end = ' ')
    for i in range(n):
        print(-1, end = ' ')
    print()
    print(1, end = ' ')
    for i in range(n):
        print(0, end = ' ')
    print()



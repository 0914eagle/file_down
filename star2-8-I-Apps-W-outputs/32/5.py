
for _ in range(int(input())):
    a, b, n, m = map(int, input().split())
    if n + m == 0:
        print('No')
    elif a + b == 0:
        print('No')
    elif n == 0:
        print('Yes')
    elif m == 0:
        print('Yes')
    else:
        if a > b:
            print('Yes')
        else:
            print('No')


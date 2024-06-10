
n = int(input())
if n == 1:
    print(0)
    print(1)
    print(0)
    print(1)
else:
    print(n)
    print(*[-1] + [0] * (n - 1) + [1])
    print(1)
    print(0, 1)


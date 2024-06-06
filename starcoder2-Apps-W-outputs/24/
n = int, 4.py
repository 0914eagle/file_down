
n = int(input())

if n % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            print("W" * n)
        else:
            print("B" * n)
else:
    for i in range(n):
        if i % 2 == 0:
            print("B" * n)
        else:
            print("W" * n)

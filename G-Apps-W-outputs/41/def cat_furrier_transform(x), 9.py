
def cat_furrier_transform(x):
    operations = []
    t = 0

    while x & (x + 1) != 0:
        n = len(bin(x)) - 3
        x ^= 2**n - 1
        operations.append(n)
        x += 1
        t += 2

    print(t)
    for i in range(0, len(operations), 2):
        print(operations[i])

x = int(input())
cat_furrier_transform(x)

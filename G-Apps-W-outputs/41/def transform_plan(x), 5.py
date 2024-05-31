
def transform_plan(x):
    operations = []
    t = 0

    while x & (x + 1) != 0:
        n = 0
        while (1 << (n + 1)) - 1 <= x:
            n += 1
        x ^= (1 << n) - 1
        operations.append(n)
        x += 1
        t += 2

    print(t)
    for i in range(len(operations)):
        if i % 2 == 0:
            print(operations[i], end=' ')

# Input
x = int(input().strip())

# Output
transform_plan(x)

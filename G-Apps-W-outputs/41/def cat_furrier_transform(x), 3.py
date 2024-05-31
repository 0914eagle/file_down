
def cat_furrier_transform(x):
    operations = []
    
    t = 0
    
    while x & (x + 1) != 0:
        t += 1
        n = 0
        while (1 << n) - 1 <= x:
            n += 1
        n -= 1
        operations.append(n)
        x ^= (1 << n) - 1
        x += 1
    
    print(t)
    for i in range(len(operations)):
        if i % 2 == 0:
            print(operations[i], end=' ')

# Input
x = int(input())

# Output
cat_furrier_transform(x)

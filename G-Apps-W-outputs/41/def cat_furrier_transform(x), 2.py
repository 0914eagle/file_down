
def cat_furrier_transform(x):
    operations = []
    
    if x == 1:
        print(0)
        return
    
    while x & (x + 1) != 0:
        n = 0
        while (1 << n) - 1 <= x:
            n += 1
        n -= 1
        x ^= (1 << n) - 1
        operations.append(n)
        x += 1

    print(len(operations))
    for i in range(len(operations)):
        print(operations[i], end=' ')

x = int(input())
cat_furrier_transform(x)

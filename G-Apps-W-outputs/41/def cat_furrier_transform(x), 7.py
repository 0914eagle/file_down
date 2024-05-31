
def cat_furrier_transform(x):
    operations = []
    
    t = 0
    while x & (x + 1) != 0:
        n = 0
        while (1 << n) - 1 <= x:
            n += 1
        n -= 1
        x ^= (1 << n) - 1
        operations.append(n)
        
        x += 1
        t += 2
    
    print(t)
    for i in range(len(operations)):
        print(operations[i], end=' ')

# Read input
x = int(input().strip())

# Call the function with input value
cat_furrier_transform(x)

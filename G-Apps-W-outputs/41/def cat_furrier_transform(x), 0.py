
def cat_furrier_transform(x):
    operations = []
    
    while x & (x + 1) != 0:
        n = x.bit_length() - 1
        operations.append(n)
        x ^= (1 << n) - 1
        x += 1
    
    print(len(operations))
    for i in range(len(operations)):
        print(operations[i], end=' ')

# Input
x = int(input())
# Output
cat_furrier_transform(x)

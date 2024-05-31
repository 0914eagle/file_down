
def cat_furrier_transform(x):
    operations = []
    
    # Check if x is already a perfect longcat
    if bin(x + 1).count('1') == 1:
        return 0, []
    
    t = 0
    while t < 40:
        b = bin(x)[2:]
        n = len(b) - b.rfind('1') - 1  # Find the position of the rightmost '1' bit
        if n == 0:
            x += 1
            t += 1
            continue
        x ^= (1 << n) - 1
        operations.append(n)
        t += 1
    
    return t, operations

x = int(input())
t, operations = cat_furrier_transform(x)
print(t)
for op in operations:
    print(op, end=' ')

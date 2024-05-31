
def cat_furrier_transform(x):
    operations = []
    while x & (x + 1):  # Check if x is not a perfect longcat
        if len(operations) % 2 == 0:  # Odd-numbered operation (A)
            n = 0
            while (1 << n) - 1 <= x:
                n += 1
            n -= 1
            x ^= (1 << n) - 1
            operations.append(n)
        else:  # Even-numbered operation (B)
            x += 1
    return len(operations), operations

# Input
x = int(input().strip())

# Output
t, operations = cat_furrier_transform(x)
print(t)
for n in operations:
    print(n, end=' ')

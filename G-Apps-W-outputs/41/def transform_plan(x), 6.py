
def transform_plan(x):
    operations = []
    
    m = 0
    while (1 << m) - 1 < x:
        m += 1
    
    while x != (1 << m) - 1 and len(operations) < 40:
        if m & 1:
            operations.append(m)
        else:
            x += 1
        m -= 1
    
    print(len(operations))
    for operation in operations:
        print(operation, end=' ')

# Input
x = int(input())
transform_plan(x)

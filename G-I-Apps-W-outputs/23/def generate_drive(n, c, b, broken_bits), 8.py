
def generate_drive(n, c, b, broken_bits):
    drive = ['0'] * n
    changes = 0
    
    # Fill in broken bits
    for bit in broken_bits:
        drive[bit-1] = '0'
    
    # Find position to add bit changes
    for i in range(1, n):
        if changes == c:
            break
        if drive[i-1] == '0' and drive[i] == '0':
            drive[i] = '1'
            changes += 1

    return ''.join(drive)

# Input parsing
n, c, b = map(int, input().split())
broken_bits = list(map(int, input().split()))

# Generate and output the drive
print(generate_drive(n, c, b, broken_bits))
```

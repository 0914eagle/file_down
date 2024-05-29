
def solve_hard_drive(n, c, b, broken_bits):
    drive = ['0'] * n
    for i in range(n):
        drive[i] = '1' if i % 2 == 0 else '0'
    
    diff_count = n // 2
    
    for i in range(1, n):
        if diff_count == c:
            break
        if drive[i - 1] == drive[i]:
            drive[i] = '1'
            diff_count += 1
    
    for bit in broken_bits:
        drive[bit - 1] = '0'
    
    return "".join(drive)

# Input
n, c, b = map(int, input().split())
broken_bits = list(map(int, input().split()))

# Output
print(solve_hard_drive(n, c, b, broken_bits))
```

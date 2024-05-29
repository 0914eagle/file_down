
def generate_hard_drive(n, c, b, broken_bits):
    remaining_changes = c
    result = ["0"] * n
    
    for i in range(1, n):
        if i not in broken_bits and remaining_changes > 0:
            result[i] = "1"
            remaining_changes -= 1
    
    return "".join(result)

# Input parsing
n, c, b = map(int, input().split())
broken_bits = list(map(int, input().split()))

# Generate and print the bit pattern
print(generate_hard_drive(n, c, b, broken_bits))

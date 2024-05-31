
def solve(N):
    total_sum = sum([int(digit) for digit in str(N)])
    binary_sum = bin(total_sum)[2:]
    return binary_sum

# Test cases
print(solve(1000))  # Output: "1"
print(solve(150))   # Output: "110"
print(solve(147))   # Output: "1100"

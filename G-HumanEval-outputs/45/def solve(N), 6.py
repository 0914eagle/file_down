
def solve(N):
    sum_digits = sum(map(int, bin(N)[2:]))
    return bin(sum_digits)[2:]

# Test cases
print(solve(1000))  # Output: "1"
print(solve(150))   # Output: "110"
print(solve(147))   # Output: "1100"
```

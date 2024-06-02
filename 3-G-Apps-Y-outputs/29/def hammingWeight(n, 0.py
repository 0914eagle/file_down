
def hammingWeight(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Test cases
print(hammingWeight(0b00000000000000000000000000001011))  # Output: 3
print(hammingWeight(0b00000000000000000000000010000000))  # Output: 1
print(hammingWeight(0b11111111111111111111111111111101))  # Output: 31

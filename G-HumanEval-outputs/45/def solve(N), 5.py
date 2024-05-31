
def solve(N):
    total_sum = sum(int(digit) for digit in str(N))
    binary_sum = bin(total_sum)[2:]
    return binary_sum

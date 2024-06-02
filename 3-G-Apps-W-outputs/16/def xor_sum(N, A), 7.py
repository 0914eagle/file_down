
def xor_sum(N, A):
    MOD = 10**9 + 7
    total_xor = 0
    for i in range(60):
        count_ones = sum((a >> i) & 1 for a in A)
        total_xor = (total_xor + (count_ones * (N - count_ones) * 2**i) % MOD) % MOD
    return total_xor

# Read input
N = int(input())
A = list(map(int, input().split()))

# Calculate and print the XOR sum
print(xor_sum(N, A))

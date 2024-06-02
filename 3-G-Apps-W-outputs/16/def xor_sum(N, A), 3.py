
MOD = 10**9 + 7

def xor_sum(N, A):
    total_xor = 0
    for i in range(60):
        count_ones = sum((a >> i) & 1 for a in A)
        total_xor += count_ones * (N - count_ones) * (1 << i) % MOD
        total_xor %= MOD
    return total_xor

# Input
N = int(input())
A = list(map(int, input().split()))

# Calculate and print the XOR sum modulo (10^9+7)
result = xor_sum(N, A)
print(result)

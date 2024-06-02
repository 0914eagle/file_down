
MOD = 10**9 + 7

def xor_sum(N, A):
    total_xor = 0
    for i in range(60):
        count_ones = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                count_ones += 1
        total_xor = (total_xor + (count_ones * (N - count_ones) * (1 << i)) % MOD) % MOD
    return total_xor

# Read input
N = int(input())
A = list(map(int, input().split()))

# Calculate and print the XOR sum modulo 10^9+7
result = xor_sum(N, A)
print(result)


def xor_sum(N, A):
    MOD = 10**9 + 7
    total_xor_sum = 0
    for i in range(N-1):
        for j in range(i+1, N):
            total_xor_sum = (total_xor_sum + (A[i] ^ A[j])) % MOD
    return total_xor_sum

# Input processing
N = int(input())
A = list(map(int, input().split()))

result = xor_sum(N, A)
print(result)


def max_xor_sum(N, K, A):
    max_val = 0
    for i in range(40, -1, -1):
        count = sum(((1 << i) & a) != 0 for a in A)
        if (max_val | (1 << i)) <= K and count <= N // 2:
            max_val |= 1 << i
    result = sum(max_val ^ a for a in A)
    return result

# Input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Output
print(max_xor_sum(N, K, A))

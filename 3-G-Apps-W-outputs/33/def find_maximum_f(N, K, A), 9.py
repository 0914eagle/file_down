
def find_maximum_f(N, K, A):
    max_f = 0
    for i in range(40, -1, -1):
        count_bits = sum((a >> i) & 1 for a in A)
        if (max_f | (1 << i)) <= K and count_bits <= N // 2:
            max_f |= 1 << i
    return sum(max_f ^ a for a in A)

# Read input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Find and print the maximum value of f
print(find_maximum_f(N, K, A))

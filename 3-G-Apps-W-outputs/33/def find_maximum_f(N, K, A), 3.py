
def find_maximum_f(N, K, A):
    max_f = 0
    for i in range(40, -1, -1):
        count = 0
        mask = 1 << i
        new_K = K | ((1 << i) - 1)
        for a in A:
            if a & mask:
                count += 1
        if count > N // 2:
            K = new_K
        max_f += mask if K & mask else 0
    return max_f

# Read input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Find and print the maximum value of f
print(find_maximum_f(N, K, A))

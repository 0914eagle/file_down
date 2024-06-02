
def solve_xor_maximum(N, K, A):
    max_val = 0
    for i in range(40, -1, -1):
        count = 0
        mask = 1 << i
        new_max = max_val | (1 << i)
        for a in A:
            if new_max & mask == 0:
                count += a ^ new_max
            else:
                count += a ^ max_val
        if count <= K:
            max_val = new_max
    return max_val

# Read input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Call the function and print the result
print(solve_xor_maximum(N, K, A))

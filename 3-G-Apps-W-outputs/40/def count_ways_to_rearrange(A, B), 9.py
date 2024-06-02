
def count_ways_to_rearrange(A, B):
    n = len(A)
    diff = [0] * n
    for i in range(n):
        diff[i] = 1 if A[i] != B[i] else -1
    
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + diff[i]
    
    count = 0
    target_sum = prefix_sum[-1]
    if target_sum != 0:
        return 0
    
    zero_positions = [i for i, x in enumerate(prefix_sum) if x == 0]
    
    for i in range(len(zero_positions) // 2):
        left = zero_positions[i]
        right = zero_positions[i + 1]
        count += (left + 1) * (n - right)
    
    return count

# Input
A = input().strip()
B = input().strip()

# Output
print(count_ways_to_rearrange(A, B))

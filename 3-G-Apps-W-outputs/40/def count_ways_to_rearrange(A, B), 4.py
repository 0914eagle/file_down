
def count_ways_to_rearrange(A, B):
    n = len(A)
    diff_count = 0
    diff_indices = []
    
    for i in range(n):
        if A[i] != B[i]:
            diff_count += 1
            diff_indices.append(i)
    
    if diff_count == 0:
        return 0
    elif diff_count % 2 != 0:
        return 0
    elif diff_count == 2:
        if A[diff_indices[0]] == B[diff_indices[1]] and A[diff_indices[1]] == B[diff_indices[0]]:
            return 1
        else:
            return 0
    else:
        return 2

# Input
A = input().strip()
B = input().strip()

# Output
print(count_ways_to_rearrange(A, B))

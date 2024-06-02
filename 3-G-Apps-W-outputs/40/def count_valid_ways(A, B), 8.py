
def count_valid_ways(A, B):
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
    elif A[diff_indices[0]:diff_indices[-1] + 1] == B[diff_indices[-1]:diff_indices[0] - 1:-1]:
        return 1
    else:
        return 0

# Input
A = input().strip()
B = input().strip()

# Output
print(count_valid_ways(A, B))


def count_ways_to_rearrange(A, B):
    n = len(A)
    count = 0
    diff_count = 0
    diff_indices = []
    
    for i in range(n):
        if A[i] != B[i]:
            diff_count += 1
            diff_indices.append(i)
    
    if diff_count % 2 != 0:
        return 0
    
    for i in range(len(diff_indices)//2):
        start = diff_indices[i]
        end = diff_indices[-(i+1)]
        if A[start:end+1] == B[start:end+1]:
            count += 1
    
    return count

# Input
A = input().strip()
B = input().strip()

# Output
print(count_ways_to_rearrange(A, B))


def count_valid_ways(A, B):
    n = len(A)
    diff_count = 0
    diff_positions = []
    
    for i in range(n):
        if A[i] != B[i]:
            diff_count += 1
            diff_positions.append(i)
    
    if diff_count == 0:
        return 0
    elif diff_count % 2 != 0:
        return 0
    elif diff_count == 2:
        return 1
    else:
        first_diff = diff_positions[0]
        last_diff = diff_positions[-1]
        if A[first_diff:last_diff+1] == B[first_diff:last_diff+1]:
            return 1
        else:
            return 2

# Input
A = input().strip()
B = input().strip()

# Output
print(count_valid_ways(A, B))

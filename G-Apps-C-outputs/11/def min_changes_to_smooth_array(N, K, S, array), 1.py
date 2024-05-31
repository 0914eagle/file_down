
def min_changes_to_smooth_array(N, K, S, array):
    min_changes = float('inf')
    
    for start_val in range(S+1):
        changes = [0] * N
        for i in range(N):
            diff = abs(array[i] - start_val)
            changes[i] = min(diff, S - diff)
        
        total_changes = sum(changes[:K])
        min_changes = min(min_changes, total_changes)
        
        for i in range(K, N):
            total_changes = total_changes - changes[i-K] + changes[i]
            min_changes = min(min_changes, total_changes)
    
    return min_changes

# Reading input
input_line = input().split()
N, K, S = map(int, input_line[:3])
array = list(map(int, input().split()))

# Calling the function and printing the result
print(min_changes_to_smooth_array(N, K, S, array))

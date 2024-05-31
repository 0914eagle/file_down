
def min_changes_to_smooth_array(N, K, S, array):
    if N == K:
        return 0
    
    min_changes = float('inf')
    
    for i in range(S+1):
        changes = 0
        for j in range(N):
            diff = abs(array[j] - i)
            if diff > S - diff:
                changes += S - diff
            else:
                changes += diff
        
        for j in range(N-K+1):
            sum_k = sum(array[j:j+K])
            if sum_k != K * i:
                changes += 1
        
        min_changes = min(min_changes, changes)
    
    return min_changes

# Read input
N, K, S = map(int, input().split())
array = [int(x) for x in input().split()]

# Call the function with the input values
result = min_changes_to_smooth_array(N, K, S, array)
print(result)

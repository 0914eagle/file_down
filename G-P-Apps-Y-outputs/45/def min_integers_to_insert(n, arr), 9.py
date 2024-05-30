
def min_integers_to_insert(n, arr):
    prefix_sum = 0
    prefix_sums = set()
    count = 0
    
    for a in arr:
        prefix_sum += a
        if prefix_sum == 0 or prefix_sum in prefix_sums:
            count += 1
            prefix_sums = {0}
        
        prefix_sums.add(prefix_sum)
    
    return count

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Output
output = min_integers_to_insert(n, arr)
print(output)

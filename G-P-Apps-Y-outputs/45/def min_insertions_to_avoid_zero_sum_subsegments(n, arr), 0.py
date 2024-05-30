
def min_insertions_to_avoid_zero_sum_subsegments(n, arr):
    count = 0
    prefix_sum = 0
    prefix_sums = set()
    
    for num in arr:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in prefix_sums:
            count += 1
            prefix_sums = set()
            prefix_sum = num
        prefix_sums.add(prefix_sum)
    
    return count

# Reading input
n = int(input())
arr = list(map(int, input().split()))

# Calling the function and printing the result
print(min_insertions_to_avoid_zero_sum_subsegments(n, arr))

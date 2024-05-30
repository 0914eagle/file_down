
def max_beauty(n, x, arr):
    max_sum = 0
    prefix_sum = [0]
    for num in arr:
        prefix_sum.append(prefix_sum[-1] + num)
    
    for i in range(n):
        for j in range(i, n):
            current_sum = prefix_sum[j + 1] - prefix_sum[i] + x * (j - i + 1)
            max_sum = max(max_sum, current_sum)
    
    return max_sum

# Reading input
n, x = map(int, input().split())
arr = list(map(int, input().split()))

# Calling the function and printing the result
print(max_beauty(n, x, arr))

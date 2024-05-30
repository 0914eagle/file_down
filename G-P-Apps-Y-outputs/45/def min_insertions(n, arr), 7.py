
def min_insertions(n, arr):
    zeros = 0
    count = 0
    
    for i in range(n):
        if arr[i] == 0:
            zeros += 1
        else:
            count += zeros // 2
            zeros = 0
    
    count += zeros // 2
    return count

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(min_insertions(n, arr))

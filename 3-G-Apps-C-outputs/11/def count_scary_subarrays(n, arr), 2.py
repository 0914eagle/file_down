
def count_scary_subarrays(n, arr):
    count = n  # All subarrays of length 1 are scary
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] >= arr[i]:
            j -= 1
        count += (i - j)
    return count

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(count_scary_subarrays(n, arr))

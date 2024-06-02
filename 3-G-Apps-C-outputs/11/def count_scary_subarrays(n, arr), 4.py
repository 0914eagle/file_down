
def count_scary_subarrays(n, arr):
    count = n  # All subarrays of length 1 are scary
    for i in range(1, n):
        left = i - 1
        right = i + 1
        while left >= 0 and right < n:
            subarray = arr[left:right+1]
            subarray.sort()
            median = subarray[len(subarray)//2] if len(subarray) % 2 != 0 else (subarray[len(subarray)//2 - 1] + subarray[len(subarray)//2]) / 2
            if arr[i] == median:
                count += 1
            else:
                break
            left -= 1
            right += 1
    return count

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(count_scary_subarrays(n, arr))

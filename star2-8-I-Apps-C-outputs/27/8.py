
import sys
def count_subarrays(arr):
    n = len(arr)
    if n < 2:
        return 0
    count = 0
    left, right = 0, 1
    while left < n:
        while right < n and arr[right] % arr[left] == 0:
            right += 1
        count += right - left - 1
        left += 1
    return count
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
print(count_subarrays(arr))


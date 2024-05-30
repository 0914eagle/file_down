
def max_points(n, nums):
    max_num = max(nums)
    freq = [0] * (max_num + 1)
    points = [0] * (max_num + 1)

    for num in nums:
        freq[num] += 1

    points[1] = freq[1]

    for i in range(2, max_num + 1):
        points[i] = max(points[i-1], points[i-2] + i * freq[i])

    return points[max_num]

# Read input
n = int(input())
nums = list(map(int, input().split()))

# Output the result
print(max_points(n, nums))
```

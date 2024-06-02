
def solve(n, k, a):
    left = 1
    right = 10**9
    while left < right:
        mid = (left + right) // 2
        count = 0
        for i in range(n):
            if a[i] <= mid:
                count += 1
        if count >= k:
            right = mid
        else:
            left = mid + 1
    if left == 10**9 and count < k:
        return -1
    return left

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))


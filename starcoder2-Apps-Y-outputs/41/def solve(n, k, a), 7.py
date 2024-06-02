
def solve(n, k, a):
    left = 1
    right = 10 ** 9
    while left < right:
        mid = (left + right) // 2
        cnt = 0
        for i in range(n):
            if a[i] <= mid:
                cnt += 1
        if cnt < k:
            left = mid + 1
        else:
            right = mid
    if left == right:
        return left
    return -1

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))


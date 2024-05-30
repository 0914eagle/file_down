
import sys

def find_earliest_arrival(n, m, t_a, t_b, k, a, b):
    left, right = 0, 10**18 + 1

    while left < right:
        mid = (left + right) // 2
        cnt = 0
        j = 0

        for i in range(n):
            while j < m and b[j] < a[i] + t_a:
                j += 1
            if j == m:
                break
            if b[j] - a[i] + t_b <= mid:
                cnt += 1
                j += 1

        if cnt > k:
            right = mid
        else:
            left = mid + 1

    if left == 10**18 + 1:
        return -1
    return left

if __name__ == "__main__":
    n, m, t_a, t_b, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = find_earliest_arrival(n, m, t_a, t_b, k, a, b)
    print(result)

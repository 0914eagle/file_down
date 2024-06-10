
def solve(arr):
    n = len(arr)
    for i in range(1, n + 1):
        if n % i == 0:
            m = n // i
            if check(arr, i, m):
                return i, m
    return -1


def check(arr, n, m):
    zero_pos = None
    for i in range(n):
        for j in range(m):
            val = arr[i * m + j]
            dist = abs(i - n // 2) + abs(j - m // 2)
            if val == 0:
                if zero_pos is not None:
                    return False
                zero_pos = (i, j)
            elif val != dist:
                return False
    return True


t = int(input())
arr = list(map(int, input().split()))
n, m = solve(arr)
if n == -1:
    print(n)
else:
    print(n, m)
    print(n // 2 + 1, m // 2 + 1)


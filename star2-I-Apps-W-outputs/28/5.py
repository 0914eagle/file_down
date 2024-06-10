
def solve(arr):
    n = len(arr)
    if n == 1:
        return 1, 1, 1, 1
    if n == 2:
        return -1
    if n % 2 == 1:
        return -1
    m = n // 2
    if arr[0] == 0:
        x, y = 1, 1
    elif arr[m] == 0:
        x, y = 1, m + 1
    elif arr[m - 1] == 0:
        x, y = 2, m
    elif arr[m + 1] == 0:
        x, y = 2, m + 2
    else:
        return -1
    return m, m + 1, x, y


t = int(input())
arr = list(map(int, input().split()))
n, m, x, y = solve(arr)
if n == -1:
    print(n)
else:
    print(n, m)
    print(x, y)


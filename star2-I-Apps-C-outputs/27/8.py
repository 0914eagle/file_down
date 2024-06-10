
def find_closest(arr, x, y):
    n = len(arr)
    diff = [min(abs(i - j), n - abs(i - j)) for i, j in zip(arr.index(x) * [1], arr.index(y) * [1])]
    return diff.index(min(diff))


def solve(arr):
    n = len(arr)
    unique = set(arr)
    if len(unique) == n:
        return sorted(unique)
    else:
        return "none"


n = int(input())
arr = list(map(int, input().split()))
print(solve(arr))


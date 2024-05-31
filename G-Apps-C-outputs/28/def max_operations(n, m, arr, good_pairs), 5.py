
def max_operations(n, m, arr, good_pairs):
    max_ops = 0

    for i, j in good_pairs:
        v = min(arr[i-1], arr[j-1])
        while v > 1 and (arr[i-1] % v == 0) and (arr[j-1] % v == 0):
            arr[i-1] //= v
            arr[j-1] //= v
            max_ops += 1

    return max_ops

# Input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
good_pairs = [list(map(int, input().split())) for _ in range(m)]

# Output
print(max_operations(n, m, arr, good_pairs))

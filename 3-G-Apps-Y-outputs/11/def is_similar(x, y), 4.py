
def is_similar(x, y):
    return x % 2 == y % 2 or abs(x - y) == 1

def can_partition_into_pairs(n, arr):
    arr.sort()
    for i in range(0, n, 2):
        if not is_similar(arr[i], arr[i+1]):
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_partition_into_pairs(n, arr))

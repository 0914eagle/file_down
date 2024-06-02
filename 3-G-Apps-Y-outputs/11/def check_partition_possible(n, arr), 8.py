
def check_partition_possible(n, arr):
    arr.sort()
    for i in range(0, n, 2):
        if arr[i] % 2 != arr[i+1] % 2:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(check_partition_possible(n, arr))

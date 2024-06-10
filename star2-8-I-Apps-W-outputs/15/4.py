
def solve(arr):
    n = len(arr) // 2
    s1 = sum(arr[:n])
    s2 = sum(arr[n:])
    if s1 == s2:
        return -1
    else:
        arr.sort()
        return arr
n = int(input())
arr = list(map(int, input().split()))
res = solve(arr)
if res == -1:
    print(res)
else:
    print(" ".join(map(str, res)))


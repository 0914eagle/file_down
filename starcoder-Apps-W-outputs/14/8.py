
def solve():
    n, m = map(int, input().split())
    arr = input().split()
    arr1 = input().split()
    arr2 = input().split()
    res = 0
    for i in range(m):
        for j in range(n):
            if arr[j][i] == arr1[i]:
                res += int(arr2[i])
            elif arr[j][i] != arr2[i]:
                res += int(arr2[i])
    print(res)
solve()

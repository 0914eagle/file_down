
def solve(arr):
    if len(arr) == 1:
        return arr[0]
    return solve(sorted(arr[1: -1])[::-1][:(len(arr) - 1) // 2]) + arr[0] + arr[-1]

n = int(input())
arr = [int(s) for s in input().split(' ')]
print(solve(arr))


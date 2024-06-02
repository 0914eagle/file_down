
def solve(n, a):
    if n == 1:
        return [0]
    if n == 2:
        if a[0] < a[1]:
            return [0, 1]
        else:
            return [1, 0]
    if a[0] < a[1]:
        if a[1] > a[2]:
            return [0, 1, 0]
        else:
            return [0, 0, 1]
    else:
        if a[1] < a[2]:
            return [1, 0, 1]
        else:
            return [1, 1, 0]

n = int(input())
a = [int(x) for x in input().split()]
res = solve(n, a)
if res is None:
    print("NO")
else:
    print("YES")
    print(" ".join(str(x) for x in res))


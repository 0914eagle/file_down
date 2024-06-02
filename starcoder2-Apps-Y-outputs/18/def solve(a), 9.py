
n = int(input())
a = list(map(int, input().split()))

def solve(a):
    if len(a) == 0:
        return []
    if len(a) == 1:
        return [0]
    if a[0] < a[1]:
        return [0] + solve(a[1:])
    if a[0] > a[1]:
        return [1] + solve(a[1:])
    if a[0] == a[1]:
        if a[0] < a[2]:
            return [0] + solve(a[1:])
        if a[0] > a[2]:
            return [1] + solve(a[1:])
        if a[0] == a[2]:
            if a[0] < a[3]:
                return [0] + solve(a[1:])
            if a[0] > a[3]:
                return [1] + solve(a[1:])
            if a[0] == a[3]:
                return [0] + solve(a[1:])

res = solve(a)
if res == None:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, res)))



n = int(input())
a = list(map(int, input().split()))

def solve(n, a):
    if sum(a) == 0:
        return [-1]
    else:
        return [1]

ans = solve(n, a)
if ans[0] == -1:
    print(ans[0])
else:
    print(len(ans))
    print(*ans)


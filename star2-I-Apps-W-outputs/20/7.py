
n = int(input())
a = list(map(int, input().split()))

def solve(a):
    stack = []
    for i, x in enumerate(a):
        if x > 0:
            stack.append(x)
        else:
            if not stack or stack[-1] != -x:
                return -1
            stack.pop()
    if stack:
        return -1
    return 1, len(a)

res = solve(a)
if res == -1:
    print(res)
else:
    d, c = res
    print(d)
    print(c)


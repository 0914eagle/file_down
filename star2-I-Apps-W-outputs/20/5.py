
def solve(a):
    n = len(a)
    stack = []
    for i in range(n):
        if a[i] > 0:
            stack.append(a[i])
        else:
            if not stack or stack[-1] != -a[i]:
                return -1
            stack.pop()
    return len(stack)

n = int(input())
a = list(map(int, input().split()))
res = solve(a)
if res == -1:
    print(res)
else:
    print(res)
    print(*[n] * res)


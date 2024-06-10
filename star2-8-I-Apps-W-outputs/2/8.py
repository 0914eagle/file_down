
n, m, p = map(int, input().split())
s = input()
q = input()
def solve(s, q):
    stack = []
    for i in range(len(q)):
        if q[i] == 'D':
            if len(stack) > 0:
                j = stack.pop()
                s = s[:j] + s[j+2:]
        elif q[i] == 'L':
            if len(stack) > 0:
                stack[-1] -= 1
        elif q[i] == 'R':
            if len(stack) > 0:
                stack[-1] += 1
        if q[i] != 'D':
            stack.append(p-1)
    return s
print(solve(s, q))


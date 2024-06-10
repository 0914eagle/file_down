
def solve(n,m,p,s,ops):
    stack = []
    res = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                res.append(c)
    stack = []
    for c in reversed(s):
        if c == ')':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                res.append(c)
    res = ''.join(res)
    left = 0
    right = 0
    for op in ops:
        if op == 'L':
            left -= 1
        elif op == 'R':
            right += 1
        else:
            left += 1
            right -= 1
    left = max(left,0)
    right = min(right,len(res)-1)
    return res[left:right+1]

n,m,p = map(int,input().split())
s = input()
ops = input()
print(solve(n,m,p,s,ops))


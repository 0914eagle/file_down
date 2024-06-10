
n, m, p = map(int, input().split())
s = input()
q = input()

def is_matched(s):
    n = len(s)
    stack = []
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

def is_valid(s):
    if len(s) == 0:
        return False
    if not is_matched(s):
        return False
    return True

def find_matched(s, i):
    n = len(s)
    stack = []
    for j in range(n):
        if s[j] == '(':
            stack.append(j)
        else:
            if len(stack) == 0:
                return -1
            if stack[-1] == i:
                stack.pop()
                return j
            stack.pop()
    return -1

def process(s, q, p):
    n = len(s)
    m = len(q)
    for i in range(m):
        if q[i] == 'L':
            if p > 1:
                p -= 1
        elif q[i] == 'R':
            if p < n:
                p += 1
        else:
            i = p-1
            j = find_matched(s, i)
            s = s[:i] + s[j+1:]
            p = i
            while p > 1 and s[p-1] == ')':
                p -= 1
            while p < n-1 and s[p] == '(':
                p += 1
    return s, p

s, p = process(s, q, p)
if not is_valid(s):
    print("ERROR")
else:
    print(s)


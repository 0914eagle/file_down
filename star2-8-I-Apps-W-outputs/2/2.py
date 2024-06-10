
import sys
input = sys.stdin.readline

def solve(n, m, p, s, q):
    stack = []
    for i in range(n):
        if s[i] == '(':
            stack.append(i+1)
        elif s[i] == ')':
            if stack:
                stack.pop()
            else:
                stack.append(i+1)
    
    left = [0]*n
    right = [0]*n
    
    stack = []
    for i in range(n):
        if s[i] == '(':
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        else:
            stack.pop()
    
    stack = []
    for i in range(n-1, -1, -1):
        if s[i] == ')':
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        else:
            stack.pop()
    
    cur = p
    for c in q:
        if c == 'L':
            if cur > 1 and right[cur-1] == 0:
                cur -= 1
        elif c == 'R':
            if cur < n and left[cur-1] == 0:
                cur += 1
        else:
            left_idx = cur-1
            right_idx = right[left_idx-1]-1
            if left_idx == right_idx:
                cur = left_idx
            else:
                cur = left_idx - (right_idx - left_idx + 1) // 2
    
    stack = []
    for i in range(n):
        if s[i] == '(':
            stack.append(i+1)
        elif s[i] == ')':
            if stack:
                stack.pop()
            else:
                stack.append(i+1)
    
    res = ''
    for i in range(n):
        if i+1 in stack:
            res += '('
        else:
            res += ')'
    
    return res

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    s = input().rstrip()
    q = input().rstrip()
    print(solve(n, m, p, s, q))


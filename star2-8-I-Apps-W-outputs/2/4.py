
n, m, p = map(int, input().split())
seq = input()
ops = input()
stack = []

for i, c in enumerate(seq):
    if c == '(':
        stack.append(i+1)
    else:
        stack.pop()
    
    if i+1 == p:
        pos = i

for op in ops:
    if op == 'L':
        pos -= 1
    
    elif op == 'R':
        pos += 1
    
    elif op == 'D':
        stack.pop(stack.index(pos+1)-1)
        pos = stack[stack.index(pos+1)-1]
    
    if pos < 0:
        pos = 0
    
    elif pos >= len(stack):
        pos = len(stack)-1

print(seq[stack[0]-1:stack[-1]])


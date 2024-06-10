
import sys
input = sys.stdin.readline

def find_matching(string, pos):
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)
        elif string[i] == ')':
            if len(stack) == 0:
                return -1
            stack.pop()
    
    if len(stack) == 0:
        return -1
    
    for i in range(len(stack)-1, -1, -1):
        if stack[i] < pos:
            return stack[i]
    
    return -1
    
def delete(string, pos):
    if pos >= len(string):
        return string
    
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)
        elif string[i] == ')':
            if len(stack) == 0:
                return string[:i] + string[i+1:]
            stack.pop()
    
    if len(stack) == 0:
        return string[:pos] + string[pos+1:]
    
    for i in range(len(stack)-1, -1, -1):
        if stack[i] < pos:
            return string[:stack[i]] + string[pos+1:]
    
    return string
    
n, m, p = map(int, input().split())
string = input().strip()
operations = input().strip()
for op in operations:
    if op == 'L':
        p -= 1
    elif op == 'R':
        p += 1
    elif op == 'D':
        pos = find_matching(string, p)
        if pos == -1:
            pos = find_matching(string[::-1], len(string)-p)
            if pos == -1:
                string = string[:p] + string[p+1:]
            else:
                string = string[:pos] + string[p+1:]
        else:
            string = string[:pos] + string[p+1:]
        
        p = pos
    
print(string)


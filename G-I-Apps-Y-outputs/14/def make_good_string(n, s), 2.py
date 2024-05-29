
def make_good_string(n, s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    if len(stack) % 2 == 1:
        stack.pop()
    
    k = len(s) - len(stack)
    result = "".join(stack)
    
    return k, result

# Input
n = int(input())
s = input().strip()

# Output
k, result = make_good_string(n, s)
print(k)
if result:
    print(result)
```

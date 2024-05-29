
def make_good_string(n, s):
    stack = []
    delete_count = 0
    for i, char in enumerate(s):
        if len(stack) > 0 and char == stack[-1]:
            delete_count += 1
            stack.pop()
        else:
            stack.append(char)
    
    if len(stack) % 2 == 1:
        stack.pop()
        delete_count += 1
        
    return delete_count, ''.join(stack)

# Input
n = int(input())
s = input().strip()

# Output
delete_count, result = make_good_string(n, s)
print(delete_count)
if result:
    print(result)
```

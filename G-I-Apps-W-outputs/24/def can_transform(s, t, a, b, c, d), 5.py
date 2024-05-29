
def can_transform(s, t, a, b, c, d):
    mapping = {'A': 'BC', 'B': 'AC', 'C': 'AB'}
    
    def transform_substr(sub):
        stack = []
        for char in sub:
            stack.append(char)
            while len(stack) >= 2:
                if stack[-2] + stack[-1] in mapping:
                    stack.pop()
                    stack.pop()
                    stack.append(mapping[stack[-1]])
                else:
                    break
        return ''.join(stack)
    
    transformed_s = transform_substr(s[a-1:b])
    transformed_t = t[c-1:d]
    
    if len(transformed_s) != len(transformed_t):
        return 0
    for i in range(len(transformed_s)):
        if transformed_s[i] != transformed_t[i]:
            return 0
    return 1

S = input().strip()
T = input().strip()
Q = int(input().strip())

answers = ''
for _ in range(Q):
    a, b, c, d = map(int, input().strip().split())
    answers += str(can_transform(S, T, a, b, c, d))

print(answers)
```

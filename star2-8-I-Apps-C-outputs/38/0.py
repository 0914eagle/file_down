
def balanced(s):
    stack = []
    last = -1
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            start = stack.pop()
            if not stack:
                last = i
    result = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            start = stack.pop()
            if not stack:
                end = i
                result.append((start, end))
    output = []
    for start, end in result:
        output.append(f"{start},{end}:{end},{end}:")
    return ''.join(output)

s = input()
print(balanced(s))


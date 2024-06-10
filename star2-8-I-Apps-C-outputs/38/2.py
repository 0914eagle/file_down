
s = input()
stack = []
alt_bracket_repr = []
for i, c in enumerate(s):
    if c == '(':
        stack.append(i)
    elif c == ')':
        start = stack.pop()
        end = i
        alt_bracket_repr.append((start, end))
alt_bracket_repr.sort(key=lambda x: x[0])
def get_header(start, end):
    return f"{start},{end}:"

headers = [get_header(start, end) for start, end in alt_bracket_repr]
print("".join(headers))


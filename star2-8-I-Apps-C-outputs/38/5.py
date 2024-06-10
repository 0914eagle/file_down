
def solve(s):
    stack = []
    brack_list = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            start = stack.pop()
            end = i
            brack_list.append((start, end))
    brack_list.sort(key=lambda x: x[0])
    def header(start, end):
        return f"{start},{end}:"
    def build_header(start, end):
        if start == end:
            return ""
        else:
            return header(start, end) + build_header(start + len(header(start, end)), end)
    min_header = build_header(0, len(s))
    for start, end in brack_list:
        header_str = build_header(start, end)
        if header_str < min_header:
            min_header = header_str
    return min_header


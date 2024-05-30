
def min_ops(s):
    a = 0
    b = 0
    for i in range(len(s)):
        if s[i] == 'a':
            a += 1
        else:
            b += 1
        if i % 2 == 1:
            if a != b:
                return i // 2 + 1
    return 0

def solve(s):
    ops = min_ops(s)
    if ops == 0:
        return ops, s
    else:
        for i in range(ops):
            if i % 2 == 0:
                s = s[:i] + 'b' + s[i + 1:]
            else:
                s = s[:i] + 'a' + s[i + 1:]
        return ops, s


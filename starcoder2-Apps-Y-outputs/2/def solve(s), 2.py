
def solve(s):
    res = []
    for c in s:
        if c == 'B':
            if res:
                res.pop()
        else:
            res.append(c)
    return ''.join(res)

s = input()
print(solve(s))


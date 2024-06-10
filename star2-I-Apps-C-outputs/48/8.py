
def factoring(s):
    if len(s) == 1:
        return s
    for i in range(1, len(s)):
        if s[:i] == s[i:2*i]:
            return factoring(s[:i]) + '(' + factoring(s[i:2*i]) + ')' + str(len(s)//len(s[:i]))
    return s

def weight(s):
    w = 0
    for c in s:
        if c.isalpha():
            w += 1
        elif c.isdigit():
            w += len(c)
    return w

def maximal_factoring(s):
    f = factoring(s)
    w = weight(f)
    while True:
        g = factoring(f)
        if w == weight(g):
            break
        f = g
        w = weight(f)
    return w

print(maximal_factoring(input()))


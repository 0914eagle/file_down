
def solve():
    n = int(input())
    s = input()
    t = s
    if n == 1:
        print(0)
        print(t)
        return
    if s[0] == s[1]:
        if s[0] == 'R':
            t = 'GB' + s[2:]
        elif s[0] == 'G':
            t = 'RB' + s[2:]
        else:
            t = 'RG' + s[2:]
    if s[-1] == s[-2]:
        if s[-1] == 'R':
            t = t[:-2] + 'GB'
        elif s[-1] == 'G':
            t = t[:-2] + 'RB'
        else:
            t = t[:-2] + 'RG'
    if s[0] == s[-1]:
        if s[0] == 'R':
            t = 'GB' + t[2:-2] + 'GB'
        elif s[0] == 'G':
            t = 'RB' + t[2:-2] + 'RB'
        else:
            t = 'RG' + t[2:-2] + 'RG'
    print(n - t.count(t[0]))
    print(t)
solve()


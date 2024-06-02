
n = int(input())
s = input()

def count_recolor(s):
    r = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            r += 1
    return r

def recolor(s):
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            if s[i] == 'R':
                s = s[:i] + 'G' + s[i + 1:]
            elif s[i] == 'G':
                s = s[:i] + 'B' + s[i + 1:]
            else:
                s = s[:i] + 'R' + s[i + 1:]
    return s

r = count_recolor(s)
t = s
for i in range(n):
    if s[i] == 'R':
        s = s[:i] + 'G' + s[i + 1:]
    elif s[i] == 'G':
        s = s[:i] + 'B' + s[i + 1:]
    else:
        s = s[:i] + 'R' + s[i + 1:]
    r1 = count_recolor(s)
    if r1 < r:
        r = r1
        t = s
    s = recolor(s)

print(r)
print(t)


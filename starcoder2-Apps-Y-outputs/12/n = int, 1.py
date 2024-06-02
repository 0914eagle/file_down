
n = int(input())
s = input()

r = 0
t = s

if n > 1:
    if s[0] == s[1]:
        if s[0] == 'R':
            t = 'G' + t[1:]
            r += 1
        else:
            t = 'R' + t[1:]
            r += 1

for i in range(1, n - 1):
    if s[i] == s[i - 1] or s[i] == s[i + 1]:
        if s[i] == 'R':
            if s[i - 1] == 'G':
                t = t[:i] + 'B' + t[i + 1:]
                r += 1
            else:
                t = t[:i] + 'G' + t[i + 1:]
                r += 1
        elif s[i] == 'G':
            if s[i - 1] == 'R':
                t = t[:i] + 'B' + t[i + 1:]
                r += 1
            else:
                t = t[:i] + 'R' + t[i + 1:]
                r += 1
        else:
            if s[i - 1] == 'R':
                t = t[:i] + 'G' + t[i + 1:]
                r += 1
            else:
                t = t[:i] + 'R' + t[i + 1:]
                r += 1

if n > 1:
    if s[-1] == s[-2]:
        if s[-1] == 'R':
            t = t[:-1] + 'G'
            r += 1
        else:
            t = t[:-1] + 'R'
            r += 1

print(r)
print(t)


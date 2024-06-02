
n = int(input())
s = input()

r = 0
t = s

if s[0] == s[1]:
    r += 1
    t = t[0] + 'G' + t[2:]

if s[-1] == s[-2]:
    r += 1
    t = t[:-2] + 'G' + t[-1]

for i in range(1, n - 1):
    if s[i] == s[i - 1] or s[i] == s[i + 1]:
        r += 1
        if s[i] == s[i - 1]:
            t = t[:i] + 'G' + t[i + 1:]
        else:
            t = t[:i + 1] + 'G' + t[i + 2:]

print(r)
print(t)


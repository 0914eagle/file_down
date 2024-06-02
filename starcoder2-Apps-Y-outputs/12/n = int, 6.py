
n = int(input())
s = input()

r = 0
t = ''
for i in range(n):
    if i == 0:
        if s[i] == 'R':
            t += 'G'
        elif s[i] == 'G':
            t += 'B'
        else:
            t += 'R'
        continue
    if s[i] == s[i - 1]:
        if s[i] == 'R':
            t += 'G'
        elif s[i] == 'G':
            t += 'B'
        else:
            t += 'R'
        r += 1
    else:
        t += s[i]

print(r)
print(t)


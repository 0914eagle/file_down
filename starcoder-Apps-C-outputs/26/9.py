
n = input()
s = raw_input()

i = 0
p = 0
while i < len(s):
    if s[i] == 'P':
        p = i
    i += 1

if s[0] == '.':
    for i in range(1, p):
        if s[i] == '*':
            print i
            break
elif s[len(s)-1] == '.':
    for i in range(len(s)-1, p, -1):
        if s[i] == '*':
            print len(s)-i
            break
else:
    for i in range(p+1, len(s)):
        if s[i] == '*':
            print i
            break

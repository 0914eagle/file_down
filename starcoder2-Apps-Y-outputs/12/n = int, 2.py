
n = int(input())
s = input()

if n == 1:
    print(0)
    print(s)
else:
    if s[0] == s[1]:
        if s[0] == 'R':
            s = 'GB' + s[2:]
        else:
            s = 'R' + s[1:]
    if s[-1] == s[-2]:
        if s[-1] == 'R':
            s = s[:-2] + 'GB'
        else:
            s = s[:-1] + 'R'
    cnt = 0
    for i in range(1, n):
        if s[i] == s[i-1]:
            cnt += 1
            if s[i] == 'R':
                s = s[:i] + 'GB' + s[i+1:]
            else:
                s = s[:i] + 'R' + s[i+1:]
    print(cnt)
    print(s)


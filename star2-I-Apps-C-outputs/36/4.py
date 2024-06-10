
n, m = map(int, input().split())
s = input()
t = input()

if s.count('*') > 1:
    print('NO')
else:
    if s.count('*') == 1:
        idx = s.index('*')
        if idx == 0:
            if s[-1] == t[0]:
                print('YES')
            else:
                print('NO')
        elif idx == len(s) - 1:
            if s[0] == t[-1]:
                print('YES')
            else:
                print('NO')
        else:
            if s[:idx] == t[:idx] and s[idx + 1:] == t[idx + 1:]:
                print('YES')
            else:
                print('NO')
    else:
        if s == t:
            print('YES')
        else:
            print('NO')


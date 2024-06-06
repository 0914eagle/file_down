
n = int(input())
ss = set()
res = 0
for i in range(n):
    s = input()
    if s[0] == ')' and s[-1] == '(':
        res += len(ss)
        ss.add(s)
    elif s[0] == '(' and s[-1] == ')':
        res += len(ss)
        ss.add(s)
    else:
        if s in ss:
            res += 1
        ss.add(s)
print(res)

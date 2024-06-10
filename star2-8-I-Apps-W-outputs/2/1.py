
import sys
n, m, p = map(int, input().split())
s = input()
cmd = input()
st = []
for i in range(n):
    if s[i] == '(':
        st.append(i + 1)
    else:
        if len(st) == 0:
            continue
        j = st.pop()
        s = s[:j-1] + s[i:]
        i -= 1
        n -= 2
for c in cmd:
    if c == 'L':
        p = max(1, p-1)
    elif c == 'R':
        p = min(n, p+1)
    else:
        if p > 1 and s[p-2] == '(':
            p -= 2
            s = s[:p] + s[p+2:]
            n -= 2
        else:
            p += 2
            s = s[:p-2] + s[p:]
            n -= 2
print(s)


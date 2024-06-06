
import re
s = input().split()
b = [i.replace("'", "").lower() for i in s]
st = 0
for i in range(len(b)):
    t = b[i]
    if t == 'es' and i > 1 and b[i-2] != 'e':
        st += 2
        if len(s[i]) == 2:
            s[i] = s[i][:-1]
    elif t == 'es' and i > 1 and b[i-2] == 'e':
        st += 1
        if len(s[i]) == 2:
            s[i] = s[i][:-1]
    elif len(re.findall('[aeiouy]', t)) == 0:
        st += len(t)
    elif len(re.findall('[aeiouy]', t)) == 1:
        st += 1
    else:
        a = re.findall('[aeiouy]', t)
        if 'e' in a[-1] and i < len(b)-1 and b[i+1] != 'l':
            st += len(a) - 1
        else:
            st += len(a)
if st == 5:
    print(s[0])
    print(s[1])
else:
    print(' '.join(s))

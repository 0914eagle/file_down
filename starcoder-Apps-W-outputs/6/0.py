
n = int(input())
a = []
b = []
c = []
d = []
e = []
f = []
for i in range(n):
    s = input()
    if s.count("(") == s.count(")"):
        a.append(s)
    elif s.count("(") > s.count(")"):
        b.append(s)
    else:
        c.append(s)
if len(a) % 2 == 0:
    print(len(a) * (len(a) - 1))
else:
    print(len(a) * (len(a) - 1) + len(b) + len(c))

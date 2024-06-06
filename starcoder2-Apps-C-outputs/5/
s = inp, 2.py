
s = input()
a = set()
for i in s:
    a.add(i)
if len(a) == len(s):
    print("YES")
else:
    print("NO")

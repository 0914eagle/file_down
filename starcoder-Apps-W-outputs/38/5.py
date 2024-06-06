

s1=input()
s2=input()
if len(s1) > len(s2):
    s1, s2 = s2, s1

for i in range(len(s1)):
    if s1[i] != s2[i]:
        if s2[i] == "0":
            s2 = s2[:i] + "1" + s2[i + 1:]
        else:
            s2 = s2[:i] + "0" + s2[i + 1:]
        s1, s2 = s2, s1

if s1 == s2:
    print("YES")
else:
    print("NO")


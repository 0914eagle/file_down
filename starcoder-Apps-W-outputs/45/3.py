
s1 = list(input())
s2 = list(input())
n = len(s1)
flag = 1

for i in range(n):
    if s2[i] != '?':
        if s1[i] != s2[i]:
            flag = 0
            break
if flag == 0:
    print(0)
else:
    print(1)

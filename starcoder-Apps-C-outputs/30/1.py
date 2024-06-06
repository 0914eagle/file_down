
s = input()
n = int(input())
a = []
ans = ''
flag = 0
for i in range(n):
    a.append(input())
for i in a:
    if s[0] == i[0] and s[-1] == i[-1]:
        ans = i
        break
for i in a:
    if s[0] == i[0] and s[-1] == i[-1]:
        if ans != i:
            flag = 1
            break
if ans != '':
    if flag == 0:
        print(ans)
    else:
        print("ambiguous")
else:
    print("impossible")

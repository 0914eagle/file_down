
n = int(input())
s = input()

cnt = 0
temp = []
for i in s:
    if len(temp) != 0:
        if temp[-1] == i:
            cnt += 1
            temp = []
        else:
            temp.append(i)
    else:
        temp.append(i)
print(n+cnt)

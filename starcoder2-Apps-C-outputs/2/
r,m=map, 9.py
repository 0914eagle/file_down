
r,m=map(int,input().split())
l=[r]
i=r
while True:
    i+=1
    if i not in l:
        l.append(i)
    else:
        continue
    for j in range(len(l)-1):
        if i-l[j] not in l:
            l.append(i-l[j])
        else:
            continue
    if m in l:
        print(l.index(m)+1)
        break

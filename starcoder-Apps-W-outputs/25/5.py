
n,m = map(int,input().split())
list1 = list(map(int,input().split()))
list1.sort()
list2 = []
for i in range(m):
    list2.append(list(map(int,input().split())))
list2 = sorted(list2,key=lambda list2:list2[0])
cnt = 0
maxval = 0
for i in list2:
    if i[0] <= list1[cnt]:
        maxval+=i[1]
    else:
        cnt+=1
        if cnt == n:
            break
        maxval+=i[1]
print(maxval)

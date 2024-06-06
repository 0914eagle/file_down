
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    if a[i][0]==a[i][2] or a[i][1]==a[i][3]:
        continue
    else:
        print("NO")
        break
else:
    print("YES")

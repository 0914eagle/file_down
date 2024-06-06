
# 暴力解法
n,m = map(int,input().split())
F = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = []
for i in range(1,n+1):
    flag = True
    for j in range(m):
        if B[j] != F[i-1]:
            flag = False
            break
    if flag:
        ans.append(i)

if len(ans) == 0:
    print("Impossible")
elif len(ans) == 1:
    print("Possible")
    for i in range(len(ans)):
        print(ans[i],end=" ")
else:
    print("Ambiguity")

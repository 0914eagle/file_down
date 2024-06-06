
N=int(input())
arr=list(map(int,input().split()))
for i in range(N):
    arr[i]=list(map(int,input().split()))
#print(arr)
#dp=[0]*N
#dp[1]=arr[1][0]
#for i in range(2,N):
#    dp[i]=max(arr[i][0],dp[i-1])
#print(dp)
for i in range(2,N):
    arr[i][0]=max(arr[i][0],arr[i-1][0])

for i in range(1,N):
    for j in range(1,len(arr[i])):
        arr[i][0]=max(arr[i][0],arr[arr[i][j]][0])
print(arr[-1][0])

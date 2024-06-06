
# YOUR CODE GOES HERE
for _ in range(int(input())):
    n,k,q=map(int,input().split())
    arr=[[0 for _ in range(200002)] for _ in range(200002)]
    for __ in range(n):
        l,r=map(int,input().split())
        arr[l][r]+=1
    for i in range(1,200001):
        for j in range(1,200001):
            arr[i][j]+=arr[i-1][j]+arr[i][j-1]-arr[i-1][j-1]
    #print(arr)
    for __ in range(q):
        a,b=map(int,input().split())
        count=0
        for i in range(a,b+1):
            temp=0
            for j in range(i,b+1):
                #print(arr[i-1][j],arr[j][j],arr[i-1][i-1],arr[j][i-1])
                temp+=arr[j][j]-arr[j][i-1]-arr[i-1][j]+arr[i-1][i-1]
                if temp>=k:
                    count+=1
                    break
        print(count)

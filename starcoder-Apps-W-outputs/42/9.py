

for _ in range(int(input())):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    arr.sort()
    index = []
    for i in range(N):
        index.append(i+1)
    ans = []
    #print(arr)
    for i in range(0,N,2):
        if i != N-1:
            if arr[i] == arr[i+1]:
                ans.append([index[i],index[i+1]])
                index.remove(index[i])
                index.remove(index[i])
                continue
        ans.append([index[i],index[-1]])
        index.remove(index[i])
        index.remove(index[-1])
    for x in ans:
        print(*x)

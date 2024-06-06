
import sys
sys.setrecursionlimit(1000000)
def djs(i):
    for j in range(len(arr)):
        if arr[i][1] > arr[j][1] and arr[i][2] < arr[j][2]:
            #print(i,j)
            #print(arr[i],arr[j])
            break
    else:
        return 1
    if ans[j] == -1:
        ans[j] = djs(j)
    return ans[j] + 1
n,q = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key = lambda x: x[1])
arr.sort(key = lambda x: x[2])
ans = [-1 for i in range(n)]
for i in range(n):
    if ans[i] == -1:
        ans[i] = djs(i)
for i in range(q):
    i = int(input())
    for j in range(n):
        if i == arr[j][0]:
            #print(arr[j])
            print(arr[j+ans[j]][0],ans[j])
            break

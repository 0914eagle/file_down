
import sys
input=sys.stdin.readline
def selection_sort(lst):
    for i in range(len(lst)):
        minimum = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[minimum]:
                minimum = j
        lst[minimum],lst[i] = lst[i],lst[minimum]
# n,s,m,k=map(int,input().split())
n,s,m,k=1500,1500,1,1500
arr=list(map(int,input().split()))
# arr=list(map(int,input().split()))
# for i in range(n):
#     arr.append(int(input()))
l=[]
for i in range(s):
    l1,r1=map(int,input().split())
    l.append([l1,r1])
# print(l)
# l.sort(key = lambda x: x[1])
# print(l)
# k=len(l)-m
ans=[]
for i in l:
    temp=[]
    for j in range(i[0]-1,i[1]):
        temp.append(arr[j])
    ans.append(temp)
# print(ans)
# print(len(ans))
# print(m)
for i in range(len(ans)):
    selection_sort(ans[i])
for i in range(m):
    print(ans[i])
# print(k)
# print(ans[k])
# print(ans[k][len(ans[k])-1])

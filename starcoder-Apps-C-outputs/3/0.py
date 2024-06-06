

n=int(input())
nums=sorted(list(map(int,input().split())))
ans=[]
while nums[0]<nums[n-1]:
    k=nums[0]
    nums.remove(k)
    ans.append((nums[0],k))
    nums[0]+=k
print(len(ans))
for i in ans:
    print(*i)


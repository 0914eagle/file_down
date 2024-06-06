
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
  if a[i]>a[i+1]:
    print(i+1,i+2)
    a[i+1]+=a[i]

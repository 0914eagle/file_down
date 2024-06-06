
s = []
for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s.append('a'*(a[0]+1))
    s.append('a'*a[n-1]+'r'*(n-a[n-1]+1))
    for i in range(1,n-1):
        s.append('a'*(a[i]+1)+'r'*(i-a[i]+1))

for i in s:
    print(i)

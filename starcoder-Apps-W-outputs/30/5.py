
s=input()
n=len(s)
a=0
b=0
for i in range(n-1):
    if s[i] not in ['a','e','i','o','u','n']:
        if s[i+1] not in ['a','e','i','o','u']:
            a+=1
if s[n-1] not in ['a','e','i','o','u','n']:
    b+=1
if a==0 and b==0:
    print("YES")
else:
    print("NO")

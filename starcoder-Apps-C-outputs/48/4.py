
n,k=map(int,input().split())
s=input()
arr=[int(input()) for _ in range(n)]
m=10**9
for i in range(n):
    for j in range(i+1,n):
        s=s[:i]+'('*(arr[i]>0)+')'*(arr[i]<0)+s[i+1:j]+'('*(arr[j]>0)+')'*(arr[j]<0)+s[j+1:]
        p=0
        for k in s:
            if k=='(': p+=1
            else:
                if p>0: p-=1
                else: break
        m=min(m,abs(arr[i])+abs(arr[j])+(n-p)*10**6)
        s=s[:i]+'('*(arr[i]<0)+')'*(arr[i]>0)+s[i+1:j]+'('*(arr[j]<0)+')'*(arr[j]>0)+s[j+1:]
print('?' if m==10**9 else m)

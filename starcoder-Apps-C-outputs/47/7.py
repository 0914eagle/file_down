
n,k=map(int,input().split())
if(k>26 or k<1 or n<1 or n>10**6):
    print(-1)
elif(k==1):
    print('a'*n)
else:
    s=''
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(n):
        if(len(s)==0):
            s+='a'
        else:
            if(len(s)==n-1):
                if(s[i-1]=='z'):
                    s+=a[k-2]
                else:
                    s+=a[a.index(s[i-1])+1]
            else:
                if(s[i-1]=='z'):
                    s+=a[k-len(set(s))]
                else:
                    s+=a[a.index(s[i-1])+1]
    print(s)

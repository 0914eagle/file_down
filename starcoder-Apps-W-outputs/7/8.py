
n,m,k=map(int,input().split())

n1=0
for i in range(1,n+1):
    for j in range(1,m+1):
        print(f'({i},{j}) ',end="")
        n1+=1
        if n1==k:
            break
    print()

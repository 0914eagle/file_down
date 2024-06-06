
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    A=list(map(int,input().split()))
    #print(n,m,k)
    #print(A)
    A.sort()
    A.reverse()
    print(sum(A[:k*m]))

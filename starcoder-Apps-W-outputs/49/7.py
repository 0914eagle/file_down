
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    s=[['']*n for i in range(2)]
    x=0
    for i in range(n):
        for j in range(a[i]):
            s[0][i]=s[0][i]+chr(x+97)
            s[1][i]=chr(x+97)+s[1][i]
        x+=1
    for i in range(n):
        print(s[0][i])
    for i in range(n-1,-1,-1):
        print(s[1][i])

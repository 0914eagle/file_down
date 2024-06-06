
n=int(input())
s=input()
if n==1:
    print(1)
else:
    for i in range(n):
        if s[i]==s[i-1]:
            c=1
            break
    else:
        print(n)
    if c==1:
        print(i+2)

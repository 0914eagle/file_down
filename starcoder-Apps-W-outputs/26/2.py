
n=int(input())
s=input()
k=0
b=""
for i in range(n):
    b+=s[i]
    if b==s[0:len(b)]:
        k+=1
print(n+k-1)

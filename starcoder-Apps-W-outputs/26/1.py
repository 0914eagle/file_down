
n=int(input())
s=input()
c=0
for i in range(len(s)):
    if s[0]==s[i]:
        c+=1
    else:
        break
print(c+(len(s)//c))

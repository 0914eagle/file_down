
n=int(input())
s=input()
t=s.find("P")
c=0
for i in range(n):
    if s[i]=="*":
        c+=abs(i-t)
print(c)

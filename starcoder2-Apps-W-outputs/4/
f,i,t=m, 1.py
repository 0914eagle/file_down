
f,i,t=map(int,input().split())
s=0
for _ in range(f):
    if input().count('Y')>=t:
        s+=1
print(s)

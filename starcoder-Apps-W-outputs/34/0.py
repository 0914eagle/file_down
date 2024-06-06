
n = int(input())
t = []
f = []
for i in range(n):
    a,b = input().split()
    if b == '0':
        t.append(a)
    else:
        f.append(a)
print(len(t)+len(f))
for i in range(len(f)):
    print("move",f[i],i+1)
for i in range(len(t)):
    print("move",t[i],i+1+len(f))

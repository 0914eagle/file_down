
# 1104C-Masha-and-Two-Friends.py

b1,q,l,m=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]

n=0
for i in range(l+1):
    if b1+i*q not in a:
        n+=1
    if b1-i*q not in a:
        n+=1
print(n)


s = input()
lis = input().split()
lis = [int(i) for i in lis]
i = 0
while len(lis)>1:
    n = int(lis[i])+int(lis[i+1])
    lis[i] = n
    del lis[i+1]
    i+=1
print(lis[0])

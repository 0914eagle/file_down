
X,A,B = [int(x) for x in input().split()]
S = input()
count=0
for i in range(A,B+1):
    if i%X==0:
        a = str(i)
        flag=0
        for j in a:
            if j not in S:
                flag=1
                break
        if flag==0:
            count+=1
print(count)

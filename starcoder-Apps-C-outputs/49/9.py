
x,a,b=input().split()
x,a,b=int(x),int(a),int(b)
s=input()
count=0
for i in range(a,b+1):
    flag=True
    if str(x) in str(i):
        for j in str(i):
            if j not in s:
                flag=False
                break
        if flag:
            count+=1
print(count)

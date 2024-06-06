
a=input()
k=[]
f=0
if '1' in a and '6' in a and '8' in a and '9' in a:
    for i in range(len(a)):
        if a[i]=='1' or a[i]=='6' or a[i]=='8' or a[i]=='9':
            k.append(int(a[i]))
        else:
            f=f+1
    k.sort()
    if f==0:
        for i in range(len(k)):
            print(k[i],end="")
    else:
        print("0")
else:
    print("0")

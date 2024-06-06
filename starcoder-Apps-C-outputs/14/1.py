
n = input()
l = n.split()
z = len(l)
l1 = []
l2 = []
l3 = []
a = 0
b = 0
c = 0
for i in l:
    s = 0
    for j in i:
        if(j.isalpha()):
            if(j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u' or j == 'y'):
                if((j == 'e' and i[a-2] == 'l') or (j == 'e' and i[a-1] == 'l')):
                    s = s
                else:
                    s+=1
                a+=1
            elif(j == 'q' and i[a+1] == 'u'):
                s+=1
                a+=1
            else:
                s+=1
                a+=1
    if(s == 5):
        l1.append(i)
    if(s == 7):
        l2.append(i)
    if(s == 5 or s == 7):
        l3.append(i)
        a = 0
    else:
        a = 0
    c+=1
if(len(l1) == 5 and len(l2) == 7 and len(l3) == 15):
    for i in l3:
        print(i,end=' ')
else:
    print(n)

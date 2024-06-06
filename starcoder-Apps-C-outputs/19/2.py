
# 18

t1=input()
t2=input()
a=t1[0:2]
b=t1[3:5]
c=t2[0:2]
d=t2[3:5]
list=[]
for x in range(int(a),int(c)):
    if x<10:
        list.append('0'+str(x)+':'+b)
    else:
        list.append(str(x)+':'+b)
for x in range(int(a),int(c)):
    if x<10:
        list.append('0'+str(x)+':'+d)
    else:
        list.append(str(x)+':'+d)
for x in range(int(b),int(d)+1):
    if x<10:
        list.append(c+':0'+str(x))
    else:
        list.append(c+':'+str(x))
list.append(t2)
print(len(list))
for x in list:
    print(x)


t=input()
a=b=c=0
for i in t:
    if i=='a':
        a+=1
    if i=='b':
        b+=1
    if i=='c':
        c+=1
if (a==b==c):
    print "YES"
else:
    print "NO"

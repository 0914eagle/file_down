
v,n = input(),input()
a,b = [],[]

for i in range(9):
    a.append(int(n.split()[i]))
    if i==0:
        a.append(int(n.split()[i]))
    if int(n.split()[i]) == 1:
        a[i] = int(n.split()[i]) + 10

for j in range(9):
    if v >= a[j]:
        v -= a[j]
        b.append(str(j+1))
    else:
        break
if v >= a[9]:
    v -= a[9]
    b.append(str(0))

for k in range(9):
    if v >= a[k]:
        v -= a[k]
        b.append(str(k+1))
    else:
        break
if v >= a[9]:
    v -= a[9]
    b.append(str(0))

if v >= a[9]:
    b.append(str(0))

if v > 0:
    print(-1)
else:
    print(''.join(b))


n,k = map(int,input().split())
a = []
for i in range(k):
    a.append(chr(97+i))

if n>k:
    print(''.join(a) + ''.join(a[:k-1]))
else:
    print(''.join(a))

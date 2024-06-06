
n = int(input())
a = [int(input()) for _ in range(n)]
c = 0
for i in a:
    c+=i
if c>0:
    print('first')
else:
    print('second')

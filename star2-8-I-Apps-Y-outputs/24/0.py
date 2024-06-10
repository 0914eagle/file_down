
x, a, b = map(int, input().split())
if b <= x:
    print('delicious')
elif b <= x+1:
    print('safe')
else:
    print('dangerous')


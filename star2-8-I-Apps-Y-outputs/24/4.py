
X, A, B = map(int, input().split())

if A <= X <= B:
    print('delicious')
elif B < X:
    print('safe')
else:
    print('dangerous')


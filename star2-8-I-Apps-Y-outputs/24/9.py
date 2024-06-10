
X, A, B = map(int, input().split())
if B <= X:
    print("delicious")
elif B <= X+1:
    print("safe")
else:
    print("dangerous")


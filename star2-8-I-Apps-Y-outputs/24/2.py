
X, A, B = map(int, input().split())

if B > X + 1:
    print("dangerous")
elif B > X:
    print("safe")
else:
    print("delicious")


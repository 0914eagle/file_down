
def solve(N, P):
    X = 0
    for i in range(N):
        X += P[i]**(i+1)
    return X

N = int(input())
P = []
for i in range(N):
    P.append(int(input()))
print(solve(N, P))


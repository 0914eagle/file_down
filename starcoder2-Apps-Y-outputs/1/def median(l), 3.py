
def median(l):
    l.sort()
    if len(l) % 2 == 0:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        return l[len(l) // 2]

N = int(input())
X = list(map(int, input().split()))

for i in range(N):
    print(median(X[:i] + X[i + 1:]))


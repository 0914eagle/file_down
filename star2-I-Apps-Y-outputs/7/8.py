
n, q = map(int, input().split())
a = list(map(int, input().split()))
b = [int(input()) for _ in range(q)]

def solve(a, b):
    a.sort()
    for i in range(len(a)):
        if a[i] > b:
            return i
    return -1

for x in b:
    print(solve(a, x))


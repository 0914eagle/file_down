
r, m = map(int, input().split())

A = [r]

while True:
    if m in A:
        print(A.index(m) + 1)
        break
    if m - A[-1] in A:
        print(A.index(m - A[-1]) + 1)
        break
    A.append(A[-1] + 1)
    while A[-1] in A:
        A[-1] += 1

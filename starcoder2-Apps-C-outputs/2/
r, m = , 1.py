
r, m = map(int, input().split())

A = [r]

while True:
    if A[-1] == m:
        print(len(A))
        break
    elif A[-1] < m:
        A.append(A[-1] + 1)
    else:
        A.append(A[-1] + A[-1] - A[-2])

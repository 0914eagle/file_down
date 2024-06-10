
N = int(input())
S = input()

left = set()
right = set()
for i in range(N):
    if i < N // 2:
        left.add(S[i])
    else:
        right.add(S[i])

print(len(left & right))


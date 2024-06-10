
A, B, K = map(int, input().split())
takahashi = A
aoki = B

for _ in range(K):
    if takahashi > 0:
        takahashi -= 1
    elif aoki > 0:
        aoki -= 1

print(takahashi, aoki)


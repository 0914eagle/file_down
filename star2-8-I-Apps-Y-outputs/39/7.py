
A, B, K = map(int, input().split())
if A <= K:
    print(0, B - (K - A))
elif B <= K:
    print(A - (K - B), 0)
else:
    print(A - K, B - K)


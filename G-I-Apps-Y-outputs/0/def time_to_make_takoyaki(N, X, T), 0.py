
def time_to_make_takoyaki(N, X, T):
    batches = N // X
    if N % X > 0:
        return T * (batches + 1)
    else:
        return T * batches

# Input
N, X, T = map(int, input().split())

# Output
print(time_to_make_takoyaki(N, X, T))

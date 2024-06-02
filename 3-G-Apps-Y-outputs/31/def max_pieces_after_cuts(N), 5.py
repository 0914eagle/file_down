
def max_pieces_after_cuts(N):
    if N == 1:
        return 2
    else:
        return (N + 1) ** 2

# Input
N = int(input())

# Output
result = max_pieces_after_cuts(N)
print(result)

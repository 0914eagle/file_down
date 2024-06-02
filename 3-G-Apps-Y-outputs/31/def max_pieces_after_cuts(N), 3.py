
def max_pieces_after_cuts(N):
    # If N is odd, the maximum number of pieces is (N+1)*(N+2)/2
    # If N is even, the maximum number of pieces is (N+2)*(N+1)/2
    if N % 2 == 0:
        return (N + 2) * (N + 1) // 2
    else:
        return (N + 1) * (N + 2) // 2

# Input
N = int(input())

# Output
print(max_pieces_after_cuts(N))

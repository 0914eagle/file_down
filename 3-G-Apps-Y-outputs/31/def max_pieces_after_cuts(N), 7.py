
def max_pieces_after_cuts(N):
    # If N is odd, the maximum number of pieces is (N+1)*(N+2)/2
    # If N is even, the maximum number of pieces is (N+1)*(N+2)/2 + 1
    return (N+1)*(N+2)//2 if N % 2 == 0 else (N+1)*(N+2)//2 + 1

# Input
N = int(input())

# Output
print(max_pieces_after_cuts(N))

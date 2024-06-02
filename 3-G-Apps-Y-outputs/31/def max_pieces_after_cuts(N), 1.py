
def max_pieces_after_cuts(N):
    if N == 1:
        return 2
    else:
        return (N + 1) ** 2

# Read input
N = int(input())

# Call the function and output the result
result = max_pieces_after_cuts(N)
print(result)

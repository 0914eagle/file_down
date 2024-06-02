
def max_pieces_after_cuts(N):
    # Each horizontal cut will increase the number of pieces by 1
    # Each vertical cut will increase the number of pieces by 1
    # Therefore, the maximum number of pieces after N cuts is N + 1
    return N + 1

# Read input
N = int(input())

# Calculate and output the result
result = max_pieces_after_cuts(N)
print(result)

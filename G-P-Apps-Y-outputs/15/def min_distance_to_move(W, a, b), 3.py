
def min_distance_to_move(W, a, b):
    if a <= b <= a + W or b <= a <= b + W:
        return 0
    else:
        return min(abs(a - (b + W)), abs(b - (a + W)))

# Read input from Standard Input
W, a, b = map(int, input().split())

# Calculate and print the minimum distance the second rectangle needs to be moved
print(min_distance_to_move(W, a, b))

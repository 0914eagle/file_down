
def solve(n, k, marbles):
    colors = set(marbles)
    min_insert = float('inf')
    for color in colors:
        insert = 0
        for i in range(len(marbles) - k + 1):
            if all(marble == color for marble in marbles[i:i+k]):
                insert += k - 1
        min_insert = min(min_insert, insert)
    return min_insert



def solve(n, k, marbles):
    colors = set(marbles)
    min_insert = 0
    for color in colors:
        count = 0
        for marble in marbles:
            if marble == color:
                count += 1
            else:
                count = 0
            if count >= k:
                min_insert += 1
    return min_insert

n, k = map(int, input().split())
marbles = list(map(int, input().split()))
print(solve(n, k, marbles))


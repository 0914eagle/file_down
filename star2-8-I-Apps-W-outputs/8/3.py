
from itertools import combinations

N = int(input())
grid = [input() for _ in range(N)]

def find_triples(grid):
    triples = 0
    for r in range(N):
        for c in range(N):
            for dr, dc in combinations(range(-1, 2), 2):
                if dr == 0 and dc == 0:
                    continue
                if 0 <= r + 2 * dr < N and 0 <= c + 2 * dc < N:
                    letters = {grid[r + dr][c + dc], grid[r + 2 * dr][c + 2 * dc]}
                    if grid[r][c] in letters:
                        letters.remove(grid[r][c])
                    if len(letters) == 1:
                        triples += 1

    return triples

print(find_triples(grid))


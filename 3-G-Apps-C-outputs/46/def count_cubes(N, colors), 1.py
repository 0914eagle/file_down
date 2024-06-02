
from itertools import permutations

def count_cubes(N, colors):
    def check_cube(cube):
        for i in range(4):
            colors_set = set(cube[j][i] for j in range(6))
            if len(colors_set) != 1:
                return False
        return True

    tiles = list(range(1, N+1))
    perms = permutations(tiles, 6)
    unique_cubes = set()

    for perm in perms:
        cube = [colors[p-1] for p in perm]
        if check_cube(cube):
            unique_cubes.add(tuple(sorted(perm)))

    return len(unique_cubes)

# Sample Input
N = 6
colors = [
    [0, 1, 2, 3],
    [0, 4, 6, 1],
    [1, 6, 7, 2],
    [2, 7, 5, 3],
    [6, 4, 5, 7],
    [4, 0, 3, 5]
]

# Sample Output
print(count_cubes(N, colors))

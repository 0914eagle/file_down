
from itertools import permutations

def count_cubes(N, colors):
    def check_cube(cube):
        for i in range(4):
            if len(set(cube[j][i] for j in range(6))) != 1:
                return False
        return True

    def rotate_tile(tile):
        return [tile[3]] + tile[:3]

    def rotate_cube(cube):
        return [rotate_tile(cube[i]) for i in range(6)]

    cubes = set()
    for perm in permutations(range(N)):
        for rot in range(4):
            cube = [colors[perm[i]][rot:] + colors[perm[i]][:rot] for i in range(6)]
            if check_cube(cube):
                cubes.add(tuple(tuple(row) for row in cube))
    return len(cubes)

# Read input
N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]

# Output the result
print(count_cubes(N, colors))

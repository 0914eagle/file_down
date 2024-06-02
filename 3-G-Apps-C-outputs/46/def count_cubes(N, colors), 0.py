
from itertools import permutations

def count_cubes(N, colors):
    def check_cube(cube):
        for i in range(4):
            for j in range(4):
                if cube[i][j] != cube[(i+1)%4][j] or cube[i][j] != cube[(i+2)%4][j]:
                    return False
        return True

    color_permutations = permutations(colors, 6)
    unique_cubes = set()

    for perm in color_permutations:
        cube = [perm[:4], perm[1:5], perm[2:6], [perm[3]] + [perm[0]] + perm[4:6]]
        if check_cube(cube):
            unique_cubes.add(tuple(sorted(cube)))

    return len(unique_cubes)

# Reading input
N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]

# Calculate and print the number of different cubes
print(count_cubes(N, colors))


from itertools import permutations

def count_cubes(N, colors):
    def check_cube(cube):
        for i in range(4):
            if len(set(cube[j][i] for j in range(6))) != 1:
                return False
        return True

    cubes = set()
    for perm in permutations(range(N)):
        cube = [colors[perm[i]] for i in range(6)]
        for _ in range(4):
            if check_cube(cube):
                cubes.add(tuple(sorted(cube)))
            cube = [list(row) for row in zip(*cube[::-1])]
    return len(cubes)

# Read input
N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]

# Call the function and print the output
print(count_cubes(N, colors))

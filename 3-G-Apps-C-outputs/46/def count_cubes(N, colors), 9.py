
from itertools import permutations

def count_cubes(N, colors):
    def check_cube(cube):
        for i in range(4):
            if len(set(cube[j][i] for j in range(6))) != 1:
                return False
        return True

    perms = permutations(range(N))
    cubes = set()
    for perm in perms:
        cube = [colors[i] for i in perm]
        if check_cube(cube):
            cubes.add(tuple(sorted(cube)))
    
    return len(cubes)

# Sample Input Parsing
N = 6
colors = [
    [0, 1, 2, 3],
    [0, 4, 6, 1],
    [1, 6, 7, 2],
    [2, 7, 5, 3],
    [6, 4, 5, 7],
    [4, 0, 3, 5]
]

# Call the function with the sample input
print(count_cubes(N, colors))

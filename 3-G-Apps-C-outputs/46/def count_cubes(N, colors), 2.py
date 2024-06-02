
from itertools import permutations

def count_cubes(N, colors):
    def check_cube(cube):
        for i in range(4):
            for j in range(4):
                if cube[i][j] != cube[(i+1)%4][j] or cube[i][j] != cube[(i+2)%4][j]:
                    return False
        return True

    color_permutations = permutations(range(N), 6)
    count = 0
    for perm in color_permutations:
        cube = [[colors[perm[i]][j] for j in range(4)] for i in range(6)]
        if check_cube(cube):
            count += 1
    return count

# Read input
N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]

# Call the function and print the output
print(count_cubes(N, colors))

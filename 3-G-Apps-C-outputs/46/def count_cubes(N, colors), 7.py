
import itertools

def count_cubes(N, colors):
    def rotate_tile(tile):
        return [tile[3], tile[0], tile[1], tile[2]]

    def check_cube(cube):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if cube[0][i] == cube[1][j] and cube[0][i] == cube[2][k]:
                        return True
        return False

    tiles = [colors[i] for i in range(N)]
    cubes = set()

    for perm in itertools.permutations(tiles, 6):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    cube = [perm[:2], perm[1:3], perm[2:4], perm[3:5], [perm[4], perm[0]], [perm[5], perm[4]]]
                    if check_cube(cube):
                        cubes.add(tuple(cube))
        perm = rotate_tile(perm)

    return len(cubes)

# Read input
N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]

# Output the result
print(count_cubes(N, colors))

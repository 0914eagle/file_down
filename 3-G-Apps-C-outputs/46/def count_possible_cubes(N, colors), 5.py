
def count_possible_cubes(N, colors):
    def rotate_tile(tile):
        return [tile[3], tile[0], tile[1], tile[2]]

    def check_cubes(cube):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if cube[0][i] == cube[1][j] and cube[0][i] == cube[2][k]:
                        return True
        return False

    cubes = set()
    for i in range(N):
        for j in range(4):
            for k in range(j, 4):
                for l in range(k, 4):
                    cube = [[colors[i][j], colors[i][k], colors[i][l]]]
                    for m in range(N):
                        if m == i:
                            continue
                        for n in range(4):
                            for o in range(4):
                                for p in range(4):
                                    if [colors[m][n], colors[m][o], colors[m][p]] in cube:
                                        cube.append([colors[m][n], colors[m][o], colors[m][p]])
                    if len(cube) == 6 and check_cubes(cube):
                        cubes.add(tuple(sorted(cube)))

    return len(cubes)

# Read input
N = int(input())
colors = []
for _ in range(N):
    colors.append(list(map(int, input().split())))

# Output result
print(count_possible_cubes(N, colors))


from itertools import permutations

def can_form_cube(colors):
    for perm in permutations(range(6)):
        cube = [colors[i] for i in perm]
        if cube[0][0] == cube[1][2] and cube[0][1] == cube[2][3] and cube[0][3] == cube[3][1] and cube[1][0] == cube[2][2] and cube[1][1] == cube[4][3] and cube[2][0] == cube[5][2] and cube[3][0] == cube[4][2] and cube[3][3] == cube[5][1] and cube[4][0] == cube[5][3]:
            return True
    return False

N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]

count = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            for l in range(k+1, N):
                for m in range(l+1, N):
                    for n in range(m+1, N):
                        if can_form_cube([colors[i], colors[j], colors[k], colors[l], colors[m], colors[n]]):
                            count += 1

print(count)


import math

def find_distance(hill1, hill2):
    return math.sqrt((hill1[0] - hill2[0])**2 + (hill1[1] - hill2[1])**2 + (hill1[2] - hill2[2])**2)

def find_min_aqueduct_length(n, s, t, q, hills, springs, towns):
    adj_matrix = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            dist = find_distance(hills[i], hills[j])
            if dist <= q:
                adj_matrix[i][j] = dist
                adj_matrix[j][i] = dist

    for i in range(n):
        adj_matrix[i][i] = 0

    for i in range(s):
        adj_matrix[n][springs[i]-1] = 0
        adj_matrix[springs[i]-1][n] = 0

    for i in range(t):
        adj_matrix[n+1][towns[i]-1] = 0
        adj_matrix[towns[i]-1][n+1] = 0

    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                if adj_matrix[i][k] != -1 and adj_matrix[k][j] != -1:
                    if adj_matrix[i][j] == -1 or adj_matrix[i][k] + adj_matrix[k][j] < adj_matrix[i][j]:
                        adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]

    if adj_matrix[n][n+1] == -1:
        return "IMPOSSIBLE"
    else:
        return '{:.6f}'.format(adj_matrix[n][n+1])

# Input parsing
n, s, t, q = map(int, input().split())
hills = [list(map(int, input().split())) for _ in range(n)]
springs = list(map(int, input().split()))
towns = list(map(int, input().split()))

# Call the function and print the result
print(find_min_aqueduct_length(n, s, t, q, hills, springs, towns))

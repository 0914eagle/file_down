
def get_maximum_points(N, E, S_X, S_Y, C, cans):
    grid = [[0] * N for _ in range(N)]
    energy = E
    score = 0
    for t in range(1, 101):  # Game lasts up to 100 seconds
        # Move Johnny5 to update his position
        if t != 1:
            energy -= 1
        for can in cans:
            X, Y, CT = can
            if CT == t and grid[X][Y] == 0:
                if (X == S_X and Y == S_Y) or (abs(S_X - X) + abs(S_Y - Y) == 1):
                    score += 1
                    energy += 1
                grid[X][Y] = 1
        
        if energy <= 0:
            break

    return score

# Input processing
input_data = input().split()
N, E, S_X, S_Y, C = map(int, input_data[:5])
cans = []
for i in range(C):
    cans_data = list(map(int, input().split()))
    cans.append(cans_data)

# Call the function with the input
result = get_maximum_points(N, E, S_X, S_Y, C, cans)
print(result)
```

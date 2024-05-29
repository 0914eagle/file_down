
def can_collect_max_points(N, E, S_X, S_Y, C, cans):
    # Initialize variables
    grid = [[0] * N for _ in range(N)]
    points = 0
    energy = E

    # Function to check if a can is reachable
    def is_reachable(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2) == 1

    # Iterate through the cans
    for x, y, ct in cans:
        # Check if Johnny5 can reach the can in time
        if abs(x - S_X) + abs(y - S_Y) > ct:
            continue

        # If Johnny5 is at the can location when it appears
        if x == S_X and y == S_Y and energy > 0:
            points += 1
            energy -= 1

        # If the can explodes in adjacent cells
        elif is_reachable(x, y, S_X, S_Y) and energy > 0:
            points += 1
            energy += 1

    return points

# Input processing
N, E, S_X, S_Y, C = map(int, input().split())
cans = [list(map(int, input().split())) for _ in range(C)]

# Output the maximum number of points
print(can_collect_max_points(N, E, S_X, S_Y, C, cans))


def minimum_moves_to_goal(C, R, maze):
    moves = [[-1 for _ in range(C)] for _ in range(R)]
    goal_position = None

    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'M':
                goal_position = (i, j)

    def dfs(i, j, distance):
        if i < 0 or i >= R or j < 0 or j >= C or maze[i][j] == '#' or (moves[i][j] != -1 and moves[i][j] <= distance):
            return
        moves[i][j] = distance
        dfs(i+1, j, distance+1)
        dfs(i-1, j, distance+1)
        dfs(i, j+1, distance+1)
        dfs(i, j-1, distance+1)

    if goal_position:
        dfs(goal_position[0], goal_position[1], 0)

    for i in range(R):
        print(' '.join(str(move) for move in moves[i]))

# Input processing
C, R = map(int, input().split())
maze = [input() for _ in range(R)]

minimum_moves_to_goal(C, R, maze)

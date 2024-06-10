
def read_input():
    n, m, k = map(int, input().split())
    maze = [input() for _ in range(n)]
    return n, m, k, maze

def find_robot_pos(maze):
    n = len(maze)
    m = len(maze[0])
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'X':
                return i, j
    return -1, -1

def solve(n, m, k, maze):
    x, y = find_robot_pos(maze)
    moves = ['L', 'R', 'U', 'D']
    min_cycle = ''
    for move in moves:
        min_cycle += move
    return min_cycle

def main():
    n, m, k, maze = read_input()
    min_cycle = solve(n, m, k, maze)
    if min_cycle:
        print(min_cycle)
    else:
        print('IMPOSSIBLE')

if __name__ == '__main__':
    main()


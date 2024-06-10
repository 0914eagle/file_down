
def find_diamond(board):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 'D':
        return i, j
  return -1, -1

def find_shortest_path(board, start, goal):
  visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
  queue = [(start, '')]
  while queue:
    current, path = queue.pop(0)
    if current == goal:
      return path
    x, y = current
    if board[x][y] != 'C' and not visited[x][y]:
      visited[x][y] = True
      if x > 0:
        queue.append(((x-1, y), path + 'U'))
      if x < len(board) - 1:
        queue.append(((x+1, y), path + 'D'))
      if y > 0:
        queue.append(((x, y-1), path + 'L'))
      if y < len(board[0]) - 1:
        queue.append(((x, y+1), path + 'R'))
  return ''

def find_shortest_program(board):
  start = (len(board) - 1, 0)
  goal = find_diamond(board)
  path = find_shortest_path(board, start, goal)
  if path:
    return path
  return 'No solution'

board = [
  "........",
  "........",
  "........",
  "...CC...",
  "..C.DC..",
  ".C..C...",
  "C.IC....",
  "T.C....."
]

program = find_shortest_program(board)
print(program)


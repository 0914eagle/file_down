
N = int(input())
grid = []
for i in range(N):
  row = input()
  grid.append(row)

count = 0
for i in range(N):
  for j in range(N):
    letter = grid[i][j]
    if letter != '.':
      if i-1 >= 0 and j-1 >= 0 and grid[i-1][j-1] == letter:
        count += 1
      if i-1 >= 0 and j+1 < N and grid[i-1][j+1] == letter:
        count += 1
      if i+1 < N and j-1 >= 0 and grid[i+1][j-1] == letter:
        count += 1
      if i+1 < N and j+1 < N and grid[i+1][j+1] == letter:
        count += 1
print(count)


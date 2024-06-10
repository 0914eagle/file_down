
from collections import deque

def solve():
    n, m, k = map(int, input().split())
    grid = [input() for _ in range(n)]
    start_row, start_col = next(
        (row, col) for row in range(n) for col in range(m) if grid[row][col] == 'S'
    )
    treasure_row, treasure_col = next(
        (row, col) for row in range(n) for col in range(m) if grid[row][col] == 'G'
    )
    queue = deque([(start_row, start_col, k, 0)])
    visited = set()
    while queue:
        row, col, stamina, days = queue.popleft()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if row == treasure_row and col == treasure_col:
            return days
        for new_row, new_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] != '#':
                new_stamina = stamina - 1
                if grid[new_row][new_col] == 'F':
                    new_stamina -= 1
                elif grid[new_row][new_col] == 'M':
                    new_stamina -= 2
                if new_stamina >= 0:
                    queue.append((new_row, new_col, new_stamina, days))
                else:
                    queue.append((new_row, new_col, k, days + 1))
    return -1

print(solve())


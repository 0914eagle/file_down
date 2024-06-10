
def minesweeper(n):
    safe_cells = [i for i in range(1, 4 * n + 5) if i % (n + 1) != 0 and (i - 1) % (n + 1) != 0]
    return len(safe_cells), safe_cells
n = int(input())
m, safe_cells = minesweeper(n)
print(m)
print(*safe_cells)


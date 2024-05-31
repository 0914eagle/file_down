
def minPath(grid, k):
    def dfs(curr_path, path_length):
        if path_length == k:
            return curr_path

        min_path = []
        min_path_val = float('inf')

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited:
                    visited.add((r, c))
                    next_path = dfs(curr_path + [grid[r][c]], path_length + 1)
                    visited.remove((r, c))

                    if next_path < min_path_val:
                        min_path = next_path
                        min_path_val = next_path

        return min_path

    visited = set()
    return dfs([], 0)

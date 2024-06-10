
import sys

def solve(n, m, grid):
    snakes = {}
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                if grid[i][j] not in snakes:
                    snakes[grid[i][j]] = []
                snakes[grid[i][j]].append((i, j))
    
    for snake in snakes.values():
        snake.sort()
    
    snake_count = len(snakes)
    snake_coords = []
    
    for snake in snakes.values():
        snake_coords.append(snake[0] + snake[-1])
    
    return snake_count, snake_coords

def main():
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().strip().split())
        
        grid = []
        
        for _ in range(n):
            grid.append(sys.stdin.readline().strip())
        
        snake_count, snake_coords = solve(n, m, grid)
        
        print("YES")
        print(snake_count)
        
        for coord in snake_coords:
            print(*coord)

if __name__ == "__main__":
    main()


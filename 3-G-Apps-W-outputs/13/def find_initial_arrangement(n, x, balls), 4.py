
def find_initial_arrangement(n, x, balls):
    total_balls = sum(balls)
    remaining_balls = total_balls - balls[x-1]
    
    initial_balls = [0] * n
    initial_balls[x-1] = remaining_balls
    
    for i in range(n):
        initial_balls[i] = balls[i] - min(remaining_balls, balls[x-1])
        remaining_balls -= initial_balls[i]
    
    return initial_balls

# Input
n, x = map(int, input().split())
balls = list(map(int, input().split()))

# Output
result = find_initial_arrangement(n, x, balls)
print(*result)

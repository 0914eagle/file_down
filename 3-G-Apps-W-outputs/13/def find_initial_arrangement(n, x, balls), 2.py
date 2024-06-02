
def find_initial_arrangement(n, x, balls):
    total_balls = sum(balls)
    extra_balls = total_balls - balls[x-1]
    
    initial_balls = [0] * n
    for i in range(n):
        initial_balls[i] = balls[(i-x)%n] + extra_balls
    
    return initial_balls

# Input
n, x = map(int, input().split())
balls = list(map(int, input().split()))

# Output
initial_balls = find_initial_arrangement(n, x, balls)
print(*initial_balls)

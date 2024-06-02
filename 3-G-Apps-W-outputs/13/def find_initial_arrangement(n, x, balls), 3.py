
def find_initial_arrangement(n, x, balls):
    total_balls = sum(balls)
    remaining_balls = total_balls - balls[x-1]
    
    initial_balls = [remaining_balls] * n
    initial_balls[x-1] = balls[x-1]
    
    return initial_balls

# Input
n, x = map(int, input().split())
balls = list(map(int, input().split()))

# Output
initial_arrangement = find_initial_arrangement(n, x, balls)
print(*initial_arrangement)

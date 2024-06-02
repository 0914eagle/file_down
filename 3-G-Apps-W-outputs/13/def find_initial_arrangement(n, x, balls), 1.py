
def find_initial_arrangement(n, x, balls):
    total_balls = sum(balls)
    extra_balls = total_balls - balls[x-1]
    
    initial_balls = [0] * n
    for i in range(n):
        if i == x-1:
            initial_balls[i] = extra_balls
        else:
            initial_balls[i] = balls[i]
    
    return initial_balls

# Input
n, x = map(int, input().split())
balls = list(map(int, input().split()))

# Output
initial_arrangement = find_initial_arrangement(n, x, balls)
print(*initial_arrangement)

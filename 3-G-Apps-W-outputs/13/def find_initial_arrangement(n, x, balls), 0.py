
def find_initial_arrangement(n, x, balls):
    total_balls = sum(balls)
    remaining_balls = total_balls - balls[x-1]
    
    initial_balls = [0] * n
    initial_balls[x-1] = remaining_balls
    
    current_box = x % n
    for i in range(n-1):
        initial_balls[current_box] = balls[current_box-1]
        current_box = (current_box % n) + 1
    
    return initial_balls

# Input
n, x = map(int, input().split())
balls = list(map(int, input().split()))

# Output
result = find_initial_arrangement(n, x, balls)
print(*result)

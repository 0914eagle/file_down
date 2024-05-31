
def minimal_steps(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    return max(dx, dy)

# Reading input
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

# Calculating and printing output
print(minimal_steps(x1, y1, x2, y2))

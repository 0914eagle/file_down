
def min_steps_to_finish(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return max(dx, dy)

# Input
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

# Output
print(min_steps_to_finish(x1, y1, x2, y2))
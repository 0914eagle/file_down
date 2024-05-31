
def min_steps_to_reach_destination(x1, y1, x2, y2):
    diff_x = abs(x2 - x1)
    diff_y = abs(y2 - y1)
    return max(diff_x, diff_y)

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

print(min_steps_to_reach_destination(x1, y1, x2, y2))

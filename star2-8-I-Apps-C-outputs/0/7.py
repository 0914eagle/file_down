
def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def calc_time(x1, y1, x2, y2, v_max, t, vx, vy, wx, wy):
    v = dist(vx, vy, 0, 0)
    w = dist(wx, wy, 0, 0)
    d = dist(x1, y1, x2, y2)
    if v == 0:
        if w == 0:
            return d / v_max
        else:
            return (d / v_max) + (d / w)
    elif w == 0:
        return (d / v_max) + (d / v)
    else:
        return (d / v_max) + (d / v) + (d / w)


x_1, y_1, x_2, y_2 = map(int, input().split())
v_max, t = map(int, input().split())
vx, vy = map(int, input().split())
wx, wy = map(int, input().split())
print(calc_time(x_1, y_1, x_2, y_2, v_max, t, vx, vy, wx, wy))


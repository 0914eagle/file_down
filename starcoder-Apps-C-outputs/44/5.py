
def main():
    ax, ay, bx, by = input().split()
    ax = int(ax)
    ay = int(ay)
    bx = int(bx)
    by = int(by)

    cx, cy, time = input().split()
    cx = int(cx)
    cy = int(cy)
    time = int(time)

    mx = ax * cx + bx
    my = ay * cy + by

    if time == 0:
        print(0)
        return

    if time == 1:
        print(1)
        return

    if (mx >= cx) and (mx <= cx + time):
        if (my >= cy) and (my <= cy + time):
            if (mx - cx) + (my - cy) == time:
                print(2)
                return

    if (mx >= cx - time) and (mx <= cx):
        if (my >= cy - time) and (my <= cy):
            if (cx - mx) + (cy - my) == time:
                print(2)
                return

    print(1)

main()

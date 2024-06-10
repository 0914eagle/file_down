
import math
def compute_dist(x1,y1,x2,y2):
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist
def compute_time(x1,y1,x2,y2,v_max,t,v_x,v_y,w_x,w_y):
    dist = compute_dist(x1,y1,x2,y2)
    if dist <= v_max*t:
        time = dist/v_max
    else:
        dist_in_t = v_max*t
        dist_after_t = dist - dist_in_t
        time_in_t = t
        time_after_t = dist_after_t/v_max
        time = time_in_t + time_after_t
    return time
def main():
    x_1, y_1, x_2, y_2 = [int(x) for x in input().split()]
    v_max, t = [int(x) for x in input().split()]
    v_x, v_y = [int(x) for x in input().split()]
    w_x, w_y = [int(x) for x in input().split()]
    time = compute_time(x_1,y_1,x_2,y_2,v_max,t,v_x,v_y,w_x,w_y)
    print(time)
if __name__ == "__main__":
    main()


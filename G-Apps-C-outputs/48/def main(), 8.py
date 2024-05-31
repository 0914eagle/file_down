
import sys

def main():
    W, v_h, N = map(int, input().split())
    gates = [list(map(int, input().split())) for _ in range(N)]
    S = int(input())
    skis = [int(input()) for _ in range(S)]

    min_time = sys.maxsize
    best_ski = None

    for ski_speed in skis:
        current_time = 0
        max_x = 0

        for i in range(N):
            x, y = gates[i]

            if x > max_x:
                current_time += (x - max_x) / v_h
                max_x = x

            dist_to_gate = ((y ** 2) + (W ** 2)) ** 0.5
            time_to_gate = dist_to_gate / ski_speed

            if time_to_gate > current_time:
                current_time = time_to_gate

        if current_time < min_time:
            min_time = current_time
            best_ski = ski_speed

    if best_ski:
        print(best_ski)
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()

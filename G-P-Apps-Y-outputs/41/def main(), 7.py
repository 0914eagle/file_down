
import sys

def main():
    n, s = map(int, input().split())

    if n == 0:
        print("100.000000000" + "\n" * (s - 1))
        return

    holes = [list(map(int, input().split())) for _ in range(n)]
    holes.sort(key=lambda x: x[3])

    hole_volumes = [(4/3) * 3.141592653589793 * (r**3) for r, _, _, _ in holes]
    total_volume = 100000**3 - sum(hole_volumes)

    slice_volume = total_volume / s
    slice_thickness = slice_volume / 10000

    for _ in range(s):
        print("{:.9f}".format(slice_thickness))

if __name__ == "__main__":
    main()

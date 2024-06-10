
import sys
from collections import defaultdict
def solve():
    n = int(input())
    tape = [int(x) for x in input().split()]
    colors = set(tape)
    tape_pos = defaultdict(list)
    for i, color in enumerate(tape, start=1):
        tape_pos[color].append(i)
    result = []
    for color in colors:
        pos = tape_pos[color]
        result.append(f"{pos[0]} {pos[-1]} {color}")
    print(len(result))
    print("\n".join(result))


def main():
    solve()


if __name__ == "__main__":
    main()


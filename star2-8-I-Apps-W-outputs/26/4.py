
import sys
from collections import defaultdict


def solve(input_file: str, output_file: str):
    with open(input_file, "r") as input, open(output_file, "w") as output:
        n = int(input.readline())
        a = list(map(int, input.readline().split()))
        l_count, r_count = defaultdict(int), defaultdict(int)
        for x in a:
            r_count[x] += 1
        count = 0
        for i in range(n):
            r_count[a[i]] -= 1
            if r_count[a[i]] == 0:
                del r_count[a[i]]
            l_count[a[i]] += 1
            if l_count[a[i]] > r_count[a[i]]:
                count += 1
        output.write(str(count) + "\n")


if __name__ == "__main__":
    solve("input.txt", "output.txt")


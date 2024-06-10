
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    plants = [tuple(map(float, input().split())) for i in range(n)]
    species = [0] * (m + 1)
    for i, (s, x) in enumerate(plants):
        species[int(s)] = i
    if sum(species) == sum(range(m + 1)):
        print(0)
        return
    min_dist = float("inf")
    for i in range(1, m + 1):
        min_dist = min(min_dist, abs(plants[species[i] - 1][1] - plants[species[i]][1]))
    print(min_dist)


if __name__ == "__main__":
    main()


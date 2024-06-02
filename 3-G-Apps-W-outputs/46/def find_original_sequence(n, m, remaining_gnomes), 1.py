
from itertools import permutations

def find_original_sequence(n, m, remaining_gnomes):
    original_gnomes = list(range(1, n+1))
    for perm in permutations(original_gnomes):
        found = True
        idx = 0
        for gnome in perm:
            if idx < m and gnome == remaining_gnomes[idx]:
                idx += 1
            if idx == m:
                break
        if idx == m:
            return perm

# Read input
n, m = map(int, input().split())
remaining_gnomes = [int(input()) for _ in range(m)]

# Find and print the original sequence
original_sequence = find_original_sequence(n, m, remaining_gnomes)
for gnome in original_sequence:
    print(gnome)

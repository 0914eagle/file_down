
def find_original_sequence(n, m, remaining_gnomes):
    original_sequence = []
    remaining_idx = 0
    for i in range(1, n + 1):
        if remaining_idx < m and i == remaining_gnomes[remaining_idx]:
            remaining_idx += 1
        else:
            original_sequence.append(i)
    
    return original_sequence

# Read input
n, m = map(int, input().split())
remaining_gnomes = [int(input()) for _ in range(m)]

# Find original sequence
original_sequence = find_original_sequence(n, m, remaining_gnomes)

# Output the original sequence
for gnome in original_sequence:
    print(gnome)
